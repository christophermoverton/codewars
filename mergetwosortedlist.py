#!/bin/python3

import math
import os
import random
import re
import sys
import testcase_mergetwosortedlist
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node):
    while node:
        print(str(node.data))

        node = node.next


# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    res = head1
    node = head2
    while node:
        node2 = res
        prev = None
        while node2:
            if node.data > node2.data:
                if node2.next:
                    prev = node2
                    node2 = node2.next
                else:
                    node2.next = SinglyLinkedListNode(node.data)
                    break
            else:
                nnode = SinglyLinkedListNode(node.data)
                if prev:
                    prev.next = nnode
                    nnode.next = node2
                    break
                else:
                    nnode.next = node2
                    res = nnode
                    node2 = nnode
                    break
        node = node.next
    return res
                
        

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

tests = int(input())

for tests_itr in range(tests):
    llist1_count = int(input())

    llist1 = SinglyLinkedList()

    for _ in range(llist1_count):
        llist1_item = int(input())
        llist1.insert_node(llist1_item)
        
    llist2_count = int(input())

    llist2 = SinglyLinkedList()

    for _ in range(llist2_count):
        llist2_item = int(input())
        llist2.insert_node(llist2_item)

    llist3 = mergeLists(llist1.head, llist2.head)

    print_singly_linked_list(llist3)
#    fptr.write('\n')

#    fptr.close()
