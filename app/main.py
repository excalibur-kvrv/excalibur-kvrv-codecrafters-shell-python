import sys
import os

def search_in_path(program, location_return=True):
    if os.path.isfile(program) and location_return:
        return True, program
    path = os.environ.get("PATH", "")
    if path:
        for location in path.split(":"):
            if os.path.isdir(location):
                if program in os.listdir(location):
                    return True, os.path.join(location, program)
    return False, ""


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
        elif command == "pwd":
            sys.stdout.write(os.getcwd() + "\n")
            sys.stdout.flush()
        elif command.startswith("cd"):
            cmd_name, path = command.split(" ")
            if path == "~":
                os.chdir(os.getenv("HOME"))
            elif os.path.exists(path):
                os.chdir(path)
            else:
                sys.stdout.write(f"{path}: No such file or directory\n")
                sys.stdout.flush()
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
            if len(check) == 1 and check[0] in ["type", "echo", "exit", "pwd"]: 
                sys.stdout.write(f"{check[0]} is a shell builtin\n")
            elif len(check) == 1 and search_in_path(check[0], False)[0]:
                sys.stdout.write(f"{check[0]} is {search_in_path(check[0], False)[1]}\n") 
            else:
                sys.stdout.write(f"{' '.join(check)} not found\n")
            sys.stdout.flush()
        elif search_in_path(command.split(" ")[0])[0]:
            cmd, *args = command.split(" ")
            _, cmd_location = search_in_path(cmd)
            sys.stdout.write(os.popen(f"{cmd_location} {' '.join(args)}").read())
            sys.stdout.flush()
        else:
            sys.stdout.write(f"{command}: command not found\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
