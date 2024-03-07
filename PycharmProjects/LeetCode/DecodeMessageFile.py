def pyramid(message_file):
    map = {}
    string = ""
    # Read the entire file content
    with open(message_file, 'r') as file:
        for line in file.readlines():
            num, word = line.split(" ")
            map[int(num)] = word.rstrip("\n")
    # Calculate max number in a pyramid base on the information from the file
    map = {int(key): value for key, value in sorted(map.items())}
    max_n = max(map)
    print(f'max_n = {max_n}')
    print(map)
    # Calculate max numbers of levels in the pyramid
    levels = 1
    total_numbers = 0
    while total_numbers + levels <= int(max_n):
        total_numbers += levels
        levels += 1
    levels -= 1
    print(levels)
    n = 0
    for i in range(1, levels+1):
        n += i
        string += str(map[n]) + " "
    return string

message_file = r"C:/git/file.txt"
print(pyramid(message_file))