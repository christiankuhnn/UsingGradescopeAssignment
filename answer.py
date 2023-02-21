"""
Author: kuhnc@udel.edu
Updated: 2/13/2023
Description: A sample of taking a filename from stdin, loading it into a string
             array, and printing out the first line.
"""
def addNumbers(lines: list[str]):
    sum = 0
    inputs = []
    for line in lines:
        current_line = int(line)
        inputs.push(line)
        if current_line > 0:
            sum+=current_line
        
        elif current_line == -999:
            break
    
    #return "EMPTY" if sum == 0 else sum
    return inputs
                
        



if __name__ == "__main__":
    # Get the filename from stdin
    filename = input()

    # Open the file and read in its contents
    with open(filename) as data_file:
        lines = data_file.readlines()

    # Actually do the work
   ## print_all_lines(lines)
    ## call out function and print
    print(addNumbers(lines))