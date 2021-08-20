"""
LeetCode: 328

Trick is in the traversal.

"""

class Node():
    """
    Basic component for single linked list - A node
    A node consist of a value and a pointer to another node
    """
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList():

    """
    A linked list is a collection of nodes sequentially attached
    """
    def __init__(self):
        self.head = None


    def add_node(self, data):
        """
        Comparing to arrays, the biggest advantage of a linked list is insertion/deletion
        Arrays insertion/deletion - O(n) 
        Linked list insertion/deletion - O(1)
        """
        if self.head:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = Node(data)
        else:
            self.head = Node(data)

def find_length(head):
    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next
    return length

def odd_even_list(head):
    even_start = head.next # 2
    current = head # 1
    prev = head # 1 
    length = find_length(head)
    while current.next.next: # 4->5->None
       
        prev = current.next # 4 
        current.next = current.next.next # 3->5
        current = prev # 4 
    
    if length%2 != 0:
        current.next.next = even_start # 5->2
        current.next = None # 4->None
    else:
        current.next.next = None
        current.next = even_start

# def odd_even_list_opt(head):

#     if head is None or head.next is None:
#         return head

#     even_pos_start_node = head.next # 2
#     _current = head # 1
#     _prev = head # 1 
#     _next = head

#     length = 1 
#     while _current and _current.next: # 4->5->None
#         length += 1 
#         _prev = _current
#         _next = _current.next # 4 
#         _current.next = _current.next.next # 3->5
#         _current = _next # 4 
#     print(_prev.val)
#     if length%2 != 0:
#         _prev.next.next = even_pos_start_node # 5->2
#         _prev.next = None # 4->None
#     else:
#         _current.next.next = None
#         _current.next = even_pos_start_node

arr = [1, 2, 3, 4, 5]
lin_list = LinkedList()


for i in range(len(arr)):
    lin_list.add_node(arr[i])

odd_even_list¯(lin_list.head)
cur = lin_list.head
while cur:
    print(cur.val)
    cur = cur.next
