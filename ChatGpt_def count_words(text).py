# Splits the input text into words using whitespace and returns the total number of words.
def count_words(text):
    words = text.split()
    return len(words)
