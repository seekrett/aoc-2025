'''
loop for each line:
    initialize max to 0
    loop 'left' start at 0 until n-1
        loop 'right' start at 1 until n
            num = left & right
            if num > max
                max = num
    sum += max
'''

def main():
    # definitions
    FILE_NAME = "day3input.txt"

    # variables
    password = 0

    # open the file
    with open(FILE_NAME, 'r') as file:

        # go line by line
        for line in file:
            
            # clean the line
            c_line = line.strip()
            if not c_line:
                continue

            # sum up all the max 2-digit numbers
            password += findMax(c_line)
    
    print("The password is: " + str(password))

# find the max two-digit number in a line
def findMax(line):
    max = 0
    n = len(line)
    for left in range(n - 1):
        for right in range(left + 1, n):
            num = int(str(line[left]) + str(line[right]))
            if num > max:
                max = num
    return max

if __name__ == "__main__":
    main()
