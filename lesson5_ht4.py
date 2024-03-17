def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError) as e:
            if isinstance(e, ValueError):
                return "Enter the argument for the command."
            elif isinstance(e, KeyError):
                return "Contact not found."
            elif isinstance(e, IndexError):
                return "Enter the argument for the command."
    return inner

@input_error
def add_username_phone(args, contacts):
    if len(args) != 2:
        raise ValueError("Invalid number of arguments for adding a contact.")
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_username_phone(args, contacts):
    if len(args) != 2:
        raise ValueError("Invalid number of arguments for changing a contact.")
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise KeyError("Contact not found.")

@input_error
def phone_username(args, contacts):
    if len(args) != 1:
        raise ValueError("Invalid number of arguments for showing a contact.")
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}"
    else:
        raise KeyError("Contact not found.")

def all(contacts):
    if contacts:
        return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts available."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_username_phone(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":  
            print(phone_username(args, contacts))      
        elif command == "all":
            print(all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
