class Anagram:
    def __init__(self, word):
        """
        Initializes an Anagram instance with a given word.
         
        Args:
        word (str): The word to compare against.
        """
        self._word = word.lower()

    def match(self, possible_anagrams):
        """
        Finds anagrams from the list of possible anagrams.

        Args:
        possible_anagrams (list): List of words to check for anagrams.

        Returns:
        list: List of matching anagrams.
        """

        matching_anagrams = []
        # Iterate over each word in the list of possible anagrams
        for anagram in possible_anagrams:
            anagram_lower = anagram.lower()
            # Check if the current word is an anagram of the initial word
            if anagram_lower != self._word:
                sorted_word = "".join(sorted(anagram_lower))
                if sorted_word == "".join(sorted(self._word)):
                    matching_anagrams.append(anagram)
        return matching_anagrams

# Testing code
words = ["listen", "silent", "golf"]
test1 = Anagram("enlist")
print(test1.match(words))  # Output: ['silent']
