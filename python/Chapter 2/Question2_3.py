from classes.LinkedList import *

def deleteNode(linkedlist, node):
    if node.next is None:
        node.value = None         

    else:
        node.value = node.next.value
        node.next = node.next.next         



#-----------test--------------
L = randomLinkedList(5, 0, 100)
node = L.head.next.next         # Given access to the 3rd node
print L
print "After deleting the node"
deleteNode(L, node)
print L