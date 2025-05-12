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
    """Count the frequency of each word in the input file.

    Args:
        input_file (str): Path to the text file to analyze.

    Returns:
        Counter: A Counter object containing word frequencies where:
            - keys are the unique words found in the text
            - values are the number of occurrences of each word

    Example:
        >>> word_counts = count_words("sample.txt")
        >>> word_counts["hello"]
        3
        >>> word_counts.most_common(1)
        [('hello', 3)]
    """
    """Count the frequency of each word in the input file."""
    text = load_text(input_file)
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    word_count = Counter(words)
    return word_count