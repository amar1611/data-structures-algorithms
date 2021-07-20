class Node:
    
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None


    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node


    def insert_at_end(self, data):
        node = Node(data, None)

        # If the linked list is empty
        if self.head == None:
            self.head = node
            return
        
        # Iterate to the last node
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = node


    def insert_values(self, data_list):

        self.head = None

        for data in data_list:
            self.insert_at_end(data)


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next        
        return count


    def remove_at(self, index):

        if index < 0 or index > self.get_length():
            raise Exception("This is not a valid index")

        if index == 0:
            self.head = None
            return

        count = 0
        itr = self.head

        while itr:
            if count == index -  1 :
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next


    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("This is not a valid index")

        if index == 0:
            self.head = Node(data, self.head)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            count += 1
            itr = itr.next


    def print(self):
        if self.head == None:
            print("Linked list is empty")
            return

        itr = self.head
        while(itr):
            print(itr.data, end="-->")
            itr = itr.next
        print("\n")
        return

    # Excercise
    def insert_after_value(self, data_after, data_to_insert):
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next


    # Excercise
    def remove_by_value(self, data):
        # Remove first node that contains data

        # When there is no node
        if self.head == None:
            return
        
        # When only one node is present, remove the node
        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == "__main__":
    
    # Implementation
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(4)
    ll.insert_at_begining(3)
    ll.insert_at_begining(2)
    ll.insert_at_begining(1)
    ll.insert_at_end(6)
    ll.insert_at_end(7)
    ll.print()

    data_list = ["a", "b", "c", "d"]
    ll.insert_values(data_list)

    ll.print()

    print(ll.get_length())

    ll.remove_at(2)
    ll.print()

    ll.insert_at(2, "c")
    ll.print()

    ll.insert_after_value("c", "new")
    ll.print()

    ll.remove_by_value('new')
    ll.print()

    # Excercise
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.print()
    ll.remove_by_value("mango")
    ll.print()
    ll.remove_by_value("apple")
    ll.print()
    ll.remove_by_value("grapes")
    ll.print()
