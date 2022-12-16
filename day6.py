def search_string(string, quantity):
    """Searches input string for desired quantity of unique charactered substring"""
    buffer = []
    index = 0
    # iterate through input string
    for char in string:
        if char in buffer:
            # if char is already in buffer, adjust buffer position
            buffer = buffer[buffer.index(char) + 1:]
            buffer.append(char)
            index += 1
        else:
            # scanned char is not yet in buffer, so append char
            buffer.append(char)
            # if buffer length is now equal to search quant, the search is complete. Increment and return index
            if len(buffer) == quantity:
                index += 1
                return index
            else: # buffer list is not yet 4 unique characters. Increment index and continue search
                index += 1

# open and read file. Use search string function to find answer index.
with open("day6_part1_input.txt") as f:
    data_packet = f.read()
    search_result1 = search_string(data_packet, 4)
    search_result2 = search_string(data_packet, 14)
    search_result3 = search_string(data_packet, 15)

print(search_result1, search_result2, search_result3)
