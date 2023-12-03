# Opening file
file1 = open('assets/day1.txt', 'r')
total = 0

def forward_pass(line):
    for index, char in enumerate(line):
        if char.isdigit():
            return index, int(char)

def reverse_pass(line):
    for index, char in enumerate(line):
        if char.isdigit():
            return len(line) - 1 - index, int(char)

# Iterate over each line in file1.txt 
for line in file1:
    line = line.strip()  # Remove newline characters
    index_forward, num_forward = forward_pass(line)
    line_reversed = line[::-1]
    index_backward, num_backward = reverse_pass(line_reversed)

    total += (num_forward * 10) + num_backward
    # print(f"{index_forward}, {index_backward} : {num_forward}, {num_backward}")

print(f"Total: {total}")