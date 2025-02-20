from queue import Queue


def matchmake(queue, user):
    if user[1] == "join":
        queue.push(user[0])
        return
    if user[1] == "leave":
        queue.push(user[0])
        return


if __name__ == "__main__":
    q = Queue()
    user = ("amir", "join")
    user = ("khalil", "join")
    user = ("ahmed", "join")
    user = ("khalil", "leave")
    user = ("mm", "join")
    user = ("tt", "join")
    print(user[1])
