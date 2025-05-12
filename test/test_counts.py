import os
from collections import Counter
from example_package.counts import load_text, clean_text, count_words

TEST_FILE = os.path.join(os.path.dirname(__file__), "test.txt")

def test_load_text():
    """Test that load_text correctly reads file content"""
    text = load_text(TEST_FILE)
    expected = "Insanity is doing the same thing over and over and expecting different results."
    assert text == expected

def test_clean_text():
    """Test that clean_text removes punctuation and converts to lowercase"""
    text = "Insanity is doing the same thing over and over and expecting different results."
    cleaned = clean_text(text)
    expected = "insanity is doing the same thing over and over and expecting different results"
    assert cleaned == expected

def test_count_words():
    """Test that count_words correctly counts word frequencies"""
    word_counts = count_words(TEST_FILE)
    expected = Counter({
        "is": 1,
        "doing": 1,
        "the": 1,
        "same": 1,
        "thing": 1,
        "over": 2,
        "and": 2,
        "expecting": 1,
        "different": 1,
        "results": 1,
        "insanity": 1
    })
    assert word_counts == expected
