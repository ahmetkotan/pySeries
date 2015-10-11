import pykeyboard
import time

k = pykeyboard.PyKeyboard()

k.press_key(k.alt_key)
time.sleep(0.5)

k.tap_key(k.tab_key)
k.release_key(k.alt_key)
