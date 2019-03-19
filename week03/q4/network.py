#!/usr/bin/env python

from time import sleep
from sense_hat import SenseHat
try: 
    # For Python 3
    from urllib.request import urlopen
except ImportError:
    # For Python 2
    from urllib2 import urlopen
import os


def internet():
    try:
        urlopen('http://www.google.com', timeout=1)
        return True
    except Exception as err: 
        return False

def main():
    X = [255, 0, 0]
    O = [255, 255, 255]
    question_mark = [
        O, O, O, X, X, O, O, O,
        O, O, X, O, O, X, O, O,
        O, O, O, O, O, X, O, O,
        O, O, O, O, X, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, X, O, O, O, O
    ]

    sense = SenseHat()
    count = 0

    while True:
        if internet():
            sense.clear(0,255,0)
            sleep(1)
            sense.show_message(os.popen('hostname -I').read(), scroll_speed=0.2)
            break
        else:
            sense.show_message(str(count), text_colour=[255,0,0])
            count += 1
            sleep(1)
            if count >= 10:
                sense.set_pixels(question_mark)
                break

if __name__ == '__main__':
    main()
