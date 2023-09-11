contacts = {} 

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid input. Please try again."
    return wrapper

@input_error
def add_contact(command):
    _, name, phone = command.split()
    contacts[name.lower()] = phone
    return f"Contact {name} with phone number {phone} added."

@input_error
def change_phone(command):
    _, name, phone = command.split()
    contacts[name.lower()] = phone
    return f"Phone number for {name} updated."

@input_error
def get_phone(command):
    _, name = command.split()
    phone = contacts.get(name.lower())
    if phone:
        return f"The phone number for {name} is {phone}."
    else:
        return f"Contact {name} not found."

def show_all_contacts():
    if not contacts:
        return "No contacts found."
    else:
        result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
        return result

def main():
    print("Bot Assistant - How can I help you?")
    while True:
        user_input = input().strip().lower()
        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif user_input == "hello":
            print("How can I help you?")
        elif user_input.startswith("add "):
            response = add_contact(user_input)
            print(response)
        elif user_input.startswith("change "):
            response = change_phone(user_input)
            print(response)
        elif user_input.startswith("phone "):
            response = get_phone(user_input)
            print(response)
        elif user_input == "show all":
            response = show_all_contacts()
            print(response)
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
