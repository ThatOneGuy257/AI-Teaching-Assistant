from commands import handle_command

def main():
    #class_info = find_class("C2")
    print("Teaching Assistant")
    print("------------------")
    print("Type 'help' to see command list")
    print("Type 'quit' to exit.\n")

    while True:

        command = input("> ")
        if command.lower() == "quit":
            print("Goodbye!")
            break
        handle_command(command)
        
        print()

if __name__ == "__main__":
    main()