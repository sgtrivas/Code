import collections
import pyinputplus as pyip

def findMe(filename):
    f = open(filename)
    allElements = f.readlines()
    c = collections.Counter(allElements)
    print(c)
    for i,j in c.items():
        if j == 1:
            return print(f"{i.strip()} is the different line and is located in line: {allElements.index(i)+1}")

print("""Run this script in the folder where the text file is located. 
        Use the absolute path if the script is NOT where file is located.
      CTRL+C to quit!\n""")


def getFilename():
    try:
        filename = pyip.inputFilepath("Please enter the file name: ")
        findMe(filename)
    except FileNotFoundError:
        print("check your file name! Try again")
        getFilename()
    except:
        print("Error")

if __name__ == '__main__':
    getFilename()