import argparse


def get_foo(foo):
    print(foo)


def set_bar(bar):
    return bar


def main():
    parser = argparse.ArgumentParser(
        description="This is the most worthless code ever written :)"
    )
    parser.add_argument(
        "--switch",
        "-s",
        help="Nope, you'r on your own here mate..",
    )

    args = parser.parse_args()

    if args.switch == "foo":
        get_foo(args.switch)
    elif args.switch == "bar":
        set_bar(args.switch)
    else:
        print("nope")


if __name__ == "__main__":
    main()
