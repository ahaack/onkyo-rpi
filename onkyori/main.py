import sys
import time
import pigpio
from command import OnkyoCommand

GPIO = 4

if __name__ == "__main__":

    pi = pigpio.pi()

    args = len(sys.argv)

    if args > 1:
        command = OnkyoCommand(pi, gpio=GPIO)
        command.send(int(sys.argv[1]))
        time.sleep(1)

    pi.stop()
