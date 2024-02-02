import collections
#  function that takes the file name, opens it and passes the contents into a list
def find_unique_entry(filename):
    with open(filename, 'r') as file:
        # the list variable is declared global so it can be used elsewhere
        global entries
        entries = file.readlines()
        # prints the length of the list which is 8099 values. remember list index starts a 0
        #print(len(entries))
    # Count occurrences of each entry efficiently
    entry_counts = collections.Counter(entries)
    print(entry_counts)

    # Find the entry with a count of 1. a tuple with list comprehension added 
    unique_entry = next(entry for entry, count in entry_counts.items() if count == 1)
    #print(unique_entry,entries.index(unique_entry))

    return unique_entry

if __name__ == '__main__':
    filename = '/home/nestor.a.rivas78/Downloads/L4Processes.txt'  # Replace with your actual filename
    unique_entry = find_unique_entry(filename)

    if unique_entry:
        print(f"The unique 'svchost.exe' entry is: {unique_entry.strip()}, in line: {entries.index(unique_entry)+1}")
    else:
        print("No unique entries found.")