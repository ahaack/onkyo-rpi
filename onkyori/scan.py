import time
import pigpio
from command import OnkyoCommand

GPIO = 25

if __name__ == "__main__":

    pi = pigpio.pi()

    for x in range(0, 4095):
        print("command: " + str(x))
        command = OnkyoCommand(pi, gpio=GPIO)
        command.send(x)

    pi.stop()
