# Basic Keylogger in Python

## Objective

The objective of this script is to create a keylogger that can be used for educational purposes or to demonstrate the potential to capture keystrokes from a target system. The keylogger records all keystrokes made by the user and saves them to a file.

### Explanation

- The script starts by importing the necessary modules: `pynput` and `pynput.keyboard`.
- The `on_press()` function is defined, which is called whenever a key is pressed. It takes the `key` parameter, which represents the pressed key.
- Inside the `on_press()` function, a file named `log.txt` is opened in append mode using the `open()` function. The `str(key)` is written to the file, followed by a newline character to separate each key press.
- The script then uses the `pynput.keyboard.Listener()` class to create a listener object. The `on_press` parameter is set to the `on_press()` function, which is called whenever a key is pressed.
- Finally, the script enters a loop using the `listener.join()` method, which waits for the listener to finish.

### Notes

Please note that this script is for educational purposes only. It should not be used to steal sensitive information from unauthorized users.

Remember to install the pynput library using pip install pynput before running the script.
