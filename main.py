import random
import threading

import requests
from bs4 import BeautifulSoup
from colorama import Fore,Style,init
import os
import json
import string
from threading import Thread
f = open("links.txt", "w")


init()

#                         .
#                        M
#                       dM
#                       MMr
#                      4MMML                  .
#                      MMMMM.                xf
#      .              "MMMMM               .MM-
#       Mh..          +MMMMMM            .MMMM
#       .MMM.         .MMMMML.          MMMMMh
#        )MMMh.        MMMMMM         MMMMMMM
#         3MMMMx.     'MMMMMMf      xnMMMMMM"
#         '*MMMMM      MMMMMM.     nMMMMMMP"
#           *MMMMMx    "MMMMM\    .MMMMMMM=
#            *MMMMMh   "MMMMM"   JMMMMMMP
#              MMMMMM   3MMMM.  dMMMMMM            .
#               MMMMMM  "MMMM  .MMMMM(        .nnMP"
#   =..          *MMMMx  MMM"  dMMMM"    .nnMMMMM*
#     "MMn...     'MMMMr 'MM   MMM"   .nMMMMMMM*"
#      "4MMMMnn..   *MMM  MM  MMP"  .dMMMMMMM""
#        ^MMMMMMMMx.  *ML "M .M*  .MMMMMM**"
#           *PMMMMMMhn. *x > M  .MMMM**""
#              ""**MMMMhx/.h/ .=*"
#                       .3P"%....
#                     nP"     "*MMnx

#               wiz ## ANONFILE BRUTEFORCE TOOL



class Main:
    def __init__(self):
        os.system('cls && title WIZZ')

        print(Fore.RED + f'''
                                    $$\      $$\ $$$$$$\ $$$$$$$$\ $$$$$$$$\ 
                                    $$ | $\  $$ |\_$$  _|\____$$  |\____$$  |
                                    $$ |$$$\ $$ |  $$ |      $$  /     $$  / 
                                    $$ $$ $$\$$ |  $$ |     $$  /     $$  /  
                                    $$$$  _$$$$ |  $$ |    $$  /     $$  /   
                                    $$$  / \$$$ |  $$ |   $$  /     $$  /    
                                    $$  /   \$$ |$$$$$$\ $$$$$$$$\ $$$$$$$$\ 
                                    \__/     \__|\______|\________|\________|
                                    
                                                wiz {Fore.WHITE}##{Fore.RED} ANONFILE BRUTEFORCE TOOL
''')

        while True:
            self.generate()

    def generate(self):
        length = 10
        all = string.ascii_lowercase + string.ascii_uppercase + string.digits
        temp = random.sample(all, length)

        self.link = "https://anonfiles.com/" + "".join(temp)

        self.resp = requests.get(self.link)
        self.soup = BeautifulSoup(self.resp.text, "html.parser")

        self.title = self.soup.select('h1')[0].text.strip()

        if self.resp.status_code == 200:
            print(f"{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {self.link} :: {self.title} {Fore.WHITE}:: {Fore.GREEN}VALID{Fore.RED}")
            f.write(self.link + "\n")
        else:
            print(f"{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {self.link} {Fore.WHITE}:: {Fore.RED}INVALID")


if __name__ == '__main__':
    Main()
