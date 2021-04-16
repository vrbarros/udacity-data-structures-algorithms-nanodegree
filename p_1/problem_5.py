# Blockchain

import hashlib
import time
from datetime import datetime


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

    def add_block(self, data, timestamp=None):
        if not timestamp:
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
        timestamp_duplicated = self.timestamp_duplicated(timestamp)

        if data and not timestamp_duplicated:
            self.head = Block(timestamp=timestamp, data=data, previous=self.head)
        elif not timestamp_duplicated:
            print("A data value is required to add a new block to Blockchain\n")
        else:
            print("No duplicated timestamp allowed\n")

    def timestamp_duplicated(self, timestamp):
        head = self.head

        if head is None:
            return False

        while head:
            if head.timestamp == timestamp:
                return True
            head = head.previous

        return False

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
    print(blockchain.head, "\n")
    time.sleep(1)

print("Blockchain Size:", blockchain.size(), "\n")

blockchain.add_block(data=None)
# print "A data value is required to add a new block to Blockchain"

freeze_timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
blockchain.add_block(data="Time1", timestamp=freeze_timestamp)
print(blockchain.head, "\n")
blockchain.add_block(data="Time2", timestamp=freeze_timestamp)
print(blockchain.head, "\n")
# print "No duplicated timestamp allowed"