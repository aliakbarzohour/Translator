from translate import Translator

user = input(" [ ~ ] Enter text for translating : ")

options = Translator(from_lang='en', to_lang='persian')
translate = options.translate(user)

print(translate)