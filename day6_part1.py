with open("day6_part1_input.txt") as f:
    data_packet = f.read()
    buffer = []
    index = 0
    #iterate through data_packet
    for char in data_packet:
        # if scanned char is already in buffer, adjust buffer position
        if char in buffer:
            buffer = buffer[buffer.index(char) + 1:]
            buffer.append(char)
            index += 1
        else:
            # scanned char is not yet in buffer, so append char
            buffer.append(char)
            # if buffer length is now 4, buffer is now 4 unique characters, so the search is complete
            if len(buffer) == 4:
                index += 1
                break
            else: # buffer list is not yet 4 unique characters
                index += 1

print(index)