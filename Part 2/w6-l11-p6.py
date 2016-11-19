class Queue(object):
    def __init__(self):
        self.queue = []
    
    def insert(self, e):
        self.queue.append(e)
    
    def remove(self):
        try:
            e = self.queue.pop(0)
        except:
            raise ValueError('Queue empty.')
        else:
            return e