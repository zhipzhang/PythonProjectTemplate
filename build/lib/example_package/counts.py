from collections import Counter
from string import punctuation

def load_text(file_path):
    """Load text from a file."""
    with open(file_path, 'r') as file:
        return file.read()

def clean_text(text):
    """Clean the text by removing punctuation and converting to lowercase."""
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, '')
    return text

def count_words(input_file):
    """Count the frequency of each word in the input file."""
    text = load_text(input_file)
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    word_count = Counter(words)
    return word_count