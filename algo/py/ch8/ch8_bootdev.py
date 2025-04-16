from queue import Queue


def matchmake(queue, user):
    if user[1] == "join":
        if user[0] not in queue.items:
            queue.push(user[0])
    elif user[1] == "leave":
        for i in range(len(queue.items)):
            if queue.items[i] == user[0]:
                queue.items.pop(i)
                break
    if queue.size() >= 4:
        user1 = queue.pop()
        user2 = queue.pop()
        print(f"`{user1}` matched `{user2}`")

    else:
        print("No match found")


if __name__ == "__main__":
    q = Queue()
    user = ("amir", "join")
    matchmake(q, user)
    user = ("khalil", "join")
    matchmake(q, user)
    user = ("ahmed", "join")
    matchmake(q, user)
    user = ("khalil", "leave")
    matchmake(q, user)
    user = ("mm", "join")
    matchmake(q, user)
    user = ("tt", "join")
    matchmake(q, user)
    print(q.size())
