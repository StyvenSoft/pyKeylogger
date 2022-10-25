import pynput.keyboard

def press(key):
    print("Tecla {}".format(key))

def release(key):
    print("Tecla rel {}".format(key))

def convert():
    pass

with pynput.keyboard.Listener(on_press=press, on_release=release) as listen:
    listen.join()
