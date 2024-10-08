import os
import getpass
import pwd

def show_system_info():
    # Get the current username
    username = getpass.getuser()
    print(f"Username: {username}")
    
    # Get additional user info from the password database (excluding actual passwords)
    user_info = pwd.getpwnam(username)
    print(f"User Info: {user_info}")
    
    # Display the home directory, shell, etc.
    print(f"Home Directory: {user_info.pw_dir}")
    print(f"Shell: {user_info.pw_shell}")

show_system_info()
