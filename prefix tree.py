class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = ''
        self.tree = {'': []}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        flag = 1
        found = 0
        while flag:
            flag = 0
            children = []
            for u in self.tree[node]:
                if u == word:
                    found = 1
                    flag = 0
                    break
                elif len(u) < len(word) and u == word[0:len(u)]:
                    node = u
                    flag = 1
                    break
                elif len(u) > len(word) and word == u[0:len(word)]:
                    children.append(u)
        if not found:
            self.tree.update({word: children})
            for child in children:
                self.tree[node].remove(child)
            self.tree[node].append(word)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        flag = 1
        found = 0
        while flag:
            flag = 0
            for u in self.tree[node]:
                if u == word:
                    found = 1
                    flag = 0
                    break
                elif len(u) < len(word) and u == word[0:len(u)]:
                    node = u
                    flag = 1
                    break
        return found

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        flag = True
        found = False
        while flag:
            flag = 0
            for u in self.tree[node]:
                if u == prefix:
                    found = True
                    flag = False
                    break
                elif len(u) < len(prefix) and u == prefix[0:len(u)]:
                    node = u
                    flag = True
                    break
        if found:
            return found
        else:
            for u in self.tree[node]:
                if len(prefix) < len(u) and prefix == u[0:len(prefix)]:
                    return True
        return found


tree = Trie()
tree.insert('a')
tree.insert('b')
tree.insert('ab')
tree.insert('abcd')
tree.insert('abc')
tree.insert('abc')
tree.search('abc')
tree.search('abce')
