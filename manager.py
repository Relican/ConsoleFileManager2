import argparse
import utils
import os

operations = {
    "create": utils.creation,
    "copy": utils.copy,
    "delete": utils.delete,
    "nf": utils.nf,
    "search": utils.search,
    "add": utils.add,
    "analyse": utils.analyse
}


def main():
    parser = argparse.ArgumentParser(
        prog='ConsoleFileManager',
        # description='for help type -h or --help',
        add_help=True)

    parser.add_argument("operation", choices=operations.keys(), help=" - commands to enter")
    parser.add_argument("optional1", nargs='?', help=" - optional argument, usually filepath", default='None')
    parser.add_argument("optional2", nargs='?',
                        help=" - optional argument, second filepath for copy function or search string", default='None')

    args = parser.parse_args()

    function = operations[args.operation]

    if args.operation == 'copy':
        print(function(args.optional1, args.optional2))
    elif args.operation == 'search':
        print(function(args.optional1, args.optional2))
    elif args.operation == 'create':
        print(function())
    else:
        print(function(args.optional1))


if __name__ == "__main__":
    main()