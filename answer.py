"""
Author: kuhnc@udel.edu
Updated: 2/13/2023
Description: A sample of taking a filename from stdin, loading it into a string
             array, and printing out the first line.
"""

##changed print all lines to add all line and to return sum
def print_all_lines(lines: list[str]) -> int:
    """ Print each line, then return the last one. """
    sum = 0
    latest_line = None
    for line in lines:
        # Readlines includes the newline character
        latest_line = line.strip()
        last_number = int(latest_line)
        #print(latest_line)
        if(last_number>0):
            sum+=last_number
        elif(line == -999):
            break
        else:
            continue
    print(sum)
    return sum


if __name__ == "__main__":
    # Get the filename from stdin
    filename = input()

    # Open the file and read in its contents
    with open(filename) as data_file:
        lines = data_file.readlines()

    # Actually do the work
    print_all_lines(lines)