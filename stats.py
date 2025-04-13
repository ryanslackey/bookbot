
from collections import defaultdict

def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def count_words_from_text(text):
    words = text.split()
    return len(words)

def count_chars_from_text(text):
    d = defaultdict(int)
    for char in text:
        if char.isalpha():
            d[char.lower()] += 1

    sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
    
    for char, count in sorted_items:
        print(f"{char}: {count}")

    return 

    
    










