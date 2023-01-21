#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#
class TrieNode:
     
    # Trie node class
    def __init__(self):
        self.children = [None]*26
        self.count = 1
 
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
 
class Trie:
     
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
        self.keys = {}
 
    def getNode(self):
     
        # Returns new trie node (initialized to NULLs)
        return TrieNode()
 
    def _charToIndex(self,ch):
         
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
         
        return ord(ch)-ord('a')
 
 
    def insert(self,key):
         
        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        #pCrawl.count +=1
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            pCrawl.count+=1
            # if current character is not present
            if not pCrawl.children[index]:
                node = self.getNode()
                pCrawl.children[index] = node
            pCrawl = pCrawl.children[index]
 
        # mark last node as leaf
        pCrawl.isEndOfWord = True
 
    def search(self, key):
         
        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if pCrawl.isEndOfWord:
                return True
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
 
        return True
    
    def count(self,key):
        count = 0
        res = True
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return 0
            pCrawl = pCrawl.children[index]
        return pCrawl.count if pCrawl.isEndOfWord else pCrawl.count-1

                
def contacts(queries):
    # Write your code here
    trie = Trie()
    res = []
    for query in queries:
        if query[0]=='add':
            trie.insert(query[1])
        else:
            res.append(trie.count(query[1]))
    return res

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
import testcase_contacts3
queries_rows = int(input().strip())

queries = []

for _ in range(queries_rows):
    queries.append(input().rstrip().split())

result = contacts(queries)

print('\n'.join(map(str, result)))
import testcase_contacts3_out
for i in range(len(result)):
    ea = int(input())
    if ea != result[i]:
        print('ea: '+str(ea))
        print('a: '+str(result[i]))
        print(i)
#fptr.write('\n')

#fptr.close()
