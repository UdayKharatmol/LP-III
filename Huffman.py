import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq): self.char, self.freq, self.left, self.right = char, freq, None, None
    def __lt__(self, other): return self.freq < other.freq

def build_tree(freq):
    heap = [Node(char, f) for char, f in freq.items()]; heapq.heapify(heap)
    while len(heap) > 1:
        n1, n2 = heapq.heappop(heap), heapq.heappop(heap)
        merged = Node(None, n1.freq + n2.freq); merged.left, merged.right = n1, n2
        heapq.heappush(heap, merged)
    return heap[0]

def huffman_codes(node, code=""):
    return {node.char: code} if node.char else {**huffman_codes(node.left, code + "0"), **huffman_codes(node.right, code + "1")}

def huffman_encoding(msg):
    freq = defaultdict(int); [freq.update({ch: freq[ch] + 1}) for ch in msg]
    tree = build_tree(freq); codes = huffman_codes(tree)
    return "".join(codes[ch] for ch in msg), tree, codes

def huffman_decoding(encoded_msg, tree):
    decoded, node = "", tree
    for bit in encoded_msg:
        node = node.left if bit == "0" else node.right
        if node.char: decoded, node = decoded + node.char, tree
    return decoded

msg = input("Enter a message: ")
encoded, tree, codes = huffman_encoding(msg)
print("\nOriginal:", msg, "\nEncoded:", encoded, "\nCodes:", codes, "\nDecoded:", huffman_decoding(encoded, tree))
