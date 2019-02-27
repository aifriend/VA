class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def count(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self, back=0):
        return self.items[len(self.items) - (1 + back)]

    def size(self):
        return len(self.items)

    def find(self, index, key, compare):
        for item in reversed(self.items):
            item_list = item[index]
            for value_list in item_list:
                if key in value_list:
                    if compare(value_list[key]):
                        return item
        return []
