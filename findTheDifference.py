import collections
import pyinputplus as pyip
#  findMe opens the filename that it passed from the getFilename function, opens it and reads it into a list. 

def findMe(filename):
    f = open(filename)
    allElements = f.readlines()
    #  the collections module has a function called Counter that counts hashable objects. 
    #  It is a collection where elements are stored as 
    #  dictionary keys and their counts are stored as dictionary values. 
    #  Counts are allowed to be any integer value including zero or negative counts. 
    #  The Counter class is similar to bags or multisets in other languages.
    c = collections.Counter(allElements)
    #  The print statement below show the dictionary with the element:count key/value pair.
    print(c)
    #  for loop is created with two variables i and j to store the element:count pair of the dicionary items that are iterated 
    for i,j in c.items():
        #  conditional statement checks to see if the count of an element is greater than or equal to 1
        #  if it is greater than 1 the element and list index number (line number) is returned. 
        #  1 is added due to a list index beginning at 0
        if j >= 1:
            return print(f"{i.strip()} is the different line and is located in line: {allElements.index(i)+1}")
        else:
            print(f"{filename} has no unique items!")


print("""Run this script in the folder where the text file is located. 
        Use the absolute path if the script is NOT where file is located.
      CTRL+C to quit!\n""")


def getFilename():
    try:
        #  filepath has to be valid in order to pass this check, if valid it is passed to findMe(). inputFilepath will catch any blanks
        filename = pyip.inputFilepath("Please enter the file name: ")
        findMe(filename)
    except FileNotFoundError:
        #  if file name or path is not there, print error
        print("File not found: Check your file name or file path! Try again")
        getFilename()
    except:
        #  to catch all other issues
        print("Error")

if __name__ == '__main__':
    getFilename()
