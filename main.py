import os

action = int(input(
"""
   ____ _                                                     _   _               
  / ___| |__   ___   ___  ___  ___    __ _ _ __     __ _  ___| |_(_) ___  _ __  _ 
 | |   | '_ \ / _ \ / _ \/ __|/ _ \  / _` | '_ \   / _` |/ __| __| |/ _ \| '_ \(_)
 | |___| | | | (_) | (_) \__ \  __/ | (_| | | | | | (_| | (__| |_| | (_) | | | |_ 
  \____|_| |_|\___/ \___/|___/\___|  \__,_|_| |_|  \__,_|\___|\__|_|\___/|_| |_(_)
                                                                                

    1. Make a directory in current directory
    2. Remove a directory in current directory
    3. Make a file in current directory
    4. Remove a folder in current directory
    5. Close a port
"""
))

def make_dir():
    name = str(input("Please specify the name of your directory: "))
    try:
        os.system(f"mkdir {name}")
        return f"The directory {name} created successfully!"
    except Exception as e:
        return f"An error occurred: {e}"

def remove_dir():
    name = str(input("Please specify the name of the directory you want to delete: "))
    try:
        os.system(f"rmdir {name}")
        return f"The directory {name} deleted successfully!"
    except Exception as e:
        return f"An error occurred: {e}"


def make_file():
    name = str(input("Please specify the name of your file: "))
    try:
        os.system(f"touch {name}")
        return f"The file {name} created successfully!"
    except Exception as e:
        return f"An error occurred: {e}"

def remove_file():
    name = str(input("Please specify the name of the file you want to delete: "))
    try:
        os.system(f"rm {name}")
        return f"The file {name} deleted successfully!"
    except Exception as e:
        return f"An error occurred: {e}"

def close_port():
    port = int(input("Please enter a port you want to close: "))
    try:
        os.system(f"sudo kill -9 $(sudo lsof -t -i:{port})")
        return f"The port {port} is closed successfully!"
    except Exception as e:
        return f"An error occurred: {e}"

if action == 1:
    print(make_dir())
elif action == 2:
    print(remove_dir())
elif action == 3:
    print(make_file())
elif action == 4:
    print(remove_file())
elif action == 5:
    print(close_port())
else:
    print(f"Please choose an option between 1 and 5")
