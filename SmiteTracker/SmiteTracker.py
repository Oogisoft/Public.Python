#track erics smite progress

from playwright.sync_api import sync_playwright
from discord_webhook import DiscordWebhook
from pathlib import Path

disc_webhooks = Path.home() / 'home' / 'scripts'



smite_rank = 'https://tracker.gg/smite2/profile/psn/Pearadoxx/overview?gamemode=conquest-ranked&season=3'
smite_casual = 'https://tracker.gg/smite2/profile/psn/Pearadoxx/overview?gamemode=conquest&season=3'



eric_id = '472887827139526656'

#fun phrases to randomize message
#TO DO
phrases = ['phrase 1: ', 'phrase 2: ']
##
with sync_playwright() as pw:
    #setup Edge as browser for PW
    browser = pw.chromium.launch(headless=False,
        args=["--disable-blink-features=AutomationControlled"])

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

    # slight delay for bot checks
    page.wait_for_timeout(500)

    # Go to the rank page first
    page.goto(smite_rank, wait_until="domcontentloaded")

    # Wait for the specific rank image to appear
    page.wait_for_selector("img.image.object-contain")

    # Extract rank alt text
    rank = page.locator("img.image.object-contain").first.get_attribute("alt")
    last_rank_game = page.locator('div.text-18.font-bold.text-secondary').first.text_content()
    rank_wins = page.locator("span.value.text-green.truncate").first.text_content()
    rank_losses = page.locator("span.value.text-red.truncate").first.text_content()
    
    
    #Extract win loss text
    #need to load new page for this data
    page.goto(smite_casual, wait_until="domcontentloaded")
    cas_wins = page.locator("span.value.text-green.truncate").first.text_content()
    cas_losses = page.locator("span.value.text-red.truncate").first.text_content()


    #phrase creation for message to discord
    cur_rank = str(rank)
    last_ranked = str(last_rank_game)
    todays_cas_WL = f'{cas_wins} {cas_losses}'
    todays_rank_WL = f'{rank_wins} {rank_losses}'
    
    
    
    browser.close()
phrase1 = f'<@{eric_id}> is rank {cur_rank} but hasn\'t played ranked since {last_rank_game}'
phrase2 = f'Eric\'s ranked W/L is {todays_rank_WL}'
phrase3 = f'Eric\'s casual W/L is {todays_cas_WL}'
print(f'<@{eric_id}> is rank {cur_rank} but hasn\'t played ranked since {last_rank_game}')
print(f'Eric\'s ranked W/L is {todays_rank_WL}')
print(f'Eric\'s casual W/L is {todays_cas_WL}')
#Discord execution is below, mute for testing
webhook1 = DiscordWebhook(url=webhook_url, content=f"""{phrase1} \n {phrase2} \n {phrase3}""")

response = webhook1.execute()
if response.status_code == 204 or 200:
    print('succesfully ran')
else:
    print(f'I failed somewhere, check this, {response.status_code}, Response: {response.text}')

