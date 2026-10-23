import heapq
import math
from collections import Counter
from itertools import count


class Node:
    __slots__ = ("freq", "sym", "left", "right")

    def __init__(self, freq, sym=None, left=None, right=None):
        self.freq = freq
        self.sym = sym
        self.left = left
        self.right = right


def build_huffman(freqs):
    counter = count()
    heap = [(f, next(counter), Node(f, sym=s)) for s, f in freqs.items()]
    heapq.heapify(heap)

    if len(heap) == 0:
        return {}, None
    if len(heap) == 1:
        sym = heap[0][2].sym
        return {sym: "0"}, heap[0][2]

    while len(heap) > 1:
        f1, _, n1 = heapq.heappop(heap)
        f2, _, n2 = heapq.heappop(heap)
        merged = Node(f1 + f2, left=n1, right=n2)
        heapq.heappush(heap, (f1 + f2, next(counter), merged))

    root = heap[0][2]
    codes = {}

    def traverse(node, code):
        if node.left is None and node.right is None:
            codes[node.sym] = code or "0"
            return
        traverse(node.left, code + "0")
        traverse(node.right, code + "1")

    traverse(root, "")
    return codes, root


def print_tree(node, prefix=" ", is_left=True):
    if node is None:
        return
    if node.left is None and node.right is None:
        sym_repr = repr(node.sym)
        print(f"{prefix}{'|-- ' if is_left else '!-- '}{sym_repr} ({node.freq})")
    else:
        print(f"{prefix}{'|-- ' if is_left else '!-- '}* ({node.freq:g})")
        print_tree(node.left, prefix + ("|   " if is_left else "    "), True)
        print_tree(node.right, prefix + ("|   " if is_left else "    "), False)


def encode_text(text):
    freqs = Counter(text)
    codes, root = build_huffman(freqs)
    encoded = "".join(codes[ch] for ch in text)
    return codes, root, encoded


def decode_text(encoded, codes):
    inv = {v: k for k, v in codes.items()}
    out, cur = [], ""
    for bit in encoded:
        cur += bit
        if cur in inv:
            out.append(inv[cur])
            cur = ""
    return "".join(out)


def entropy(freqs):
    total = sum(freqs.values())
    return -sum((f / total) * math.log2(f / total) for f in freqs.values() if f > 0)


def exercise_1():
    print("EXERCISE 1 — Huffman code table")

    freqs = {"a1": 0.31, "a2": 0.26, "a3": 0.24, "a4": 0.18, "a5": 0.01}
    codes, root = build_huffman(freqs)

    print("\nTree structure:")
    print_tree(root)

    print(f"\n{'Symbol':<8}{'Frequency':<12}{'Code':<10}{'Length':<8}")
    for sym in sorted(freqs, key=lambda k: -freqs[k]):
        print(f"{sym:<8}{freqs[sym]:<12}{codes[sym]:<10}{len(codes[sym]):<8}")


def exercise_2():
    print("EXERCISE 2")

    text = input("\nEnter text to encode: ")

    codes, root, encoded = encode_text(text)

    print("\nTree structure:")
    print_tree(root)

    print("\nCode table:")
    for sym, code in sorted(codes.items(), key=lambda kv: (len(kv[1]), kv[0])):
        print(f"  {repr(sym):<6} -> {code}")

    print(f"\nOriginal text ({len(text)} chars): {text!r}")
    print(f"Encoded ({len(encoded)} bits): {encoded}")

    decoded = decode_text(encoded, codes)
    print(f"Roll-back is: {decoded == text}")

def exercise_3():
    print('EXERCISE 3')

    text = "Algorithms and data structures"
    codes, root, encoded = encode_text(text)

    print("\nTree structure:")
    print_tree(root)

    print(f"\n{'Char':<6}{'Freq':<6}{'Code':<12}")
    for sym in sorted(codes, key=lambda c: (len(codes[c]), c)):
        print(f"{repr(sym):<6}{text.count(sym):<6}{codes[sym]:<12}")

    print(f"\nEncoded bit string:\n{encoded}")

    decoded = decode_text(encoded, codes)
    print(f"\nDecoded: {decoded!r}")
    print(f"Roll-back is: {decoded == text}")


if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()