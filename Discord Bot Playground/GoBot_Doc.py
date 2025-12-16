#discord bot to query Godot documentation


from playwright.sync_api import sync_playwright


def go_godot():
    url = 'https://docs.godotengine.org/en/stable/index.html'

    