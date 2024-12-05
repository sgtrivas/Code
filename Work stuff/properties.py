import pyinputplus as pyip
from datetime import datetime as d
from datetime import timezone as t
# Define the file name
def fieldInfo():
       
    fields = [
        "Field1", #  Start time
        "Field2", #  End time
        "Field3", 
        "Field4", 
        "Field5",
        "Field6", 
        "Field7", 
        "Field8", #  UUID?
        "Field9", 
        "Field10", 
        "Field11", 
        "Field12"
    ]

    # Manually populate the fields
    global data
    zulu = d.now(t.utc).strftime("%Y%m%dT%H:%M:%SZ")
   
    data = {}
    for field in fields:
        #  This is the uuid field so its pre populated
        if field == "Field8":
            data[field] = "test"
        #  The start time (field1) and end time (field2) can be set to the same time.
        elif field == "Field1" or field == "Field2":
            data[field] = zulu
        else:
            value = input(f"Enter {field}=")
            data[field] = value

    ans = pyip.inputChoice(['y', 'n'], f"Do the fields have the correct information? y or n: ")
    if ans.lower() == "y":
        writeFile(data)
    else:
        print("\nPlease re-enter the fields.")
        fieldInfo()

    # Write the data to the file
def writeFile(value):
     file_name = "properties.txt"

     with open(file_name, "w") as file:
        for field, value in data.items():
            file.write(f"{field}={value}\n")

        print(f"Data saved to {file_name}")

fieldInfo()