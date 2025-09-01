import csv
import os

# Define the dictionary file name
DICTIONARY_FILE = 'dictionary.csv'

def load_dictionary():
    """Loads the dictionary from the CSV file into memory."""
    eng_to_aliench = {}
    aliench_to_eng = {}
    if not os.path.exists(DICTIONARY_FILE):
        # Create the file if it doesn't exist to avoid errors
        open(DICTIONARY_FILE, 'w').close() 
    
    with open(DICTIONARY_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                eng, aliench = row
                eng_to_aliench[eng.strip()] = aliench.strip()
                aliench_to_eng[aliench.strip()] = eng.strip()
    return eng_to_aliench, aliench_to_eng

def add_word():
    """Adds a new word and its translation to the dictionary."""
    print("\n--- Add a New Word ---")
    english_word = input("Enter the English word: ").strip().lower()
    aliench_word = input(f"Enter the Aliench translation for '{english_word}': ").strip().lower()
    
    with open(DICTIONARY_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([english_word, aliench_word])
        
    print(f"✅ Success! Added '{english_word}' -> '{aliench_word}' to the dictionary.")

def translate_file(input_file_path, output_file_path, direction):
    """Translates a text file from a source language to a target language."""
    eng_to_aliench, aliench_to_eng = load_dictionary()
    
    # Choose the correct dictionary for the translation direction
    if direction == 'eng_to_aliench':
        dictionary = eng_to_aliench
        print("Translating from English to Aliench...")
    else:
        dictionary = aliench_to_eng
        print("Translating from Aliench to English...")
        
    try:
        with open(input_file_path, 'r', encoding='utf-8') as infile, \
             open(output_file_path, 'w', encoding='utf-8') as outfile:
            
            for line in infile:
                words = line.strip().split()
                translated_words = [dictionary.get(word.lower(), f"<{word}?>") for word in words]
                outfile.write(' '.join(translated_words) + '\n')
                
        print(f"✔️ Translation complete! Output saved to '{output_file_path}'")
    except FileNotFoundError:
        print(f"❌ Error: The input file '{input_file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        print("\n===== 👽 Alien-Human Interpreter 🧑‍💻 =====")
        print("1. Translate English to Aliench")
        print("2. Translate Aliench to English")
        print("3. Add a new word to the dictionary")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1' or choice == '2':
            input_file = input("Enter the name of the input text file (e.g., input.txt): ")
            output_file = input("Enter the name for the output translated file (e.g., output.txt): ")
            direction = 'eng_to_aliench' if choice == '1' else 'aliench_to_eng'
            translate_file(input_file, output_file, direction)
        elif choice == '3':
            add_word()
        elif choice == '4':
            print("Goodbye! Yalla!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()