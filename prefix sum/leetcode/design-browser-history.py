class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.current = self.head

    def visit(self, url: str) -> None:
        new = ListNode(url, self.current)
        self.current.next = new
        self.current = new

    def back(self, steps: int) -> str:
        count = 0
        while count < steps and self.current.prev:
            self.current = self.current.prev
            count += 1
        return self.current.val

    def forward(self, steps: int) -> str:
        count = 0
        while count < steps and self.current.next:
            self.current = self.current.next
            count += 1
        return self.current.val

