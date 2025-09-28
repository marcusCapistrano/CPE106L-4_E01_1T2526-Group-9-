import random
import os

def getWords(filename):
    """Reads words from a file and returns them as a tuple."""
    words = []
    with open(filename, "r") as file:
        for line in file:
            word = line.strip()
            if word:  # skip empty lines
                words.append(word.upper())
    return tuple(words)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load vocabulary from files
articles = getWords(os.path.join(BASE_DIR, "articles.txt"))
nouns = getWords(os.path.join(BASE_DIR, "nouns.txt"))
verbs = getWords(os.path.join(BASE_DIR, "verbs.txt"))
prepositions = getWords(os.path.join(BASE_DIR, "prepositions.txt"))

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

if __name__ == "__main__":
    main()
