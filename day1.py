def main():
    # definitions
    FILE_NAME = "day1_input.txt"
    DIAL_SIZE = 100

    # counters
    arrow = 50      # dial initiated at 50
    password = 0    # password counter

    # open the file
    with open(FILE_NAME, 'r') as file:

        # go line by line
        for line in file:
            
            # clean the line
            c_line = line.strip()
            if not c_line:
                continue

            # get the first letter, and then the number
            direction = c_line[0]
            num_str = c_line[1:]

            # num_str to integer
            try:
                num = int(num_str)
            except ValueError:
                print("Cannot convert to integer")
                continue

            # get direction and add/subtract the number
            if direction == 'R':
                arrow = (arrow + num) % DIAL_SIZE
            elif direction == 'L':
                arrow = (arrow - num) % DIAL_SIZE
            else:
                print("Error in logic")
            
            # if arrow is at 0, add to password
            if arrow == 0:
                password += 1

    # print password
    print("Password is: " + str(password))

if __name__ == "__main__":
    main()