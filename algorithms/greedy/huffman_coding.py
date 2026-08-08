import heapq
from collections import Counter


class HuffmanNode:
    """
    Represents a node in the Huffman Tree.
    """

    def __init__(self, char=None, frequency=0):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def build_huffman_tree(text):
    """
    Build a Huffman Tree from the input text.
    """

    frequencies = Counter(text)

    heap = [
        HuffmanNode(char, frequency)
        for char, frequency in frequencies.items()
    ]

    heapq.heapify(heap)

    while len(heap) > 1:

        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(
            frequency=left.frequency + right.frequency
        )

        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(node, code="", codes=None):
    """
    Generate Huffman codes by traversing the Huffman Tree.
    """

    if codes is None:
        codes = {}

    if node is None:
        return codes

    if node.char is not None:
        codes[node.char] = code or "0"
        return codes

    generate_codes(node.left, code + "0", codes)
    generate_codes(node.right, code + "1", codes)

    return codes


def huffman_encode(text):
    """
    Encode text using Huffman Coding.

    Returns:
        tuple: Encoded text and Huffman codes.
    """

    if not text:
        return "", {}

    root = build_huffman_tree(text)

    codes = generate_codes(root)

    encoded = "".join(codes[char] for char in text)

    return encoded, codes


if __name__ == "__main__":

    text = "hello huffman"

    encoded, codes = huffman_encode(text)

    print("Original Text:")
    print(text)

    print("\nHuffman Codes:")

    for char, code in sorted(codes.items()):
        display_char = "space" if char == " " else char
        print(f"{display_char}: {code}")

    print("\nEncoded Text:")
    print(encoded)