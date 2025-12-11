class MemoryScan(object):
    """
    yield table data
    """
    def __init__(self, table):
        self.table = table
        self.idx = 0

    def next(self):
        if self.idx >= len(self.table):
            return None
        
        x = self.table[self.idx]
        self.idx += 1
        return x 

class Projection(object):
    pass

class Selection(object):
    pass

class Limit(object):
    pass

class Sort(object):
    """
    Sort based on the given key function
    """
    pass


def run(q):
    """
    run query
    """
    while True:
        x = q.next()
        if x is None:
            break
        yield x

def Q(*nodes):
    """
    Create linked list of executor nodes
    """
    ns = iter(nodes)
    parent = root = next(ns)
    for node in ns:
        parent.child = node 
        parent = node
    return root