# Doubly Linked List Approach
class Node:
    def __init__(self, char: str):
        self.char = char
        self.next = None
        self.prev = None

class TextEditor:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cursor = self.head

    def addText(self, text: str) -> None:
        for char in text:
            node = Node(char)
            tmp = self.cursor.next
            self.cursor.next = node
            node.next = tmp
            tmp.prev = node
            node.prev = self.cursor
            self.cursor = self.cursor.next

    def deleteText(self, k: int) -> int:
        count = 0
        while k > 0 and self.cursor != self.head:
            prev_node = self.cursor.prev
            next_node = self.cursor.next
            prev_node.next = next_node
            next_node.prev = prev_node
            self.cursor = prev_node
            k -= 1
            count += 1
        return count

    def cursorLeft(self, k: int) -> str:
        while k > 0 and self.cursor != self.head:
            self.cursor = self.cursor.prev
            k -= 1
        return self._get_left_text()
        
    def cursorRight(self, k: int) -> str:
        while k > 0 and self.cursor.next != self.tail:
            self.cursor = self.cursor.next
            k -= 1
        return self._get_left_text()

    def _get_left_text(self) -> str:
        text = []
        count = 0
        curr = self.cursor

        while curr != self.head and count < 10:
            text.append(curr.char)
            curr = curr.prev
            count += 1
        return "".join(text[::-1])

        



    

        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)