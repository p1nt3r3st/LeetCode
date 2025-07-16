class Trie:

    def __init__(self):
        self.tokens = set()
        self.words = set()

    def insert(self, word: str) -> None:
        for i in range(1, len(word) + 1):
            self.tokens.add(word[:i])
        self.words.add(word)

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.tokens


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # True
print(trie.search("app"))  # False
print(trie.startsWith("app"))  # True
trie.insert("app")
print(trie.search("app"))  # True
