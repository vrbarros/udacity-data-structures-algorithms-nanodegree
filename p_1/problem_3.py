# Huffman Coding

import sys


"""
Draft of the expected solution.

Encode:
1. We should take a string and determine the relevant character frequencies
2. Start building and sorting a list of tuples from the lowest to the highest frequencies
3. Assigning a binary code to each letter in a Huffman tree, need to use shorter codes most frequent letters
4. Need to remove frequencies from the previously built tree (recursive solution)
5. Encode text (will compress)

Decode:
1. Cycles through the encoded data 
2. Need to check binary code with the tree

"""


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

    def set_right_child(self, right):
        self.right = right

    def set_left_child(self, left):
        self.left = left

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def get_value(self):
        return self.value


class Tree:
    def __init__(self):
        self.root = None

    # Time complexity: O(n)
    def get_frequency_list(self, data):
        frequency_dict = {}

        for chr in data:
            if chr in frequency_dict:
                frequency_dict[chr] += 1
            else:
                frequency_dict[chr] = 1

        frequency_list = [(freq, chr) for chr, freq in frequency_dict.items()]
        frequency_list.sort(reverse=True)

        return frequency_list

    # Time complexity: O(n)
    def sort_nodes(self, nodes_list, node):
        node_freq, node_chr = node.get_value()
        max_index = len(nodes_list)
        current_index = 0

        while True:
            if current_index == max_index:
                nodes_list.append(node)
                return

            current_node_freq, current_node_chr = nodes_list[current_index].get_value()

            if current_node_freq <= node_freq:
                nodes_list.insert(current_index, node)
                return

            current_index += 1

    # Time complexity: O(n)
    def make(self, data):
        frequency_list = self.get_frequency_list(data)
        nodes_list = []

        for freq_chr_tuple in frequency_list:
            node = Node(freq_chr_tuple)
            nodes_list.append(node)

        while len(nodes_list) != 1:
            first_node = nodes_list.pop()
            second_node = nodes_list.pop()

            freq_first_node, chr_first_node = first_node.get_value()
            freq_second_node, chr_second_node = second_node.get_value()

            node = Node(
                (freq_first_node + freq_second_node, chr_first_node + chr_second_node)
            )
            node.set_left_child(second_node)
            node.set_right_child(first_node)

            self.sort_nodes(nodes_list, node)

        self.root = nodes_list[0]


class Huffman:
    def __init__(self, tree):
        self.tree = tree
        self.chr_dict = None
        self.rev_dict = None

    def reverse_dict(self):
        if self.chr_dict is None:
            self.chr_dict = self.encoded_dict(self.tree.root)

        rev_chr_dict = {}

        for value, key in self.chr_dict.items():
            rev_chr_dict[key] = value

        return rev_chr_dict

    def encoded_dict(self, node):
        if node is None:
            return {}
        freq, chr = node.get_value()
        chr_dict = dict([(i, "") for i in list(chr)])

        left_branch = self.encoded_dict(node.get_left_child())

        for key, value in left_branch.items():
            chr_dict[key] += "0" + left_branch[key]

        right_branch = self.encoded_dict(node.get_right_child())

        for key, value in right_branch.items():
            chr_dict[key] += "1" + right_branch[key]

        return chr_dict

    def encode(self, data):
        if self.chr_dict is None:
            self.chr_dict = self.encoded_dict(self.tree.root)

        encoded_data = ""

        for char in data:
            encoded_data += self.chr_dict[char]

        return encoded_data

    def decode(self, data):
        if self.rev_dict is None:
            self.rev_dict = self.reverse_dict()

        start_index = 0
        end_index = 1
        decoded_data = ""

        while start_index != len(data):
            bin = data[start_index:end_index]

            if bin in self.rev_dict:
                decoded_data += self.rev_dict[bin]
                start_index = end_index

            end_index += 1

        return decoded_data


def huffman_encoding(data):
    if data == "":
        return None, None

    tree = Tree()
    tree.make(data)

    huffman = Huffman(tree)
    encoded_data = huffman.encode(data)

    if encoded_data == "":
        return None, None

    return encoded_data, tree


def huffman_decoding(data, tree):
    if data == "":
        return None

    huffman = Huffman(tree)
    decoded_data = huffman.decode(data)

    return decoded_data


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print(
        "The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))
        )
    )
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    empty_input = ""

    encoded_data, tree = huffman_encoding(empty_input)

    print(encoded_data, "when expected None for empty input\n")
    # print None

    repetitive_char = "AAA"

    encoded_data, tree = huffman_encoding(repetitive_char)

    print(encoded_data, "when expected None for repetitive char\n")
    # print None
