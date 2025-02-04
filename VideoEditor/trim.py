import os
from moviepy import *
from moviepy.video.io.VideoFileClip import VideoFileClip


folder_name = "/Users/diegoibarra/Downloads/Adventure Time S05/Original"
edit_folder_name = "/Users/diegoibarra/Downloads/Adventure Time S05/Edit"

all_items = os.listdir(folder_name)

for i in all_items:
    full_old_file = os.path.join(folder_name, i)
    full_new_file = os.path.join(edit_folder_name, i)
    
    

    original_clip = VideoFileClip(full_old_file)

    _starttime = 25
    _endtime = original_clip.duration - 29

    no_intro = original_clip.subclipped(start_time=_starttime, end_time=_endtime)

    no_intro.write_videofile(full_new_file)

    
    
    