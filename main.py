from googletrans import Translator, LANGUAGES
import os
import time

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def checkinput(userInput, translator, sourceLang, desLang, transText):
    if userInput == "1":
        listLanguages(translator, sourceLang, desLang, transText)
    elif userInput == "2":
        setSourceLang(translator, desLang, transText)
    elif userInput == "3":
        setDesLang(translator, sourceLang, transText)
    elif userInput == "4":
        translate(translator, sourceLang, desLang)
    elif userInput == "5":
        exit()
    else:
        main(translator, sourceLang, desLang, transText)

def listLanguages(translator, sourceLang, desLang, transText):
    cls()
    print("Available languages:")
    for code, language in LANGUAGES.items():
        print(f"{code}: {language}")
    print()
    print("Press any key to continue...")
    input()  # Wait for user input
    main(translator, sourceLang, desLang, transText)

def setSourceLang(translator, desLang, transText):
    cls()
    print("Enter source language code (e.g.: en, fr, es, de, ...):")
    sourceLang = input()

    matchFound = False
    for code, lang in LANGUAGES.items():
        if code == sourceLang:
            matchFound = True
            break

    if not matchFound:
        print("No language code found!\n")
        choice = 0
        while choice != "1" and choice != "2":
            choice = input("Press 1 to retry or 2 to exit to main!\n")

        if choice == "1":
            setSourceLang(translator, sourceLang, transText)
        elif choice == "2":
            main(translator, sourceLang, desLang, transText)

    main(translator, sourceLang, desLang, transText)

def setDesLang(translator, sourceLang, transText):
    cls()
    print("Enter destination language code (e.g., en, fr, es):")
    desLang = input()

    matchFound = False
    for code, lang in LANGUAGES.items():
        if code == desLang:
            matchFound = True
            break

    if not matchFound:
        print("No language code found!\n")
        choice = 0
        while choice != "1" and choice != "2":
            choice = input("Press 1 to retry or 2 to exit to main!\n")

        if choice == "1":
            setDesLang(translator, sourceLang, transText)
        elif choice == "2":
            main(translator, sourceLang, desLang, transText)

    main(translator, sourceLang, desLang, transText)

def translate(translator, sourceLang, desLang):
    if sourceLang == "" or desLang == "":
        cls()
        print("You have to set source and destination Language first!")
        print("Press any key to continue...")
        input()  # Wait for user input
        main(translator, sourceLang, desLang)
    cls()
    print("Enter the text to translate:")
    transText = input()
    result = translator.translate(transText, src=sourceLang, dest=desLang)
    print()
    print("Translated text:")
    print(result.text)
    time.sleep(5)
    print("\nPress any key to continue...")
    input()  # Wait for user input
    main(translator, sourceLang, desLang, transText)

def print_header(sourceLang, desLang):
    header_text = [
        "------------------------------------------------------",
        "       Welcome to this simple translator API.",
        "       Following options are available:",
        "       1. To list available languages.",
        "       2. To define source language.",
        "       3. To define destination language.",
        "       4. To start translating.",
        "       5. To exit.",
        "",
        f"       Current SourceLang: {sourceLang}",
        f"       Current DestinationLang: {desLang}",
        "------------------------------------------------------"
    ]

    # Find the maximum length of the text lines
    max_length = len(header_text[1])  # Using the length of the template line for alignment

    # Print the header with right-aligned '#'
    for line in header_text:
        print(line)

def main(translator=None, sourceLang="", desLang="", transText=""):
    cls()
    if translator is None:
        translator = Translator()

    print_header(sourceLang, desLang)

    userInput = input("Enter your choice: ")
    checkinput(userInput, translator, sourceLang, desLang, transText)

if __name__ == '__main__':
    main()