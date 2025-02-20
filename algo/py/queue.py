class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    q.push("amir")
    q.push("khalil")
    print(q.pop())
