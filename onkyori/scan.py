import time
import pigpio
import argparse
from command import OnkyoCommand

GPIO = 25


def parse_args():
    parser = argparse.ArgumentParser(
        description='A tool to scan all messages for your onkyo Remote Interactive (RI) interface.')
    parser.add_argument('--lower', type=lambda x: int(x, 0), nargs='?', default=0,
                        help='lower boundary (0x000-0xFFF or 0-4095) - default: 0')
    parser.add_argument('--upper', type=lambda x: int(x, 0), nargs='?', default=4095,
                        help='upper boundary (0x000-0xFFF or 0-4095) - default: 4095')
    parser.add_argument('--gpio', type=int, nargs='?', default=25,
                        help="GPIO port of your pi you want to use - default: 25")
    parser.add_argument('--delay', type=int, nargs='?', default=0,
                        help="sleep delay in seconds between commands - default: 0")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    pi = pigpio.pi()

    lower = int(args.lower)
    upper = int(args.upper)

    print('scan from {:012b} ({:04d}) to {:012b} ({:04d})'
          .format(lower, lower, upper, upper))

    for x in range(lower, upper):
        print("command: {:012b} ({:04d})".format(x, x))
        command = OnkyoCommand(pi, gpio=int(args.gpio))
        command.send(x)
        time.sleep(int(args.delay))

    pi.stop()
