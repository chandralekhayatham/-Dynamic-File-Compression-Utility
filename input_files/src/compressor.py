from src.huffman import build_huffman_tree, generate_codes


def compress(input_file, output_file):
    with open(input_file, "r") as file:
        text = file.read()

    tree = build_huffman_tree(text)
    codes = generate_codes(tree)

    encoded_text = ""

    for char in text:
        encoded_text += codes[char]

    with open(output_file, "w") as file:
        file.write(encoded_text)

    return tree, codes