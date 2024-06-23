from argparse import ArgumentParser
from exploit import *
from offsets import *

def main():
    parser = ArgumentParser(description='pppwn')
    parser.add_argument('--interface', required=True)
    parser.add_argument('--fw',
                        choices=[
                            '700', '701', '702', '750', '751', '755',
                            '800', '801', '803', '850', '852',
                            '900', '903', '904', '950', '951', '960',
                            '1000', '1001', '1050', '1070', '1071',
                            '1100'
                        ],
                        default='1100')
    parser.add_argument('--stage1', default='/root/PPPwn-py/1100/stage1.bin')
    parser.add_argument('--stage2', default='/root/PPPwn-py/1100/stage2.bin')
    args = parser.parse_args()

    print("\033[1;32mPorting oleh bug-sys 2024 (c)\033[0m")

    try:
        with open(args.stage1, mode='rb') as f:
            stage1 = f.read()

        with open(args.stage2, mode='rb') as f:
            stage2 = f.read()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1

    if args.fw in ('700', '701', '702'):
        offs = OffsetsFirmware_700_702()
    elif args.fw in ('750', '751', '755'):
        offs = OffsetsFirmware_750_755()
    elif args.fw in ('800', '801', '803'):
        offs = OffsetsFirmware_800_803()
    elif args.fw in ('850', '852'):
        offs = OffsetsFirmware_850_852()
    elif args.fw == '900':
        offs = OffsetsFirmware_900()
    elif args.fw in ('903', '904'):
        offs = OffsetsFirmware_903_904()
    elif args.fw in ('950', '951', '960'):
        offs = OffsetsFirmware_950_960()
    elif args.fw in ('1000', '1001'):
        offs = OffsetsFirmware_1000_1001()
    elif args.fw in ('1050', '1070', '1071'):
        offs = OffsetsFirmware_1050_1071()
    elif args.fw == '1100':
        offs = OffsetsFirmware_1100()
    else:
        raise ValueError("Versi firmware tidak didukung")

    exploit = Exploit(offs, args.interface, stage1, stage2)
    exploit.run()

    return 0

if __name__ == '__main__':
    exit(main())
