#!/usr/local/bin/python

# /Library/Frameworks/Python.framework/Versions/3.12/bin/pip3

from subprocess import run, Popen, PIPE
from time import sleep
from os import path, chdir
import pandas as pd
from collections import defaultdict


def main():
    
    # SETUP MAIN VARIABLES
    SCRIPTDIR = path.dirname(__file__)
    CSV_NAME = "game_list.csv"
    GAMELIST_CSV = path.join(SCRIPTDIR, CSV_NAME)
    BASEDIR = "/Users/diegoibarra/Local/PlayStation/Games/PS3 Games Pkg"
    USERAGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Safari/605.1.15"
    skipped_files = []
    downloaded_files = []
    

    # OPEN CSV FILE
    csv_file = pd.read_csv(GAMELIST_CSV, header=None)
    games_list = getGameList(csv_file)


    # ITERATE THROUGH EACH GAME
    for _game in games_list:
        
        newdirpath = path.join(BASEDIR, _game['GameName'])
        
        if path.exists(newdirpath):
            # IF GAME DIRECTORY ALREADY EXISTS, SKIPS CURRENT GAME
            print(f'ALREADY EXISTS:  \'{_game['GameName']}\' Directory\n')
            skipped_files.append([_game['GameName'], newdirpath])

        # TEMP TEMP
        # TEMP TEMP
        # TEMP TEMP
        
            run(['rm', '-r', newdirpath])
        # else:

        # TEMP TEMP
        # TEMP TEMP
        # TEMP TEMP
        
        
        #  MAKES NEW DIRECTORY FOR CURRENT GAME
        print(f"Working on {_game['GameName']}...")
        run(['mkdir', newdirpath]) ; sleep(1)
        
        # CHANGES CWD TO NEW DIRECTORY SO THAT FILES SAVE IN THAT DIRECTORY
        chdir(newdirpath)

        # RUN WGET TWICE
        # FIRST FOR RAP FILE
        # SECOND FOR PKG FILE
        for _part in range(2):
            if _part == 0:
                print("Downloading Rap File...")
                file_name = f"{_game['RapName']}.rap"
                wget_returncode = wgetCmd(file_name, _game['RapLink'], USERAGENT)
                
            elif _part == 1:
                print("Downloading Pkg File...")
                file_name = f"{_game['GameName']}.pkg"
                wget_returncode =wgetCmd(file_name, _game['PkgLink'], USERAGENT)
                
        print()


def getGameList(_file: pd.DataFrame) -> list[dict]:
    """
    Summary:
        Iterates through CSV File where each line is a seperate game with a PKG and RAP link
        From each game, a Dict is created with all variables needed to download
        Each game is appended to the masterlist which is the return value of this method
    
    Parameters:
        _file: CSV File with Game Info and Links. Order of items is GameName, RapName, RapLink, PkgLink

    Return:
        List of Game Dict containing the keys 'GameName', 'RapName', 'RapLink', 'PkgLink'
    """
    games_list = []
    
    for _row in range(len(_file.index)):
        _keys = ['GameName', 'RapName', 'RapLink', 'PkgLink']
        game_dict = defaultdict(str)
        game_dict[_keys[0]] = _file.loc[_row, 0].strip() # GameName
        game_dict[_keys[1]] = _file.loc[_row, 1].strip() # RapName
        game_dict[_keys[2]] = _file.loc[_row, 2].strip() # RapLink
        game_dict[_keys[3]] = _file.loc[_row, 3].strip() # PkgLink
        games_list.append(game_dict)
    return games_list


def wgetCmd(new_file_name: str, url_link: str, user_agent: str) -> int:
    """
    Summary:
        Runs wget command with verbose output

    Parameters:
        new_file_name: str = File name to be saved as including extension
        url_link: str = URL Link to download file
        user_agent: str = User Agent of browser
    
    Return:
        shell command return code
    """

    # wgetcommand = f'wget -O "{new_file_name}" -U "{user_agent}" "{url_link}"'
    
    process = run(['wget', '-O', new_file_name, '-U', user_agent, url_link], capture_output=True, text=True)
    stdout = (process.stdout).strip()
    stderr = (process.stderr).strip()
    stdreturn = process.returncode
    return (stdout, stderr, stdreturn)

    # process = Popen(
    #     wgetcommand,
    #     stdout = PIPE,
    #     stderr = PIPE,
    #     text = True,
    #     shell = True
    # )
    # stdout, stderr = process.communicate()
    # return (stdout, stderr)

if __name__ == "__main__":
    main()