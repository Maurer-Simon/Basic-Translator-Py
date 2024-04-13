from deep_translator  import GoogleTranslator
import os
import time

class TranslatorApp:
    def __init__(self):
        GoogleTranslator()
        self.language_dict = GoogleTranslator().get_supported_languages(as_dict=True).items()
        self.sourceLang = ""
        self.desLang = ""
        self.transText = ""

    def main_menu(self):
        self.cls()
        self.print_header()
        self.checkinput()

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def checkinput(self):
        userInput = input("Enter your choice: ")

        if userInput == "1":
            self.listLanguages()
        elif userInput == "2":
            self.setSourceLang()
        elif userInput == "3":
            self.setDesLang()
        elif userInput == "4":
            self.translate()
        elif userInput == "5":
            exit()
        else:
            self.main_menu()

    def listLanguages(self):
        self.cls()
        print("Available languages:")
        for language, abbreviation in self.language_dict:
            print(f"{abbreviation}: {language}")
        print()
        print("Press any key to continue...")
        input()  # Wait for user input
        self.main_menu()

    def find_language_name(self, language_code):
        for language, abbreviation in self.language_dict:
            if abbreviation == language_code:
                return language
        return "Not set"

    def setSourceLang(self):
        self.cls()
        print("Enter source language code (e.g.: en, fr, es, de, ...):")
        sourceLang = input()

        matchFound = False
        for code, lang in self.language_dict:
            if code == sourceLang or lang == sourceLang or lang.lower() == sourceLang.lower():
                matchFound = True
                self.sourceLang = sourceLang
                break

        if not matchFound:
            print("No language code found!\n")
            choice = 0
            while choice != "1" and choice != "2":
                choice = input("Press 1 to retry or 2 to exit to main!\n")

            if choice == "1":
                self.setSourceLang()
            elif choice == "2":
                self.main_menu()

        self.main_menu()

    def setDesLang(self):
        self.cls()
        print("Enter destination language code (e.g., en, fr, es):")
        desLang = input()

        matchFound = False
        for code, lang in self.language_dict:
            if code == desLang or lang == desLang or lang.lower() == desLang.lower():
                matchFound = True
                self.desLang = desLang
                break

        if not matchFound:
            print("No language code found!\n")
            choice = 0
            while choice != "1" and choice != "2":
                choice = input("Press 1 to retry or 2 to exit to main!\n")

            if choice == "1":
                self.setDesLang()
            elif choice == "2":
                self.main_menu()

        self.main_menu()

    def translate(self):
        if self.sourceLang == "" or self.desLang == "":
            self.cls()
            print("You have to set source and destination Language first!")
            print("Press any key to continue...")
            input()  # Wait for user input
            self.main_menu()

        self.cls()
        print("Enter the text to translate:")
        transText = input()
        sourceLang = self.sourceLang
        desLang = self.desLang

        try:
            result = GoogleTranslator(source=sourceLang, target=desLang).translate(text=transText)
            print()
            print("Translated text:")
            print(result)
        except Exception as e:
            print("\nAn error occurred during translation:", e)

        time.sleep(5)
        print("\nPress any key to continue...")
        input()  # Wait for user input
        self.main_menu()

    def print_header(self):
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
            f"       Current Source Language: {self.find_language_name(self.sourceLang)}",
            f"       Current Destination Language: {self.find_language_name(self.desLang)}",
            "------------------------------------------------------"
        ]

        # Find the maximum length of the text lines
        max_length = len(header_text[1])  # Using the length of the template line for alignment

        # Print the header with right-aligned '#'
        for line in header_text:
            print(line)




def main():
    app = TranslatorApp()
    app.main_menu()


if __name__ == '__main__':
    main()