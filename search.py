
class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def add_word(self, word):
        if len(word) > 1:
            letter = word[0]
        else:
            letter = word
        if not letter in self.children.keys():
            self.children[letter] = Node()
        child = self.children[letter]
        if len(word) > 1:
            child.add_word(word[1:])
        else:
            child.is_end = True

    def is_word(self, word):
        if len(word) > 1:
            letter = word[0]
        else:
            letter = word
        if not letter in self.children.keys():
            return False
        child = self.children[letter]
        if len(word) > 1:
            return child.is_word(word[1:])
        return True

    def print(self, indent=0):
        for l, child in self.children.items():
            print(" " * (indent * 2) + l)
            child.print(indent+1)

    def autocomplete(self, query):
        node = self
        for i in range(len(query)):
            if not query[i] in node.children:
                return []
            node = node.children[query[i]]
        return node.aggregate_words(query)
        

    def aggregate_words(self, word):
        words = []
        if self.is_end:
            words.append(word)
        for l, child in self.children.items():
            child_words = child.aggregate_words(word + l)
            for word_1 in child_words:
                words.append(word_1)
        return words
        
            
        

root = Node()
root.add_word("Johan")
root.add_word("Jonas")
root.add_word("Kasper")
root.add_word("Karakter")
root.add_word("Kravstor")
print(root.is_word("Jon"))
root.print()
while True:
    prompt = input("Search: ")
    print(root.autocomplete(prompt))
