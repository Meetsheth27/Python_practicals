from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get credentials from .env
stored_username = os.getenv("USERNAME")
stored_password = os.getenv("PASSWORD")

# User input
username = input("Enter username: ")
password = input("Enter password: ")

# Login check
if username == stored_username and password == stored_password:
    print("Login successful ✅")
else:
    print("Invalid username or password ❌")