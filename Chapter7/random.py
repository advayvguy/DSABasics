import time

def cool_cursor():
    while True:
        for char in "|/-\\":
            print(char, end="\b", flush=True)
            time.sleep(0.1)

cool_cursor()