import sys
from deep_translator import GoogleTranslator

def translate_file(filepath):
    try:
        # Open and read the file with UTF-8 encoding for Russian characters
        with open(filepath, 'r', encoding='utf-8') as f:
            russian_text = f.read()
        
        if not russian_text.strip():
            print("The file is empty.")
            return

        # Translate the entire block of text
        translated = GoogleTranslator(source='auto', target='en').translate(russian_text)
        
        print(f"\n--- Translation of {filepath} ---")
        print(translated)
        print("---------------------------------")

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if a filename was provided as a command-line argument
    if len(sys.argv) > 1:
        translate_file(sys.argv[1])
    else:
        print("Usage: python3 translate_file.py <path_to_russian_file.txt>")
