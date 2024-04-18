from deep_translator  import GoogleTranslator
import os
import time

class TranslatorApp:
    def __init__(self):
        """Initialize the TranslatorApp object."""
        self.translator = GoogleTranslator()
        self.language_dict = self.translator.get_supported_languages(as_dict=True).items()
        self.sourceLang = ""
        self.destinationLang = ""
        self.transText = ""

    def main_menu(self):
        """Display the main menu and handle user input."""
        self.cls()
        self.print_header()
        self.checkinput()

    def cls(self):
        """Clear the screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def checkinput(self):
        """Check user input and perform corresponding actions."""
        userInput = input("Enter your choice: ")

        match userInput:
            case "1":
                self.listLanguages()
            case "2":
                self.set_language("source")
            case "3":
                self.set_language("destination")
            case "4":
                self.translate()
            case "5":
                exit()
            case _:
                self.main_menu()

    def listLanguages(self):
        """List available languages."""
        self.cls()
        print("Available languages:")
        for language, abbreviation in self.language_dict:
            print(f"{abbreviation}: {language}")
        print()
        input("Press Enter to continue...")
        self.main_menu()

    def find_language_name(self, language_code):
        """Find the language name from its code."""
        for language, abbreviation in self.language_dict:
            if abbreviation == language_code:
                return language
        return "Not set"

    def set_language(self, lang_type):
        """Set the source or destination language."""
        self.cls()
        lang_type_str = "source" if lang_type == "source" else "destination"
        lang_code_input = input(f"Enter {lang_type_str} language code (e.g.: en, fr, es, de, ...): ")

        match_found = False
        for lang, code in self.language_dict:
            if code.lower() == lang_code_input.lower():
                match_found = True
                setattr(self, lang_type_str + "Lang", lang_code_input)
                break

        if not match_found:
            print("No language code found!\n")
            choice = input("Press 1 to retry or 2 to exit to main: ")
            if choice == "1":
                self.set_language(lang_type)
            elif choice == "2":
                self.main_menu()

        self.main_menu()

    def translate(self):
        """Translate text from source to destination language."""
        if not self.sourceLang or not self.destinationLang:
            self.cls()
            print("You have to set source and destination Language first!")
            input("Press any key to continue...")
            self.main_menu()

        self.cls()
        print("Enter the text to translate:")
        transText = input()
        sourceLang = self.sourceLang
        destinationLang = self.destinationLang

        try:
            result = self.translator.translate(text=transText, ssource=sourceLang, target=destinationLang)
            print("\nTranslated text:")
            print(result)
        except Exception as e:
            print("\nAn error occurred during translation:", e)

        time.sleep(5)
        print("\nPress any key to continue...")
        input()  # Wait for user input
        self.main_menu()

    def print_header(self):
        """Print the header with menu options and current language settings."""
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
            f"       Current Destination Language: {self.find_language_name(self.destinationLang)}",
            "------------------------------------------------------"
        ]

        # Print the header with right-aligned '#'
        for line in header_text:
            print(line)

def main():
    app = TranslatorApp()
    app.main_menu()


if __name__ == '__main__':
    main()