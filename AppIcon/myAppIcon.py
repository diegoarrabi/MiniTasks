#!/Users/diegoibarra/.config/pyenv/versions/3.12.1/envs/AppIcon/bin/python

import pandas as pd
import shutil
from subprocess import call

app_icon_data = pd.read_csv("data.csv")

for count, app_name in enumerate(app_icon_data['App_Name']):
    print(f'{app_name} Icon Changed')
    stock_icon_path = str(app_icon_data['Icon_Path'][count])
    new_icon_path = str(app_icon_data['New_Icon_Path'][count])
    shutil.copyfile(src= new_icon_path, dst=stock_icon_path)

# call(["killall", "Dock"])
