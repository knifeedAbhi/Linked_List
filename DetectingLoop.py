class Node:
    def __init__(self,data,next = None):
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

    def CheckingLoop(self):
        exist = set()
        current = self.head

        while current.next!=None:
            if current in exist:
                return True

            else:
                exist.add(current)
                current = current.next


obj = LinkedList()
obj.append(45)
obj.append(90)
obj.append(4)
obj.append(33)

#detecting loop
obj.head.next.next.next.next = obj.head
if obj.CheckingLoop():
    print('Looping exists')
else:
    print('No looping found')
