import sys
from stats import get_book_text, count_words_from_text, count_chars_from_text

def main():
    text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt..\n--------- Word Count ----------")
    print (f"Found {count_words_from_text(text)} total words\n--------- Character Count -------") 
    count_chars_from_text(text)
    return

if len(sys.argv) !=2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()
