import subprocess
from subprocess import run

from time import sleep as delay
from os import path





def trial():
    
    txt_file = "/Users/diegoibarra/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/Documents.txt"

    if not path.isfile(txt_file):
        run(["zshTestDialog"])
        

    process_return = run(['cat', txt_file], capture_output=True, text=True)
    stdout_raw = (process_return.stdout).splitlines()
    print(stdout_raw)

    """
    chrome_list = []
    safari_list = []
    for _url in stdout_raw:
        if _url == '':
            continue
        new_url = _url.split("//")
        if new_url[1].startswith("best"):
            safari_list.append(_url)
        else:
            chrome_list.append(_url)

    
    for safari_url in safari_list:
        print(safari_url)
        # run(["open", "-a", "Safari", safari_url])

    for chrome_url in chrome_list:
        print(chrome_url)
        # delay(2)
        # run(["open", "-a", "Google Chrome", chrome_url])
    """




"""
def main():

    # path.append()

    txt_file = "/Users/diegoibarra/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/Documents.txt"

    if not path.isfile(txt_file):
        run(["zshTestDialog"])
        exit_script()

    # process_return = run(['pyenv', 'which', 'python'], capture_output=True, text=True)
    # stdout_raw = (process_return.stdout).strip()
    # print(stdout_raw)

    # run(["zshTestDialog", stdout_raw])
    

    # exit_script()

    # run(["zshTestDialog"])

    # url_text = open_file(txt_file, "r+")
    # url_text = builtins.open(txt_file, "r+")
    # print(url_text)
    # individual_url = (url_text.read()).splitlines()
    # url_text.close()

    # with open_file(txt_file, "r+") as url_text:
    with builtins.open(txt_file, "r+") as url_text:
         individual_url = (url_text.read()).splitlines()
         print(individual_url[1])


    chrome_list = []
    safari_list = []
    for _url in individual_url:
        if _url == '':
            continue
        new_url = _url.split("//")
        if new_url[1].startswith("best"):
            safari_list.append(_url)
        else:
            chrome_list.append(_url)

    for safari_url in safari_list:
        run(["open", "-a", "Safari", safari_url])

    for chrome_url in chrome_list:
        delay(2)
        run(["open", "-a", "Google Chrome", chrome_url])
"""



if __name__ == '__main__':
    trial()