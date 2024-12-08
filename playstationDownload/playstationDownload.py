#!/usr/local/bin/python

# /Library/Frameworks/Python.framework/Versions/3.12/bin/pip3

from subprocess import run, Popen, PIPE
from time import sleep
from os import path, chdir, get_terminal_size, listdir
import pandas as pd
from collections import defaultdict


def main():
    
    # SETUP MAIN VARIABLES
    SCRIPTDIR = path.dirname(__file__)
    CSV_NAME = "game_list.csv"
    GAMELIST_CSV = path.join(SCRIPTDIR, CSV_NAME)
    USERAGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Safari/605.1.15"
    downloaded_files = []
    skipped_files = []
    
    print('\x1b[2J', end="")
    print('\x1b[H', end="")
    

    # OPEN CSV FILE
    csv_file = pd.read_csv(GAMELIST_CSV, header=None)
    games_list = getGameList(csv_file)

    # ITERATE THROUGH EACH GAME
    for _game in games_list:
        _continue = True
        newdirpath = path.join(BASEDIR, _game['GameName'])
        
        if path.exists(newdirpath):
            _continue = False
            # IF GAME DIRECTORY ALREADY EXISTS AND IS NOT EMPTY, SKIPS CURRENT GAME
            files = len([_file for _file in listdir(newdirpath) if not _file.startswith('.')])
            if files == 0:
                _continue = True
                run(['rm', '-r', newdirpath])
                sleep(0.5)
            else:
                skipped_files.append([_game['GameName'], newdirpath])
                print(f'ALREADY EXISTS:  \'{_game['GameName']}\' Directory\n')

        if _continue:
            #  MAKES NEW DIRECTORY FOR CURRENT GAME
            run(['mkdir', newdirpath])
            sleep(1)

            # CHANGES CWD TO NEW DIRECTORY SO THAT FILES SAVE IN THAT DIRECTORY
            chdir(newdirpath)

            if _game['Type'] == "PKG":
                # RUN WGET TWICE
                # FIRST FOR RAP FILE
                # SECOND FOR PKG FILE
                for _part in range(2):
                    if _part == 0:
                        print('\x1b[2J', end="")
                        print('\x1b[H', end="")
                        print(f"Working on {_game['GameName'].upper()}...")
                        print('-'*terminal_size.columns)
                        print("Downloading RAP File...\n")
                        file_name = f"{_game['RapName']}.rap"
                        wget_output = wgetCmd(file_name, _game['RapLink'], USERAGENT)
                        checkWgetExitStatus(wget_output, _game, "rap", file_name, downloaded_files, skipped_files)
                    elif _part == 1:
                        print('\x1b[2J', end="")
                        print('\x1b[H', end="")
                        print(f"Working on {_game['GameName'].upper()}...")
                        print('-'*terminal_size.columns)
                        print("Downloading PKG File...\n")
                        file_name = f"{_game['GameName']}.pkg"
                        wget_output = wgetCmd(file_name, _game['MainLink'], USERAGENT)
                        checkWgetExitStatus(wget_output, _game, "pkg", file_name, downloaded_files, skipped_files)
                print()
            elif _game['Type'] == "ISO":
                # RUN WGET ONCE
                print('\x1b[2J', end="")
                print('\x1b[H', end="")
                print(f"Working on {_game['GameName'].upper()}...")
                print('-'*terminal_size.columns)
                print("Downloading ISO File...\n")
                file_name = f"{_game['GameName']}.zip"
                wget_output = wgetCmd(file_name, _game['MainLink'], USERAGENT)
                checkWgetExitStatus(wget_output, _game, "iso", file_name, downloaded_files, skipped_files)
                
    programEnd(downloaded_files, skipped_files)
    # DEBUG(DEBUGDELETEDIRECTORIES)
# ##############################################################################################
# ##############################################################################################


def programEnd(success_list: list, skip_list: list):
    print('\x1b[2J', end="")
    print('\x1b[H', end="")
    if len(success_list) != 0:
        print("\nFILES COMPLETED:")
        for _item in success_list:
            print(f"{_item[1].upper()}: {_item[0]:>30}")
    if len(skip_list) != 0:
        print("\nFILES SKIPPED:")
        for _item in skip_list:
            print(f"{_item[1].upper()}: {_item[0]:>30}")


