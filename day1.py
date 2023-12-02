# Opening file
file1 = open('/home/bwaidyaratne/repos/adventofcode/advent-of-code2023/assets/day1.txt', 'r')
total = 0
 
# Using for loop
for line in file1:
    reversed_line = line[::-1]
    first_number = None
    first_reversed = None

    for index, char in enumerate(line):
        if char.isdigit():
            first_num_index = index
            total += int(char) * 10
            break

    for index_rev, char_rev in enumerate(reversed_line):
        if char_rev.isdigit():
            rev_index = len(line) - 1 - index_rev
            total += int(char_rev)
            break

    print(f"{first_num_index}: {total}, {rev_index}: {total}")

print("Total lines processed:", count)