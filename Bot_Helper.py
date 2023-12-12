"""The function takes a string of user input, breaks it into words.
It returns the first word as the command cmd and the rest as a list of arguments *args.
Next, it removes extra spaces around the command and converts it to lower case."""
def parse_input(user_input):
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, *args

"""this add-function has to have 2 args (name and phone (int number))
which it will use for adding to the list"""
def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        if phone.isdigit():
            contacts[name] = phone
            return "Contact added."
        else:
            return "Second argument need to be phone number"
    else:
        return "Please try again. You should write name AND phone"

"""this change-function has to have 2 args (name and phone (int number))
which it will use for changing the user's phone to the list"""
def change_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        if name in contacts:
            if phone.isdigit():
                contacts[name] = phone
                return "Contact updated."
            else:
                return "Second argument need to be phone number"
        else:
            return f"I don't find {name} in list"   
    else:
        return "Please try again. You should write name AND phone on which change it"

"""this command show someone's phone number (if it is possible)"""
def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return f"I don't find {name} in list"
    else:
        return "Please try again. You should write ONLY name"

"""show all contacts which has in the phone book"""
def show_all(contacts):
    if contacts:
        for name, phone in contacts.items():
            return "\n".join([f"{name}: {phone}"])
    else:
        return "No contacts available."

"""main function where everything happening"""
def main():
    contacts = {}
    print("\n💫 Welcome to the assistant bot!🌟")

    """this cycle will work until user not write command "close or exit"""
    while True:
        print("""
        WRITE COMMAND:
            For example:
                - hello
                - add username phone
                - change username phone
                - phone username
                - all
                - close or exit""")
        user_input = input("\nEnter a command:")
        command, *args = parse_input(user_input)
        
        """these commands are letters' independed and for 
        each command call function which is written in the top"""
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()