import os

folder_name = "The.Legend.of.Korra.S02.1080p.BluRay.DDP.5.1.x265-EDGE2020"

text_replace_folder = ".1080p.BluRay.DDP.5.1.x265-EDGE2020"
text_replace_file = ".1080p.BluRay.DDP.5.1.H.265.-EDGE2020"


new_folder_name = folder_name.replace(text_replace_folder, "")
new_folder_name = new_folder_name.replace(".", " ")


downloads_directory = "/Users/diegoibarra/Downloads"


full_old_directory = os.path.join(downloads_directory, folder_name)
full_new_directory = os.path.join(downloads_directory, new_folder_name)

os.rename(full_old_directory, full_new_directory)

all_items = os.listdir(full_new_directory)

for i in all_items:
    full_old_file = os.path.join(full_new_directory, i)
    
    old_name = i.replace(text_replace_file, "")
    period_count = old_name.count(".")
    new_name = old_name.replace(".", " ", period_count-1)

    full_new_file = os.path.join(full_new_directory, new_name)

    os.rename(full_old_file, full_new_file)
    
    
    