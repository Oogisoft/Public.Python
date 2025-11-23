#track erics smite progress

from playwright.sync_api import sync_playwright
from discord_webhook import DiscordWebhook

smite_profile = 'https://tracker.gg/smite2/profile/psn/Pearadoxx'
webhook_url = 'https://discord.com/api/webhooks/1204479951911264327/GvJ2P5oPcQ9ubZuzm3w9L9O5VeKRKMIrd0iqkSAcISEVMM0W94VezJb7bdKyjbXBgD_O'
eric_id = '472887827139526656'


phrases = ['phrase 1: ', 'phrase 2: ']
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
    # Extract win loss text
    #need to load new page for this data
    page.goto('https://tracker.gg/smite2/profile/psn/Pearadoxx/overview?gamemode=conquest&season=3', wait_until="domcontentloaded")
    wins = page.locator("span.value.text-green.truncate").first.text_content()
    losses = page.locator("span.value.text-red.truncate").first.text_content()


    #phrase creation for message to discord
    cur_rank = f"<@{eric_id}> Eric is currently Rank: " + str(rank)
    last_ranked = "the last time Eric played Ranked was " + str(last_rank_game)
    todays_WL = f'His record for today is {wins} {losses}'
    
    
    
    browser.close()

webhook = DiscordWebhook(url=webhook_url, content= cur_rank + ' and ' 
                         + last_ranked + ' and ' + todays_WL)

response = webhook.execute()
if response.status_code == 204:
    print('succesfully ran')
else:
    print(f'I failed somewhere, check this, {response.status_code}, Response: {response.text}')

print(wins, losses)
