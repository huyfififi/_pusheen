import pusheen.version
import shutil
import time
import argparse


PUSHEEN = [
    '   ▐▀▄       ▄▀▌   ▄▄▄▄▄▄▄              ',
    '   ▌▒▒▀▄▄▄▄▄▀▒▒▐▄▀▀▒██▒██▒▀▀▄           ',
    '  ▐▒▒▒▒▀▒▀▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄         ',
    '  ▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▒▒▒▒▒▒▒▒▀▄       ',
    '▀█▒▒▒█▌▒▒█▒▒▐█▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌      ',
    '▀▌▒▒▒▒▒▒▀▒▀▒▒▒▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐   ▄▄ ',
    '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▄█▒█ ',
    '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▀  ',
    '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▀    ',
    '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌     ',
    ' ▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐      ',
    ' ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌      ',
    '  ▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐       ',
    '  ▐▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▌       ',
    '    ▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀         ',
]

PUSHEEN_SWING = [
    '   ▐▀▄       ▄▀▌   ▄▄▄▄▄▄▄              ',
    '   ▌▒▒▀▄▄▄▄▄▀▒▒▐▄▀▀▒██▒██▒▀▀▄           ',
    '  ▐▒▒▒▒▀▒▀▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄         ',
    '  ▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▒▒▒▒▒▒▒▒▀▄       ',
    '▀█▒▒▒█▌▒▒█▒▒▐█▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌      ',
    '▀▌▒▒▒▒▒▒▀▒▀▒▒▒▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐      ',
    '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐     ',
    '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▄    ',
    '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▐▄  ',
    '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▀▌▒█ ',
    ' ▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐   ▀▀ ',
    ' ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌      ',
    '  ▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐       ',
    '  ▐▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▌       ',
    '    ▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀         ',
]

SIZE_COLUMNS_TERMINAL = shutil.get_terminal_size().columns
SIZE_COLUMNS_PUSHEEN = len(PUSHEEN[0])


def parse():
    usage = 'pusheen [--run] [--time TIME] [--percentage PERCENTAGE]'
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument('-v',
                        '--version',
                        help='print product version and exit',
                        action='version',
                        version=f'{pusheen.__version__}')
    parser.add_argument('-r', '--run', action='store_true', help='pusheen will run')
    parser.add_argument('-t', '--time', type=float, default=0.04, help='set sleep time')
    parser.add_argument('-p', '--percentage', type=int, default=30, help='set percentage of distance (0 to 100)')
    args = parser.parse_args()
    if args.percentage > 100:
        args.percentage = 100
    elif args.percentage < 0:
        args.percentage = 0
    return args


def swing_pusheen(counter: int, frequency: int):
    if (counter % frequency) < (frequency / 2):
        return PUSHEEN
    else:
        return PUSHEEN_SWING


def display_pusheen(time_sleep, percentage_show, from_right):
    if from_right:
        print('\033[34m', end='')
        for i in range(int(SIZE_COLUMNS_TERMINAL * percentage_show / 100)):
            time.sleep(time_sleep)
            print('\n'.join(map(lambda x: (' ' * (SIZE_COLUMNS_TERMINAL - i) + x)[:SIZE_COLUMNS_TERMINAL], swing_pusheen(i, 10))) + '\n' + '\033[16A')
    else:
        print('\033[31m', end='')
        for i in reversed(range(int(SIZE_COLUMNS_TERMINAL * percentage_show / 100))):
            time.sleep(time_sleep)
            print('\n'.join(map(lambda x: (' ' * (SIZE_COLUMNS_TERMINAL - i) + x)[:SIZE_COLUMNS_TERMINAL], swing_pusheen(i, 10))) + '\n' + '\033[16A')
    time.sleep(time_sleep)
        

def main():
    args = parse()
    if args.run:
        display_pusheen(0.01, 100, True)
    else:
        display_pusheen(args.time, args.percentage, True)
        display_pusheen(args.time, args.percentage, False)


if __name__ == '__main__':
    main()
