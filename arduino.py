#!/usr/bin/env python3
import time
import pyfirmata2
import time
if __name__ == '__main__':
    PORT = pyfirmata2.Arduino.AUTODETECT

    board = pyfirmata2.Arduino(PORT)
    print("Communication Successfully started")
    
    while True:
        board.digital[13].write(1)
        time.sleep(1)
        board.digital[13].write(0)
        time.sleep(1)
