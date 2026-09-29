import argparse
from .device import Enigma

def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", type=str,  default="", help="Enter the text")
    parser.add_argument("--plugboard", type=str,  default="", help="Letters to substitute. Use \"-\" letters and \";\" to separate groups")
    parser.add_argument("--rotors", type=str,  default="III-II-I", help="Rotor types from last to first, with roman numbers. Available rotors are from I to V")
    parser.add_argument("--message_key", type=str,  default="AAA", help="Rotor configuration from last to first, three letters from A to Z")

    return parser.parse_args()

def main() -> None:
    args = parse_input()

    device = Enigma(args.rotors.upper(), args.plugboard.upper())
    device.adjust(args.message_key.upper())

    print(device.start(args.text.upper()))

if __name__ == "__main__":
    main()