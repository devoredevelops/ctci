from classes.LinkedList import *


# if k = 1, return the last element
def kth_to_last(linkedlist, k):
    if k <= 0:
        return "invalid k"
    pointer2 = linkedlist.head
    for _ in range(k-1):
        if pointer2.next is None:
            return "k exceeds the length of linkedlist"
        else:
            pointer2 = pointer2.next
    pointer1 = linkedlist.head
    while pointer2.next != None:
        pointer2 = pointer2.next
        pointer1 = pointer1.next
    return pointer1
   
 

#---------------test------------------
L = randomLinkedList(8, 0, 100)
print L
print "The 3th to last element is", kth_to_last(L, 3)
