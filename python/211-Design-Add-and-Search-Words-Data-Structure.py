class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie

        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any letter.
        """
        def search_in_node(word, node) -> bool:
            for i, ch in enumerate(word):
                if not ch in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == '.':
                        for x in node:
                            if x != '$' and search_in_node(word[i + 1:], node[x]):
                                return True
                    # if no nodes lead to answer
                    # or the current character != '.'
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    node = node[ch]
            return '$' in node

        return search_in_node(word, self.trie)
    
    

#class WordNode:
    #def __init__(self):
        #self.children = {}
        #self.isEnd = False

#class WordDictionary:
    #def __init__(self):
        #self.root = WordNode()

    #def addWord(self, word):
        #node = self.root
        #for w in word:
            #if w in node.children:
                #node = node.children[w]
            #else:
                #node.children[w] = WordNode()
                #node = node.children[w]
        #node.isEnd = True

    #def search(self, word):
        #stack = [(self.root,word)]
        #while stack:
            #node, w = stack.pop()
            #if not w:
                #if node.isEnd:
                    #return True
            #elif w[0]=='.':
                #for n in node.children.values():
                    #stack.append((n,w[1:]))
            #else:
                #if w[0] in node.children:
                    #n = node.children[w[0]]
                    #stack.append((n,w[1:]))
        #return False
    