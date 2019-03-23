def compress_str(message):
    output_str = ""
    counter = 0
    previous = message[0]
    for letter in message:
        if letter == previous:
            counter += 1
        else:
            output_str += previous
            output_str += str(counter)
            previous = letter
            counter = 1
    if counter != 1:
        output_str += previous
        output_str += str(counter)
    return output_str


message = "aabbbbcdddeaaaaa"
message = compress_str(message)
print(message)