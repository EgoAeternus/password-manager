from main import*

def main():
    password = {}

    password_manager_object = PasswordManager()
    print("""What do you want to do: 
        (1) - Create a new key
        (2) - Load an existing key
        (3) - Create a new password file
        (4) - Load existing password file
        (5) - Add a new password
        (6) - Get a password
        (7) - All sites
        (q) - Quit""")
    
    done = False
    while not done:
        choice = input("Enter choice: ")
        if choice == "1":
            path = input("Enter the path: ")
            password_manager_object.create_key(path)
        elif choice == "2":
            path  = input("Enter the path: ")
            password_manager_object.load_key(path)
        elif choice == "3":
            path = input("Enter the path: ")
            password_manager_object.create_password_file(path, password)
        elif choice == "4":
            path = input("Enter the path: ")
            password_manager_object.load_password_file(path)
        elif choice == "5":
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            password_manager_object.add_password(site, password)
        elif choice == "6":
            site = input("Site you need: ")
            print(f"Password for {site} is {password_manager_object.get_password(site)}")
        elif choice == "7":
            password_manager_object.print_all_saved_sites()
        elif choice == 'q':
            done = True
            print("Bye.")
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()