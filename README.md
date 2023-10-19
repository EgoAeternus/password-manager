# Password Manager

This Python-based password manager is a lightweight and secure solution for managing website passwords locally. It utilizes the Fernet encryption library to protect your password data. Below is an overview of the code and its functionalities:

## Features

### Encryption with Fernet

The heart of this password manager is its use of the [Fernet](https://cryptography.io/en/latest/fernet/) encryption library. Fernet is a symmetric key encryption system, making it an excellent choice for securing your passwords. Here's how it works:

- **Master Key Creation**: When you choose to create a new key (Option 1), the code generates a random master key using Fernet. This key is used for both encrypting and decrypting passwords.

- **Password Encryption**: When you add a new password (Option 5), the code encrypts the password using the Fernet key before storing it in the password file. This ensures that your passwords remain confidential.

- **Password Decryption**: When you need to retrieve a password (Option 6), the code decrypts the stored password using the master key, allowing you to access your site passwords securely.

### Password File Management

The password manager allows you to create and manage a password file. Here's how it works:

- **Create a New Password File (Option 3)**: You can create a new password file or load an existing one. This file stores your encrypted site-password pairs.

- **Load an Existing Password File (Option 4)**: If you already have a password file, you can load it to access your stored passwords.

### Password Management

You can add, retrieve, and view your stored passwords using the following options:

- **Add a New Password (Option 5)**: Add new site-password pairs to the password manager. The manager encrypts and stores them securely in the password file.

- **Get a Password (Option 6)**: Retrieve a password by specifying the
