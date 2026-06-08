import os

from src.compressor import compress
from src.decompressor import decompress

INPUT = "input_files/sample.txt"
COMPRESSED = "compressed_files/compressed.txt"
DECOMPRESSED = "decompressed_files/output.txt"

os.makedirs("compressed_files", exist_ok=True)
os.makedirs("decompressed_files", exist_ok=True)

tree, codes = compress(INPUT, COMPRESSED)

print("\nHuffman Codes:\n")

for char, code in codes.items():
    print(f"{char} : {code}")

decompress(COMPRESSED, DECOMPRESSED, tree)

original_size = os.path.getsize(INPUT)
compressed_size = os.path.getsize(COMPRESSED)

ratio = compressed_size / original_size

print("\nCompression Report")
print("------------------")
print("Original Size:", original_size, "bytes")
print("Compressed Size:", compressed_size, "bytes")
print("Compression Ratio:", round(ratio, 2))

print("\nDecompression Successful")