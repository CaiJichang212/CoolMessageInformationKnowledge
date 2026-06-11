#!/usr/bin/env python3
"""Use Playwright to fetch the page with a real browser to bypass Cloudflare."""
import sys
from playwright.sync_api import sync_playwright

URL = "https://developers.openai.com/codex/learn/best-practices"
OUT = "/Users/lzc/TNTprojectZ/CoolExplore/codex-best-practices/codex-best-practices.html"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        viewport={"width": 1440, "height": 900},
        locale="en-US",
    )
    page = context.new_page()
    page.goto(URL, wait_until="networkidle", timeout=60000)
    page.wait_for_timeout(2000)
    html = page.content()
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Saved {len(html)} bytes to {OUT}")
    browser.close()
