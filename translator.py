from translate import Translator
from colorama import Fore,init

print("Welcome to Translator\n")
user = input(Fore.YELLOW+" [ * ] "+Fore.WHITE+"Enter text for translating : ")

options = Translator(from_lang='en', to_lang='persian')
translate = options.translate(user)

print(Fore.YELLOW+'----------'+Fore.WHITE+' Translate '+Fore.YELLOW+'----------')

print(translate)