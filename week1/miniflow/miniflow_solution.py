class Node:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.function = kwargs.get('function', None)
        self.parent = None
        self.children = list()

    def add_child(self, node):
        node.parent = self
        self.children.append(node)
    
    def get_children(self):
        return self.children

    def dft(self):
        yield self
        for node in self.get_children():
            yield from node.dft()

    def get_parent(self, node):
        return self.parent
    
    def parents(self):
        curr_node = self
        while curr_node:
            yield curr_node
            curr_node = curr_node.parent
    
class Runner:
    def __init__(self):
        self.f1 = None
    
    def add(self, f1, *args):
        if args:
            self.f1 = Node(function=args[0])
            self.f1.add_child(Node(function=f1, id=str(f1)))
        else:
            self.f1 = Node(function=f1)

    def run(self, function):
        seq = iter(self.f1.dft())
        curr_node = next(seq) # yields itself first
        val = curr_node.function()
        for curr_node in seq:
            val = curr_node.function(val)
        return val

"""
ALTERNATIVE SOLUTION FOR RUNNER CLASS WITH SIMPLER ADD FUNCTION, BUT CONSEQUENTLY A
MORE COMPLEX RUN FUNCTION THAT TRAVERSES THE TREE TWICE (BUT ALSO USES)

class Runner:
    def __init__(self):
        self.f1 = None
    
    def add(self, f1, *args):
        self.f1 = Node(function=f1, id=str(f1))
        if args:
            self.f1.add_child(Node(function=args[0]))

    def run(self, function):
        seq = iter(self.f1.dft())
        curr_node = next(seq) # yields itself first
        while curr_node.get_children():
            curr_node = next(seq)
        seq = iter(curr_node.parents())
        curr_node = next(seq) # go the other way
        val = curr_node.function()
        for curr_node in seq:
            val = curr_node.function(val)
        return val
"""


        