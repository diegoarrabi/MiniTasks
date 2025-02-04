import os

season_number = 3
folder_path = f"I.Think.You.Should.Leave.with.Tim.Robinson.S03.1080p.NF.WEBRip.DDP5.1.Atmos.x264-WDYM[rartv]"
folder_rename = f"Season {season_number}"

file_name = "I.Think.You.Should.Leave.with.Tim.Robinson.S03E01.THAT.WAS.THE.EARTH.TELLING.ME.IM.SUPPOSED.TO.DO.SOMETHING.GREAT.1080p.NF.WEB-DL.DDP5.1.Atmos.H.264-WDYM"
change_one = [f"i.think.you.should.leave.with.tim.robinson.s01e", "I Think You Should Leave - S01E"]
change_two = [".720p.web.x264-wayne", ""]
change_three = ["I Think You Should Leave - ", ""]
change_once = ["", ""]


base_path = os.path.dirname(folder_path)


new_directory = os.path.join(base_path, folder_rename)
# os.rename(folder_path, new_directory)

all_items = os.listdir(new_directory)

for i in all_items:
    old_file = os.path.join(new_directory, i)

    name_change = i.replace(change_one[0], change_one[1])
    name_change = name_change.replace(change_two[0], change_two[1])
    name_change = name_change.replace(change_three[0], change_three[1])

    period_count = name_change.count(".")
    name_change = name_change.replace(".", " ", period_count-1)
    new_name = name_change.replace(change_once[0], change_once[1], 1)

    new_file = os.path.join(new_directory, new_name)

    os.rename(old_file, new_file)
