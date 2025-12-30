class Node:
    def __init__(self, data=None):
      self.data = data
      self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
          self.head = new_node
        else:
          cur = self.head
          while cur.next:
            cur = cur.next
          cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
          print("Попереднього вузла не існує.")
          return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def reverse_list(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
          return
      
        dummy = Node(float("-inf"))
        current = self.head

        while current:
          next_node = current.next

          prev = dummy
          while prev.next and prev.next.data <= current.data:
              prev = prev.next

          current.next = prev.next
          prev.next = current
          current = next_node

        self.head = dummy.next
    


def merge_two_lists(first: LinkedList, second: LinkedList):
    merged = LinkedList()
    if not first and not second:
        return merged
    
    if not first or first.head is None:
        return second
    
    if not second or second.head is None:
        return first
    
    f_c = first.head if first else None
    s_c = second.head if second else None

    while f_c is not None or s_c is not None:
        if f_c is None:
          merged.insert_at_end(s_c.data)
          s_c = s_c.next
        elif s_c is None:
          merged.insert_at_end(f_c.data)
          f_c = f_c.next
        elif f_c.data <= s_c.data:
          merged.insert_at_end(f_c.data)
          f_c = f_c.next
        else: 
          merged.insert_at_end(s_c.data)
          s_c = s_c.next

    return merged
      

llist_1 = LinkedList()

# Вставляємо вузли в початок
llist_1.insert_at_beginning(5)
llist_1.insert_at_beginning(10)
llist_1.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist_1.insert_at_end(20)
llist_1.insert_at_end(25)

# Друк зв'язного списку
print("Linked list 1")
llist_1.print_list()

print("After reverse :")
llist_1.reverse_list()
llist_1.print_list()

llist_2 = LinkedList()

llist_2.insert_at_beginning(23)
llist_2.insert_at_beginning(15)
llist_2.insert_at_beginning(7)
llist_2.insert_at_beginning(33)
llist_2.insert_at_beginning(3)
llist_2.insert_at_beginning(63)

print("Linked list 2")
llist_2.print_list()

llist_2.insertion_sort()
print("After sort :")
llist_2.print_list()

first = LinkedList()
first.insert_at_end(2)
first.insert_at_end(5)
first.insert_at_end(7)
first.insert_at_end(13)

second = LinkedList()
second.insert_at_end(3)
second.insert_at_end(63)

merged = merge_two_lists(first, second)

print('Merged')
merged.print_list()





