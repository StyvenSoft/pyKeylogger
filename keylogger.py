import pynput.keyboard

key_list = []

def print():
    key = ''.join(key_list)
    print(key)

def press(key):
    key1 = convertOne(key)
    # print("Tecla {}".format(key1))

    if key1 == 'Key.esc':
        print('Exit...')

    elif key1 == 'key.space':
        key_list.append()

    else:
        key_list.append(key1)

'''

if key1 === 'Kay.space
:
def release(key):
    key1 = convertOne(key)
    print("Tecla rel {}".format(key1))

    if str(key) == "Key.esc":
        print("Exit...")
        return False
'''

def convertOne(key):
    if isinstance(key, pynput.keyboard.KeyCode):
        return key.char
    else:
        return str(key)

with pynput.keyboard.Listener(on_press=press) as listen:
    listen.join()
