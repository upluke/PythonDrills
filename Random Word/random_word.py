# You’ll need to make a class that works like this:

# it is instantiated with a path to a file on disk that contains words, one word per line

# it reads that file, and makes an attribute of a list of those words
# it prints out “[num-of-words-read] words read”
# (it doesn’t need to do all of this directly in the __init__ method; it might be a good idea for the __init__ method to call other functions to do some of this.)

# it provides a method, random(), which returns a random word from that list of words

# Note: the random method should not re-read the list of words each time; it should work with the already-read-in list of words.

# For example, assume you have a file at /Users/student/words.txt that looks like this:


"""Word Finder: finds random words from a dictionary."""


from random import choice


class WordFinder:

    """ Initialize the input path and the varibale for storing shown words"""

    def __init__(self, path):
        self.path = path

        self.shown_words = []

    """ Get the words from the file """

    def get_list(self):
        return open(self.path)

    """ Randomly print a line of work, but initals are excluded """

    def random(self):
        ran_word = choice(self.get_list().read().splitlines())
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        while True:
            if ran_word not in self.shown_words and ran_word not in list(alphabet):
                self.shown_words.append(ran_word)
                print(self.shown_words)
                return ran_word

        # file.close()


wf = WordFinder("words.txt")

# print(wf.random())
# print(wf.random())


# Subclass The RandomWordFinder
# Our RandomWordFinder is nice, but we’ve received a new requirement: sometimes, we’ll be provided with files that have blank lines, as well as lines that start with a # symbol to make a comment.

# When we work with this, we want it to return one of the actual foods, like “kale” or “apple”, but never to return the blank lines or comments.

# We can’t just change the original Word Finder, though — our requirements have changed, so it would be unfair for users of that class to have this behavior suddenly change.

# Make a subclass, SpecialWordFinder, that uses WordFinder, but changes needed parts so it can work. Try to do this so as little code as needed is duplicated.


class SpecialWordFinder(WordFinder):

    def read(self):
        for word in super().get_list():
            if not word.startswith("#") and len(word) > 1:
                print(word.strip())


s = SpecialWordFinder("words2.txt")
s.read()
