def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a valid command."
        except ValueError:
            return "Invalid input. Please try again."
        except IndexError:
            return "Invalid input. Please try again."

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def show_all_contacts(args, contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "add":
            args = input("Enter the argument for the command: ").split()
            print(add_contact(args, contacts))
        elif command == "all":
            args = None
            print(show_all_contacts(args, contacts))
        elif command == "quit":
            break
        else:
            print("Enter a valid command.")

if __name__ == "__main__":
    main()

