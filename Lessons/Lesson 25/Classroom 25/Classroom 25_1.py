# Create a deque and add 3 elements to the left and right, after that remove 2 elements from left and right sides
# and then reverse the deque
class Deque:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        return self._items.pop()

    def remove_rear(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)

    def __repr__(self):
        return f"<Deque: `rear` {self._items} `front`>"

    def __str__(self):
        return self.__repr__()
    def reverse_1(self):
        return self._items.reverse()


if __name__ == "__main__":
    d = Deque()
    d.add_rear('Rear1')
    d.add_rear('Rear2')
    d.add_rear('Rear3')
    print(d)
    d.add_front('Front1')
    d.add_front('Front2')
    d.add_front('Front3')
    print(d)
    d.remove_rear() #remove rear3 element
    d.remove_rear()
    d.remove_front()
    d.remove_front()
    print(d)
    d.reverse_1()
    print(d)

