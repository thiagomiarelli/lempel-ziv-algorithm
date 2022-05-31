class Tree:
    def __init__(self, text = "", compressed = ""):
        self.root = Node('', 0, None)
        self.current = self.root
        self.index = 1
        self.text = text
        self.compressed = compressed
        self.dictionary = {0: ""}
    
    def add_child(self, child_node):
        self.index += 1
        self.current.children.append(child_node)

    def get_sufix(self, character):
        current_children = self.current.children_keys()
        correspondent_child = current_children.index(character) if character in current_children else -1
        if correspondent_child == -1:
            new_node = Node(character, self.index, self.current)
            self.add_child(new_node)
            self.compressed = self.compressed + new_node.get_node_notation()
            self.current = self.root

        else:
            self.current = self.current.children[correspondent_child]

    def compress(self):
        for character in self.text:
            self.get_sufix(character)
        return self
    
    def get_compressed_cell_value(self, cell):
        cell_id, parent_id, value = cell.split(chr(4))
        cell_id = int(cell_id)
        parent_id = int(parent_id)
        if cell_id not in self.dictionary:
            self.dictionary[cell_id] = self.dictionary[parent_id] + value
        return self.dictionary[cell_id]

    def decompress(self):
        cells = self.compressed.split(chr(2))
        print(len(cells))
        for cell in cells[1:]:
            self.text = self.text + self.get_compressed_cell_value(cell)
class Node:
    def __init__(self, value, index, parent):
        self.index = index
        self.value = value
        self.children = []
        self.parent = parent

    def __repr__(self):
        return 'Node({})'.format(self.value)
    
    def __str__(self, level=0):
        ret = "\t"*level+" index: " + str(self.index) + " key: " + str(self.value) +"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def add_child(self, child_node):
        self.children.append(child_node)
        return child_node

    def children_keys(self):
        return [child.value for child in self.children]
    
    #doc: gera a notacao de compressao de um no, por exemplo, se o no for o no 1 com valor a, o seu pai eh o no 0, entao o no 1 tera a notacao #1,0,a
    def get_node_notation(self):
        return chr(2)+ str(self.index) + chr(4) + str(self.parent.index) + chr(4) + str(self.value)