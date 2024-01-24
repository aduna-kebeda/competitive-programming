class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        i = 0
        temp = self.head
        while i < index and temp:
            temp = temp.next
            i += 1
        return temp.val if temp else -1

    def addAtHead(self, val: int) -> None:
        newNode = MyLinkedList()
        newNode.val = val
        newNode.next = self.head
        self.head = newNode

    def addAtTail(self, val: int) -> None:
        newNode = MyLinkedList()
        newNode.val = val
        newNode.next = None
        if not self.head:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
            return
        newNode = MyLinkedList()
        newNode.val = val
        c = 0
        temp = self.head
        while c < index - 1 and temp:
            temp = temp.next
            c += 1
        if not temp:
            return
        temp2 = temp.next
        newNode.next = temp2
        temp.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return
        if index == 0:
            if self.head:
                temp = self.head
                self.head = self.head.next
                del temp
            return
        c = 0
        temp2 = self.head
        temp = self.head
        while c < index and temp:
            temp2 = temp
            temp = temp.next
            c += 1
        if not temp:
            return
        temp2.next = temp.next
        del temp


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
