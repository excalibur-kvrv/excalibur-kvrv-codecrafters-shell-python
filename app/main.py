import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.

    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")
    # sys.stdout.flush()
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()
    sys.stdout.write(f"{command}: command not found")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
