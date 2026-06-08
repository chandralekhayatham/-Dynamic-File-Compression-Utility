def decompress(encoded_file, output_file, root):
    with open(encoded_file, "r") as file:
        bits = file.read()

    decoded_text = ""
    current = root

    for bit in bits:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.char:
            decoded_text += current.char
            current = root

    with open(output_file, "w") as file:
        file.write(decoded_text)

    return decoded_text