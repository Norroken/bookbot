def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    #sorted_chartacter = character_sort()
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print_alphabet(text)
    print("--- End report ---")

# Count number of words in text provided
def get_num_words(text):
    words = text.split()
    return len(words)


#Counts the number of characters in the text provided
def get_num_characters(text):
    alphabet = dict()
    lowered_text = text.lower()
    for letter in lowered_text:
        alphabet[letter] = alphabet.get(letter, 0) + 1
     
    return alphabet   


def sort_on(dict):
    return dict["num"]

def character_sort(text):
    sorted_alpha = []
    num_characters = get_num_characters(text)
    for char, count in num_characters.items():
        if char.isalpha():
            letter_data = {"char": char, "num": count}
            sorted_alpha.append(letter_data)
    
    sorted_alpha.sort(reverse=True, key=sort_on)
    return sorted_alpha
           
           
def print_alphabet(text):
    sorted_alpha = character_sort(text)
    for items in sorted_alpha:
        print(f"The '{items['char']}' character was found {items['num']} times")

         
    
# reads the book in to a string
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
