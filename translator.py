# import librarys
from translate import Translator
from colorama import Fore,init
import subprocess
# start 
print("Welcome to Translator\n")
# define content
user = input(Fore.YELLOW+" [ * ] "+Fore.WHITE+"Enter text for translating : ")
# changing languege 
options = Translator(from_lang='en', to_lang='persian')
translate = options.translate(user)
# baner for start translating
print(Fore.YELLOW+'----------'+Fore.WHITE+' Translate '+Fore.YELLOW+'----------')
# print result
print(translate)
# sending content of translate variable to .txt file 
echo = subprocess.getoutput(f"echo {translate} >> translate.txt")
