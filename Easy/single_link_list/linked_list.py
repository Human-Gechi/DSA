class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = self.head
        count = 0

        while current:
            if count == index:
                return current.val
            count += 1
            current = current.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        current = self.head
        count = 0

        while current and current.next:
            if count == index - 1:
                current.next = current.next.next
                return True

            current = current.next
            count += 1

        return False


    def getValues(self) -> List[int]:
        elements = []
        current = self.head
        while current:
            elements.append(current.val)
            current = current.next
        return elements

