import pyperclip, time
print('Recording Clipboard.... begin Copying and I\'ll save it to the terminal for you')
print('')
print('1. Pressing Ctrl-C will copy all saved contents to your clipboard and close the program.\n2. To selectively save links, do not Ctrl-C until you are finished.')
previous_content = ''
total_content = []
pyperclip.copy('')
try:
    while True:
        content = pyperclip.paste()
        if content != previous_content:
            print(content)
            total_content.append(content)
            previous_content = content
        time.sleep(0.01)
except KeyboardInterrupt:
    pyperclip.copy(total_content)
    pass