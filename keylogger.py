import pynput.keyboard

def press(key):
    key1 = convertOne(key)
    print("Tecla {}".format(key1))

def release(key):
    key1 = convertOne(key)
    print("Tecla rel {}".format(key1))

    if str(key) == "Key.esc":
        print("Exit...")
        return False

def convertOne(key):
    if isinstance(key, pynput.keyboard.KeyCode):
        return key.char
    else:
        return str(key)

with pynput.keyboard.Listener(on_press=press, on_release=release) as listen:
    listen.join()
