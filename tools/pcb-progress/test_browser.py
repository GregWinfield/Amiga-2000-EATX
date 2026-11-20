"""Exercise the generated dashboard with headless Chromium under a Pages-style prefix."""
import argparse
from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
from threading import Thread
from urllib.parse import urlsplit

from playwright.sync_api import expect, sync_playwright

ROOT = Path(__file__).resolve().parents[2]
DASHBOARD = ROOT / "dashboard"
PREFIX = "/Amiga-2000-EATX/"


class DashboardFiles(SimpleHTTPRequestHandler):
    """Only serve dashboard/ under the project path, just like a project Pages site."""

    def do_GET(self):
        if not self.path.startswith(PREFIX):
            self.send_error(404)
            return
        self.path = "/" + self.path.removeprefix(PREFIX)
        super().do_GET()

    def log_message(self, template, *args):
        pass


@contextmanager
def preview():
    handler = partial(DashboardFiles, directory=str(DASHBOARD))
    with ThreadingHTTPServer(("127.0.0.1", 0), handler) as server:
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            yield f"http://127.0.0.1:{server.server_port}{PREFIX}"
        finally:
            server.shutdown()
            thread.join()


def camera(board):
    return tuple(float(v) for v in re.split(r"[ ,]+", board.get_attribute("viewBox").strip()))


def choose_ref(page, ref):
    page.locator("#search").fill(ref)
    page.locator(f'#reference-list button[data-ref="{ref}"]').click()
    expect(page.locator("#inspector")).to_contain_text(ref)


def test_dashboard(page, url, manifest):
    errors = []
    external = []
    origin = urlsplit(url).netloc

    def keep_local(route):
        resource = urlsplit(route.request.url)
        if resource.scheme in {"http", "https"} and resource.netloc != origin:
            external.append(route.request.url)
            route.abort()
        else:
            route.continue_()

    page.route("**/*", keep_local)
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.on("response", lambda response: errors.append(f"{response.status} {response.url}")
            if response.status >= 400 else None)
    page.goto(url)

    current = page.locator("svg.board:visible").first
    expect(current.locator("[data-ref]").first).to_be_attached(timeout=90000)
    fit = camera(current)
    choose_ref(page, "R803")
    expect(page.locator("#inspector")).to_contain_text("DIN0207")
    assert camera(current)[2] < fit[2], "Search did not focus the matching footprint"

    page.locator("#fit").click()
    socket = current.locator('[data-ref="CN605"]').first
    socket.click()
    expect(page.locator("#inspector")).to_contain_text("CN605")
    expect(page.locator("#inspector")).to_contain_text("5645235")
    page.locator("#compare").click()
    boards = page.locator("svg.board:visible")
    expect(boards).to_have_count(2)
    page.locator("#fit").click()
    baseline_fit = camera(boards.first)
    assert baseline_fit == camera(boards.last)
    page.locator("#zoom-in").click()
    assert camera(boards.first) == camera(boards.last)
    assert camera(boards.first)[2] < baseline_fit[2]
    bounds = boards.first.bounding_box()
    x, y = bounds["x"] + bounds["width"] * 0.45, bounds["y"] + bounds["height"] * 0.45
    before = camera(boards.first)
    page.mouse.move(x, y)
    page.mouse.down()
    page.mouse.move(x + 35, y + 25, steps=5)
    page.mouse.up()
    assert camera(boards.first)[:2] != before[:2] and camera(boards.first) == camera(boards.last)
    page.mouse.move(x, y)
    before = camera(boards.first)
    page.mouse.wheel(0, -140)
    page.wait_for_function(
        "width => +document.querySelector('svg.board').getAttribute('viewBox').split(/[ ,]+/)[2] < width",
        arg=before[2],
    )
    assert camera(boards.first) == camera(boards.last)
    page.locator("#reset").click()
    assert camera(boards.first) == baseline_fit

    page.locator("#compare").click()
    page.locator("#region").select_option("rtc")
    assert camera(current)[2] < fit[2]
    page.locator("#layers summary").click()
    layers = page.locator("input[data-layer]")
    toggled = 0
    for checkbox in layers.all():
        if checkbox.is_enabled():
            previous = checkbox.is_checked()
            checkbox.set_checked(not previous)
            checkbox.set_checked(previous)
            toggled += 1
    assert toggled >= 5
    page.locator("#layers summary").click()

    page.locator('[data-page="components"]').click()
    table = page.locator("#parts-table tbody tr")
    page.locator("#table-search").fill("R803")
    expect(table).to_have_count(1)
    expect(table).to_contain_text("R803")
    page.locator("#table-search").fill("")
    page.locator("#status-select").select_option("converted")
    expected = [r["ref"] for r in manifest["components"] if r["status"] == "converted"]
    assert expected
    expect(table).to_have_count(len(expected))
    for ref in expected:
        expect(page.locator("#parts-table")).to_contain_text(ref)

    page.locator('[data-page="verification"]').click()
    verification = page.locator("#verification-content")
    expect(verification).to_contain_text("ERC")
    expect(verification).to_contain_text("DRC")
    expect(verification).to_contain_text(re.compile(r"fabrication", re.I))
    page.locator('[data-page="board"]').click()
    page.set_viewport_size({"width": 820, "height": 1180})
    expect(page.locator("#workspace")).to_be_visible()
    assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth + 1"), "Tablet overflow"
    choose_ref(page, "R803")
    assert not external, f"External runtime dependency: {external}"
    assert not errors, f"Browser or static asset failures: {errors}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--browser", help="Installed Chrome/Edge executable (default: Playwright Chromium)")
    args = parser.parse_args()
    manifest = json.loads((DASHBOARD / "data/manifest.json").read_text(encoding="utf-8"))
    with preview() as url, sync_playwright() as pw:
        with pw.chromium.launch(executable_path=args.browser, headless=True) as browser:
            page = browser.new_page(viewport={"width": 1440, "height": 960})
            test_dashboard(page, url, manifest)
            broken = browser.new_page()
            broken.route("**/data/manifest.json", lambda route: route.fulfill(status=404, body="Missing"))
            broken.goto(url)
            expect(broken.locator("#notice")).to_be_visible(timeout=15000)
            expect(broken.locator("#notice")).to_contain_text(re.compile(r"fail|unavailable|missing|404|error|load", re.I))
            print(f"Chromium {browser.version}: selection, search, comparison, cameras, layers, filters, "
                  "verification, tablet layout, subdirectory assets and missing-input handling passed.")


if __name__ == "__main__":
    main()