def checkWgetExitStatus(wget_exitcode: tuple, game_info: dict, file_type: str, file_name: str, downloaded_list: list, skipped_list: list):
    # types: pkg, rap, iso
    if wget_exitcode[0] == 0:
        list_entry = (game_info['GameName'], file_type)
        downloaded_list.append(list_entry)
    else:
        list_entry = (game_info['GameName'], file_type)
        skipped_list.append(list_entry)
        logFile(game_info, file_type, wget_exitcode[1])
        file_path = path.join(BASEDIR, game_info['GameName'], file_name)
        run(['rm', file_path])


def logFile(game_info: dict, _type: str, msg: str):
    process = run(["date"], capture_output=True, text=True)
    _time = process.stdout
    logfile_path = path.join(BASEDIR, "wgetlog.log")
    if not path.exists(logfile_path):
        run(['touch', logfile_path])
        sleep(0.5)
    with open(logfile_path, 'a') as logopen:
        logopen.writelines([
            f"{_time}"
            f"Game: {game_info['GameName'].upper():>20}\n",
            f"Type: {_type.upper():>20}\n",
            f"WGET Output:\n{msg}\n\n"
        ])


def getGameList(_file: pd.DataFrame) -> tuple[int, str]:
    """
    Summary:
        Iterates through CSV File where each line is a seperate game
        Rows with 4 values are PKG / RAP links
        Rows with 2 values are ISO links
        From each game, a Dict is created with all variables needed to download
        Each game is appended to the masterlist which is the return value of this method

    Parameters:
        _file: CSV File with Game Info and Links. Order of items is GameName, RapName, RapLink, MainLink, Type

    Return:
        List of Game Dict containing the keys 'GameName', 'RapName', 'RapLink', 'MainLink', 'Type'
    """
    games_list = []

    for _row in range(len(_file.index)):
        _keys = ['GameName', 'RapName', 'RapLink', 'MainLink', 'Type']
        game_dict = defaultdict(str)

        if _file.isnull().iloc[_row].any() or len(_file.columns) == 2:
            # CHECKS TO SEE IF ROW HAS LESS THAN 4 ENTRIES (IF OTHER ROWS HAVE FOUR ENTRIES)
            # OR CHECKS TO SEE IF THERE ARE ONLY 2 COLUMNS
            # TWO COLUMNS IS THE ENTRY FOR AN ISO FILE
            game_dict[_keys[0]] = _file.loc[_row, 0].strip()  # GameName
            game_dict[_keys[3]] = _file.loc[_row, 1].strip()  # MainLink
            game_dict[_keys[4]] = "ISO"                      # Type
        else:
            # ROW HAS 4 ENTRIES, THEREFORE IT IS A PKG/RAP COMBO
            game_dict[_keys[0]] = _file.loc[_row, 0].strip()  # GameName
            game_dict[_keys[1]] = _file.loc[_row, 1].strip()  # RapName
            game_dict[_keys[2]] = _file.loc[_row, 2].strip()  # RapLink
            game_dict[_keys[3]] = _file.loc[_row, 3].strip()  # MainLink
            game_dict[_keys[4]] = "PKG"                      # Type
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
    # process = run(['wget', '--max-redirect=1', '-O', new_file_name, '-U', user_agent, url_link], capture_output=True, text=True)
    # wget_output = (process.stderr).strip()
    # print(wget_output)
    # exitcode = process.returncode
    # return (exitcode, wget_output)
    stdout=""
    process = Popen(['wget', '--progress=bar:force:noscroll', '--max-redirect=1', '-O', new_file_name, '-U', user_agent, url_link], stderr=PIPE, text=True)
    print('\x1b[?25l', end="")
    print('\x1b[1m', end="")
    print('\x1b[38;5;0m', end="")
    print('\x1b[48;5;249m', end="")
    for _line in process.stderr:
        if "%" in _line:
            _chars = len(_line.strip())
            extra_space = terminal_size.columns - _chars
            _filler = " "*extra_space
            print(f"\r{_line.strip()}{_filler}", end="")
            sleep(1)
        else:
            stdout+=_line
    exitcode = process.wait()
    print('\x1b[0m', end="")
    print('\x1b[?25h', end="")
    return (exitcode, stdout)


if __name__ == "__main__":
    BASEDIR = "/Users/diegoibarra/Local/PlayStation/Games/PS3 Games Pkg"
    terminal_size = get_terminal_size()
    main()
