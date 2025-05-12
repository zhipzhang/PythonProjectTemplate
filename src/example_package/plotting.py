import matplotlib.pyplot as plt
from collections import Counter
def plot_words(word_counts:Counter, top_n = 10):
    """Plot the top N words from the word counts."""
    top_n_words = word_counts.most_common(top_n)
    word, count = zip(*top_n_words)
    fig = plt.bar(range(top_n), count)
    plt.xticks(range(top_n), word, rotation=45)
    plt.xlabel('Words')
    plt.ylabel('Counts')
    return fig
