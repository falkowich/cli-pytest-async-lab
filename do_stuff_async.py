import argparse
import asyncio


async def get_foo(foo):
    print(foo)


async def set_bar(bar):
    return(bar)


async def main():
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
        await get_foo(args.switch)
    elif args.switch == "bar":
        await set_bar(args.switch)
    else:
        print("nope")


if __name__ == "__main__":
    asyncio.run(main())
