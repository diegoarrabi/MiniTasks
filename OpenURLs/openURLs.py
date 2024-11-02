import subprocess
from subprocess import run
from builtins import open as open_file

from time import sleep as delay
from os import path
import sys

def main():
    
    txt_file = "/Users/diegoibarra/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/URL_Links.txt"

    if not path.isfile(txt_file):
        run(["zshTestDialog", "File does not Exist"])
    
    with open_file(txt_file, "r+") as url_text:
         individual_url = (url_text.read()).splitlines()
         url_text.truncate(0) 
    
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
        run(["open", "-a", "Google Chrome", chrome_url])
        delay(4)
    
    run(["zshTestDialog", "DONE"])
    


if __name__ == '__main__':
    main()