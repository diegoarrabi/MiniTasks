import shutil
from os import path
from os import listdir
import tkinter as tk
from tkinter import filedialog


def namePad(item_count):
    if item_count < 10:
        pad = 2
    elif item_count < 100:
        pad = 3
    elif item_count < 1000:
        pad = 4
    return pad


def renameFiles(directory):
    image_ext = ['.jpg', '.jpeg', '.png', '.webp']
    videos_ext = ['.mp4', '.mov', '.m4v']

    basename = path.basename(directory)
    parent_dir = path.dirname(directory)
    filename = basename.replace(" ", "_")

    contents_list = sorted(
        [path.join(directory, file) for file in listdir(directory) if (not file.startswith(".") and path.isfile(path.join(directory, file)))],
        key=lambda f: path.getsize(path.join(directory, f))
    )

    pad = namePad(len(contents_list))

    image_count = 1
    video_count = 1

    for oldfile in contents_list:
        _, file_ext = path.splitext(oldfile)
        file_ext = file_ext.lower()
        if file_ext in image_ext:
            new_file_name = f"{image_count:0>{pad}}_{filename}{file_ext}"
            image_count += 1
        elif file_ext in videos_ext:
            new_file_name = f"{video_count:0>{pad}}_{filename}{file_ext}"
            video_count += 1
        newfile_path = path.join(directory, new_file_name)
        if path.exists(newfile_path):
            continue
        shutil.move(src=oldfile, dst=newfile_path)


def main():
    home_user = path.join(path.expanduser("~"), "local", "temp", "organized")
    app = tk.Tk()
    app.withdraw()

    directory = filedialog.askdirectory(
        title="Select Folder with contents to rename...",
        initialdir=home_user,
    )
    if not directory:
        exit()
    
    # for directory in listdir[]:


    renameFiles(directory)

    return


# def extensions():
#     ext_list = []
#     directory = "/Users/diegoibarra/Local/temp/organized/1. fav"
#     subdirs = [path.join(directory, subdir) for subdir in os.listdir(directory) if not subdir.startswith(".")]
#     for sub_directory in subdirs:
#         files = [file for file in os.listdir(sub_directory) if (not file.startswith(".") and path.isfile(path.join(sub_directory, file)))]

#         for file in files:
#             _, file_extension = path.splitext(file)
#             file_extension = file_extension.replace('.', '').lower()
#             if not file_extension in ext_list:
#                 ext_list.append(file_extension)

#     print(ext_list)
#     return


if __name__ == "__main__":
    main()
