from stack import Stack


def is_balanced(input_str):
    st = Stack()
    for i in input_str:
        if i == "(":
            st.push(i)
        if i == ")":
            if st.pop() is None:
                return False
    return True if st.size() == 0 else False


if __name__ == "__main__":
    print(is_balanced("(()())"))
    print(is_balanced("((())"))
    print(is_balanced("()())"))
