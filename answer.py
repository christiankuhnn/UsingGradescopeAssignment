"""
Author: kuhnc@udel.edu
Updated: 2/13/2023
Description: A sample of taking a filename from stdin, loading it into a string
             array, and printing out the first line.
"""
def addNumbers(nums: list[int]):
    i=1
    temp=[]
    if(len(nums)==0):
        return None
    for num in range(i,(len(nums))):
        if(int(nums[i]==-999)):
            break
        elif(int(nums[i])<0):
            i+=1
        else:
            temp.append(int(nums[i]))
            i+=1
    if(len(temp)==0):
        return "EMPTY"
    final = sum(temp)
    return final
def print_all_lines(lines: list[str]) -> str:
    """ Print each line, then return the last one. """
    latest_line = None
    for line in lines:
        # Readlines includes the newline character
        latest_line = line.strip()
        print(latest_line)
        return latest_line


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