import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    freq = Counter(text)

    heap = [Node(char, f) for char, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(node, current="", codes={}):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current

    generate_codes(node.left, current + "0", codes)
    generate_codes(node.right, current + "1", codes)

    return codes