class Queue(object):
    def __init__(self):
        self.queue = []
        self.end_index = 0
        self.heading_index = -1

    def show_content(self):
        return self.queue

    def enqueue(self, item):
        return self.queue.append(item)

    def add_tail(self, item):
        return self.queue.insert(self.end_index, item)

    def dequeue(self):
        return self.queue.pop(self.end_index)

    def add_multiple(self, iterable):
        return self.queue.extend(iterable)

    def is_empty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

    def is_heading(self, item):
        if self.is_empty():
            return False
        else:
            if item == self.queue[self.heading_index]:
                return True
            else:
                return False

    def get_heading(self):
        if self.is_empty():
            return None
        else:
            return self.queue[self.heading_index]
    def get_tail(self):
        if self.is_empty():
            return None
        else:
            return self.queue[self.end_index]

    def summation(self, item):
        if not self.is_empty():
            from_queue = self.queue[self.heading_index]
            return [from_queue[0]+item[0], from_queue[1]+item[1]]
        else:
            print("this is error")
            exit(-1)
    def summation_end(self, item):
        if not self.is_empty():
            from_queue = self.queue[self.end_index]
            return [from_queue[0]+item[0], from_queue[1]+item[1]]
        else:
            print("this is error")
            exit(-1)




if __name__ == '__main__':
    queue = Queue()
    queue.add_multiple([[1,2],[3,4],[5,6]])
    print(queue.queue)
    x = queue.summation([20,30])
    print(x)
    print(queue.queue)
    pass