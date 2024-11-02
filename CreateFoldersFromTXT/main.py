from sys import exit
from os import path, listdir, getcwd, mkdir

def main():

    def getFile(directory):
        for item in directory:
            item_suffix = item.split(".")
            if len(item_suffix) < 2:
                pass
            else:
                if item_suffix[1].lower() == "txt":
                    return item
        exit(print("No '.txt' file found"))

    def openFile(working_directory, file_name):
        file_path = path.join(working_directory, file_name)
        my_file = open(file_path, "r+")
        my_file_contents = my_file.readlines()
        my_file.close()
        if len(my_file_contents) == 0:
            exit(print("Text File is empty"))
        for i, text_line in enumerate(my_file_contents):
            my_file_contents[i] = text_line.rstrip()
            my_file_contents[i] = my_file_contents[i].replace("/", "-")
            my_file_contents[i] = my_file_contents[i].replace(".", "_")
        return my_file_contents

    pwd = getcwd()
    items_in_dir = listdir(pwd)
    file_name = getFile(items_in_dir)
    file_contents = openFile(working_directory=pwd, file_name=file_name)
    for i, title in enumerate(file_contents):
        i = i + 1
        if len(file_contents) > 9 and i < 10:
            file_string = f"0{i}_{title}"
        else:
            file_string = f"{i}_{title}"          
        mkdir(file_string)
        
if __name__ == '__main__':
    main()
