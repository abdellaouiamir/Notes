class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def size(self):
        return len(self.items)

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()

    def peek(self):
        if self.size() == 0:
            return None
        return self.items[-1]


class DebounceStack(Stack):
    def push(self, item):
        if item == self.peek():
            return
        return super().push(item)


if __name__ == "__main__":
    st = Stack()
    print(st.peek())
    st.push("amir")
    st.push("khalil")
    print(st.peek())
    print(st.pop())
    print(st.peek())
    ss = DebounceStack()
    print(ss.size())
    ss.push("amir")
    ss.push("amir")
    ss.push("khalil")
    print(ss.size())
