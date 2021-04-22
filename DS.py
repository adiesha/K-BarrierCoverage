class DS:
    def __init__(self, G, removeNode):
        self.nodes = list(G.nodes)
        self.nodes.remove(removeNode)

        self.OUT = {}
        self.IN = {}
        for i in list(G.nodes):
            self.OUT[i] = list(G.successors(i))

        for i in self.nodes:
            self.IN[i] = list(G.predecessors(i))

    def query(self, v):
        if self.OUT[v]:
            return self.OUT[v].pop()
        else:
            return None

    def remove(self, u):
        for i in self.IN[u]:
            self.OUT[i].remove(u)


def main():
    print("main")


if __name__ == '__main__':
    main()