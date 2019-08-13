import argparse
import sys
import time
import pigpio
from command import OnkyoCommand


def parse_args():
    parser = argparse.ArgumentParser(
        description='A tool to control onkyo devices over Remote Interactive (RI) interface.')
    parser.add_argument('message', metavar='message', type=lambda x: int(x, 0), nargs=1,
                        help='message (0x000-0xFFF or 0-4095) to send to your onkyo device')
    parser.add_argument('--gpio', type=int, nargs='?', default=25,
                        help="GPIO port of your pi you want to use - default: 25")

    return parser.parse_args()


if __name__ == "__main__":

    args = parse_args()

    pi = pigpio.pi()

    message = args.message[0]
    print('send message {:012b} ({:04d}) via GPIO {:d}'
          .format(message, message, args.gpio))

    command = OnkyoCommand(pi, gpio=int(args.gpio))
    command.send(int(args.message[0]))
    time.sleep(1)

    pi.stop()
