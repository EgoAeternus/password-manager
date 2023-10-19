#This is the library we will use to encrypt the data
from cryptography.fernet import Fernet

#We create a class to model a password manager
class PasswordManager:
    """Password manager model."""
    #We create the constructor
    def __init__(self):
        #We set all in 'None' because we will use functions to fill those arguments
        self.key = None
        self.password_file = None
        self.password_dict = {}
    #------------------------------------------------------------------------------------------------------
    #We create a function to create a master key
    def create_key(self, path):
        """Creating master key"""
        #We set the argument 'self.key' to be a generated key by Fernet using 'generate_key()' method
        self.key = Fernet.generate_key()
        #We open the file in writing-binary mode
        with open(path, 'wb') as file_object:
            #When we insert "path" we are defining the name of the file at the same time
            #We write they key inside the file 
            file_object.write(self.key)
    #------------------------------------------------------------------------------------------------------
    #When we already have a key created we need to load it before tryint to acces the file 
    #With the passwords inside
    def load_key(self, path):
        """Loading master key"""
        with open(path, 'rb') as file_object:
            self.key = file_object.read()
    #------------------------------------------------------------------------------------------------------
    #We create this function to add the passwords and sites to the dictionary
    def add_password(self, site, password):
        """Function to append site/pass to dictionary encrypted."""
        #Site is the key and password the value
        self.password_dict[site] = password 
        #If the file is not empty we append the new site/password
        if self.password_file is not None:
            with open(self.password_file, 'a+') as file_object:
                #These are methods from Fernet to encrypt the passwords
                encrypted = Fernet(self.key).encrypt(password.encode())
                file_object.write(f"{site}: {encrypted.decode()}\n")
    #------------------------------------------------------------------------------------------------------
    #We need to create a file where we will store the passwords
    def create_password_file(self, path, initial_values=None):
        """Creating a file with the site/pass values."""
        #When we insert "path" we are defining the name of the file at the same time
        self.password_file = path
        #If the file is not empty we call the function 'add.password' to append the new site/pass
        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)
    #------------------------------------------------------------------------------------------------------
    def load_password_file(self, path):
        """Load the file with our site/pass values."""
        #When we set the path we are setting the name and location of the file we are calling
        self.password_file = path
        #In this case we already have the file so we only call the file in read mode
        with open(path, 'r') as file_object:
            for line in file_object:
                site, encrypted = line.split(":")
                #We decrypt the passwords for internal reading
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()
    #------------------------------------------------------------------------------------------------------    
    def get_password(self, site):
        """Calling a password by site"""
        return self.password_dict[site]
    #------------------------------------------------------------------------------------------------------
    def print_all_saved_sites(self):
        """Printing all the site/pass we have saved."""
        for sites, psswrds in self.password_dict.items():
            print(f"Site is {sites} - pass is {psswrds}")
    

