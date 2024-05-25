import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.

    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")
    # sys.stdout.flush()
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()
        if command.startswith("exit"):
            cmd_name, exit_code = command.split(" ")
            if exit_code == "0":
                sys.exit(int(exit_code))
        elif command.startswith("echo"):
            cmd_name, *args = command.split(" ")
            for index, word in enumerate(args):
                sys.stdout.write(f"{word}")
                if index != len(args) - 1:
                    sys.stdout.write(" ")
            sys.stdout.write("\n")
            sys.stdout.flush()
        elif command.startswith("type"):
            cmd_name, *check = command.split(" ")
            if len(check) == 1 and check[0] in ["type", "echo", "exit"]:
                sys.stdout.write(f"{check} is a shell builtin\n")
            else:
                sys.stdout.write(f"{' '.join(check)} not found\n")
            sys.stdout.flush()
        else:
            sys.stdout.write(f"{command}: command not found\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
