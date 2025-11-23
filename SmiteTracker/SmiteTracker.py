#track erics smite progress

from playwright.sync_api import sync_playwright

smite_profile = 'https://tracker.gg/smite2/profile/psn/Pearadoxx'

with sync_playwright() as pw:

    browser = pw.chromium.launch(
        headless=False,
        args=[
            "--disable-blink-features=AutomationControlled"
        ]
    )

    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 800},
        locale="en-US",
        timezone_id="America/Chicago"
    )

    # Spoof navigator.webdriver
    context.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        });
    """)

    page = context.new_page()

    # slight delay helps with bot checks
    page.wait_for_timeout(500)

    # Go to the page
    page.goto(smite_profile, wait_until="domcontentloaded")

    # Wait for the specific rank image to appear
    page.wait_for_selector("img.image.object-contain")

    # Extract rank alt text
    rank = page.locator("img.image.object-contain").first.get_attribute("alt")
    last_rank_game = page.locator('div.text-18.font-bold.text-secondary').first.text_content()
    print("Eric is currently Rank:", rank)
    print("The last time Eric played Ranked:", last_rank_game)

    browser.close()