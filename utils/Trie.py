class Node:
    def __init__(self,data):
        self.data = data 
        self.children = [None]*128
        self.word_end = False 

class Trie:
    def __init__(self):
        self.root = Node('')

    def insert(self,word):
        
        word = word.lower()
        nodes = self.root.children
        for each_char in word[:-1]:
            idx = ord(each_char)-ord('a')
            if nodes[idx] is None:
                nodes[idx] = Node(each_char)
            nodes = nodes[idx].children
        idx = ord(word[-1])-ord('a')
        if nodes[idx] is None:
            nodes[idx] = Node(word[-1])
            nodes[idx].word_end = True


    def find(self,word):

        word = word.lower()
        nodes = self.root.children
        for each_char in word[:-1]:
            idx = ord(each_char)-ord('a')
            if nodes[idx] is None:
                return False
            nodes = nodes[idx].children
        idx = ord(word[-1])-ord('a')
        if nodes[idx] is None:
            return False 
        return nodes[idx].word_end
    
    def __collect(self,root,current_word,words):
        if root:
            if root.word_end:
                words.append(current_word)
            
            nodes = root.children
            for current_node in nodes:
                if current_node is not None:
                    char = current_word+current_node.data
                    self.__collect(current_node,char,words)

    def sort(self):
        words = []
        self.__collect(self.root,'',words)
        return words



    def autocomplete(self,prefix):

        prefix = prefix.lower()
        idx = ord(prefix[0]) - ord('a')
        nodes =  self.root.children

        if nodes[idx] is None: return []

        for each_char in prefix[:-1]:
            idx = ord(each_char) - ord('a')
            if nodes[idx] is not None:
                nodes = nodes[idx].children
        words = []
        idx = ord(prefix[-1]) - ord('a')
        self.__collect(nodes[idx],prefix,words)
        return words
        

            



