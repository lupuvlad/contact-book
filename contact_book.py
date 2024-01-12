# CSV file with a header containing name, address, phone number, email address (using pandas for csv file)
# User can:
    # add a new contact
    # edit existing contacts
    # delete existing contacts
    # view details of all contacts
    # find contact details (search for a name and view the details of that contact)

import pandas as pd


def dataframe():
    column_names = ["name", "address", "phone_number", "email"]
    cf = pd.read_csv("contacts.csv", names=column_names, skiprows=1)
    return cf


def add_contact():
    """Adds a new contact to the csv file."""
    cf = dataframe()
    new_contact = [input("name: ").title(), input("address: "),
                   int(input("phone number: (use only numbers and start with the prefix, without the + sign) ")),
                   input("email: ")]
    cf.loc[len(cf)] = new_contact
    cf.to_csv("contacts.csv")


def edit_contact(row, field):
    """Edit a contact by a field selected by the user."""
    cf = dataframe()
    cf.loc[row, field] = input(f"Type a new {field}: ")
    cf.to_csv("contacts.csv")


def delete_contact(name):
    """Deletes a contact by name."""
    cf = dataframe()
    filt = (cf["name"] == name)
    cf.drop(index=cf[filt].index, inplace=True)
    cf.to_csv("contacts.csv")


def view_details_of_contacts():
    """View all the contacts."""
    cf = dataframe()
    print(cf)


def find_a_contact(name):
    """Finds a contact by name."""
    cf = dataframe()
    filt = (cf['name'] == name)
    print(cf[filt])


def main():
    action = input("What do you want to do? (add/edit/delete/view/find/exit): ")
    while action != "exit":
        if action == "add":
            add_contact()
            action = input("\nWhat do you want to do? (add/edit/delete/view/find/exit): ")

        elif action == "edit":
            row = int(input("Enter the row that you want to edit: "))
            field = (input("What field do you want to edit? (name/address/phone number/email/stop): "))
            while field != "stop":
                edit_contact(row, field)
                question = input("Do you want to edit again? (y/n) ")
                if question == "y":
                    row = int(input("Enter the row that you want to edit: "))
                    field = (input("What field do you want to edit? (name/address/phone number/email/stop): "))
                else:
                    break
            action = input("\nWhat do you want to do? (add/edit/delete/view/find/exit): ")

        elif action == "delete":
            delete_contact(input("Enter the name of the contact you want to delete: "))
            print("Contact deleted.")
            action = input("\nWhat do you want to do? (add/edit/delete/view/find/exit): ")

        elif action == "view":
            view_details_of_contacts()
            action = input("\nWhat do you want to do? (add/edit/delete/view/find/exit): ")

        elif action == "find":
            find_a_contact(input("Search the contact you are looking for by name: "))
            action = input("\nWhat do you want to do? (add/edit/delete/view/find/exit): ")

        else:
            break


main()
