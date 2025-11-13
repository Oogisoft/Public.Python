#Chapt13-WebBrowser Module
#launch with command line or clipboard
import webbrowser, pyperclip, sys
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
#showmap version
webbrowser.open(f'https://www.openstreetmap.org/search?query={address}')
#gmaps version
webbrowser.open(f'https://www.google.com/maps/search/?api-1&query={address}')
