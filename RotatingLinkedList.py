class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head

        while last.next:
            last = last.next

        last.next = new_node



    def rotating(self):
        current = self.head
        count = 1
        while count < 5 and current is not None:
            current = current.next
            count+=1

        if current is None:
            return

        rotating_element = current

        while current.next is not None:
            current = current.next

        current.next = self.head

        self.head = rotating_element.next

        rotating_element.next = None

    def printing(self):
        temp = self.head
        while temp:
            print (temp.data)
            temp = temp.next

obj = LinkedList()


obj.append(20)
obj.append(4)
obj.append(34)
obj.append(13)
obj.append(18)
obj.append(26)

print('Old List is ')
obj.printing()

obj.rotating()
print('New List is')
obj.printing()
