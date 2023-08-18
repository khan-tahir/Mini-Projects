from googletrans import Translator
translator = Translator()
inputword = input("Enter text for Translation : ")
lang = input("Enter the language you wanted to translate : ")
output = translator.translate(inputword, dest=lang)
print(output.text)