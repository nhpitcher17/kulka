import os
import sys
import time

sys.path.append(os.path.abspath("../"))

from kulka import Kulka

def main():
    addr = '68:86:E7:06:FD:1D'
    with Kulka(addr) as kulka:
        kulka.set_inactivity_timeout(3600)

        for _ in range(10):
            kulka.set_rgb(0, 0xFF, 0)
            time.sleep(0.1)
            kulka.set_rgb(0, 0, 0)
            time.sleep(0.1)
            print(kulka.sequence())


        kulka.sleep()


if __name__ == '__main__':
    main()
