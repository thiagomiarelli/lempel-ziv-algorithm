import numpy as np


class Tree:
    def __init__(self, text = "", compressed = np.array([], dtype=np.byte)):
        self.root = Node('', 0, None)
        self.current = self.root
        self.index = 1
        self.text = text + "$"
        self.compressed = compressed
        self.dictionary = {0: ""}
    
    #adiciona nó na árvore
    def add_child(self, child_node):
        self.index += 1
        self.current.children.append(child_node)

    # adiciona o nó na arvore se nao houver o sufixo ou atualiza o no atual da iteracao
    def get_sufix(self, character):
        current_children = self.current.children_keys()
        correspondent_child = current_children.index(character) if character in current_children else -1
        if correspondent_child == -1:
            new_node = Node(character, self.index, self.current)
            self.add_child(new_node)
            self.compressed = np.append(self.compressed, new_node.convert_node_to_number())
            self.current = self.root

        else:
            self.current = self.current.children[correspondent_child]

    #comprime caracter a caractere
    def compress(self):
        for character in self.text:
            self.get_sufix(character)
        return self
    
    #retorna o valor da celula comprimida
    def get_compressed_cell_value(self, cell):
        cell_id, parent_id, value = cell
        if cell_id not in self.dictionary:
            self.dictionary[cell_id] = self.dictionary[parent_id] + value
        return self.dictionary[cell_id]
        
    #itera sobre a arvore descomprimindo
    def decompress(self):
        for i in range(len(self.compressed)):
            cell = convert_number_to_node(self.compressed[i], i + 1)
            self.text = self.text + self.get_compressed_cell_value(cell)

class Node:
    def __init__(self, value, index, parent):
        self.index = index
        self.value = value
        self.children = []
        self.parent = parent

    def add_child(self, child_node):
        self.children.append(child_node)
        return child_node

    def children_keys(self):
        return [child.value for child in self.children]
    
    def convert_node_to_number(self):
        return int(('{0:024b}'.format(self.parent.index) + '{0:08b}'.format(ord(self.value)))[:32],2)

def convert_number_to_node(number:int, index):
    bits = '{0:032b}'.format(number)
    father_index = int(bits[:24], 2)
    value = chr(int(bits[24:32], 2))
    return (index, father_index, value)

