# Blockchain

import hashlib
import time


class Block:
    def __init__(self, timestamp, data, previous):
        self.timestamp = timestamp
        self.data = data
        self.previous = previous
        self.hash = self._calc_hash()

    def _calc_hash(self):
        sha = hashlib.sha256()

        hash_str = str(self.data).encode("utf-8")

        sha.update(hash_str)

        return sha.hexdigest()

    def get_hash(self):
        return self.hash

    def __str__(self):
        previous_hash = self.previous.get_hash() if self.previous else None

        return "Data -> {}\nPrevious Hash -> {}\nCurrent Hash -> {}\nTimestamp -> {}".format(
            self.data,
            previous_hash,
            self.hash,
            self.timestamp,
        )


class Blockchain:
    def __init__(self):
        self.head = None

    def add_block(self, data):
        timestamp = time.gmtime()

        self.head = Block(timestamp=timestamp, data=data, previous=self.head)

    def size(self):
        head = self.head
        length = 0

        while head:
            head = head.previous
            length += 1

        return length


blockchain = Blockchain()

for value in ["Node1", "Node2", "Node3"]:
    blockchain.add_block(value)
    print(blockchain.head)

print("Blockchain Size:", blockchain.size())
