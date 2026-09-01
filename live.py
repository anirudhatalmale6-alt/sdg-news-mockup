from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.set_viewport_size({"width":1280,"height":800})
    pg.goto("https://anirudhatalmale6-alt.github.io/sdg-news-mockup/", wait_until="load")
    t = pg.evaluate("""() => {const n = performance.getEntriesByType('navigation')[0];
        return {ttfb: Math.round(n.responseStart), domInteractive: Math.round(n.domInteractive),
                load: Math.round(n.loadEventEnd), transfer: n.transferSize};}""")
    print("timings(ms):", t)
    print("title:", pg.title())
    pg.wait_for_timeout(400); pg.screenshot(path="live-check.png")
    b.close()
