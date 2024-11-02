# RENAME FILES
import os

def rename_files():
    # Get the current directory
    current_directory = os.getcwd()
    
    # Loop through all files in the current directory
    for filename in os.listdir(current_directory):
        # Check if the file has a .txt extension
        if filename.endswith('.txt'):
            # Construct the new filename
            new_filename = f"{filename[:-4]}_backup.txt"
            
            # Rename the file
            os.rename(os.path.join(current_directory, filename), os.path.join(current_directory, new_filename))
    
    print("Files have been renamed.")

if __name__ == "__main__":
    rename_files()

# RENAME FILES WHILE ALSO CHECKING TO SEE IF NEW FILE NAME ALREADY EXISTS
import os

def rename_files():
    # Get the current directory
    current_directory = os.getcwd()
    
    # Loop through all files in the current directory
    for filename in os.listdir(current_directory):
        # Check if the file has a .txt extension
        if filename.endswith('.txt'):
            # Construct the new filename
            new_filename = f"{filename[:-4]}_backup.txt"
            
            # Check if the new filename already exists
            if not os.path.exists(os.path.join(current_directory, new_filename)):
                # Rename the file
                os.rename(os.path.join(current_directory, filename), os.path.join(current_directory, new_filename))
            else:
                print(f"File {new_filename} already exists. Skipping rename.")
    
    print("Files have been renamed.")

if __name__ == "__main__":
    rename_files()