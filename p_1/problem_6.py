# Union and Intersection


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def __len__(self):
        head = self.head
        length = 0

        while head:
            head = head.next
            length += 1

        return length

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head

        while node:
            size += 1
            node = node.next

        return size

    def copy(self):
        list_copy = LinkedList()
        node = self.head

        while node:
            node_copy = Node(node.value)
            list_copy.append(node_copy)
            node = node.next

        return list_copy


def union(llist_1, llist_2):
    llist_1_copy = llist_1.copy()
    llist_2_copy = llist_2.copy()

    node = llist_1_copy.head

    while node.next:
        node = node.next

    node.next = llist_2_copy.head

    return llist_1_copy


def intersection(llist_1, llist_2):
    intersec = LinkedList()

    llist_1_dict = {}

    node = llist_1.head
    while node:
        if not node.value in llist_1_dict:
            llist_1_dict[node.value] = 0
        node = node.next

    node = llist_2.head
    while node:
        if node.value in llist_1_dict:
            node_copy = Node(node.value)
            intersec.append(node_copy)

        node = node.next

    return intersec


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

test_union1 = union(linked_list_1, linked_list_2)
print("Test Union 1:", test_union1, "Count:", len(test_union1), "\n")
assert len(test_union1) == len(element_1) + len(element_2)

test_intersection1 = intersection(linked_list_1, linked_list_2)
print("Test Intersection 1:", test_intersection1, "Count:", len(test_intersection1), "\n")
assert len(test_intersection1) == 4


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

test_union2 = union(linked_list_3, linked_list_4)
print("Test Union 2:", test_union2, "Count:", len(test_union2), "\n")
assert len(test_union2) == len(element_1) + len(element_2)

test_intersection2 = intersection(linked_list_3, linked_list_4)
print("Test Intersection 2:", test_intersection2, "Count:", len(test_intersection2), "\n")
assert len(test_intersection2) == 0

linked_list_empty = LinkedList()

test_intersection3 = intersection(linked_list_empty, linked_list_empty)
print("Test Intersection 3:", test_intersection3, "Count:", len(test_intersection3), "\n")
assert len(test_intersection3) == 0

test_union4 = union(linked_list_3, linked_list_empty)
print("Test Union 4:", test_union4, "Count:", len(test_union4), "\n")
assert len(test_union4) == 10