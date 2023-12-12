# My attempt at verify passwords from a file called passwords.txt

count = 0
with open("passwords.txt", "r") as pass_file:
    new_pass = pass_file.read()
    new_pass = new_pass.split(',')
    #print(new_pass)
    for item in new_pass:
        #print(item)
        if "admin" in item:
            print(f"fail admin '{item}'")
            count +=1
        elif "Admin" in item:
            print(f"fail admin '{item}'")
            count +=1
        elif "password" in item:
             print(f"fail Password '{item}'")
             count +=1
        elif "Password" in item:
             print(f"fail Password '{item}'")
             count +=1
        elif "root" in item:
             print(f"fail root '{item}'" )
             count +=1
        elif "Root" in item:
             print(f"fail root '{item}'" )
             count +=1
        elif '`' in item:
             print(f"fail !,@,:,& '{item}'" )
             count += 1
        elif len(item) < 4:
             print(f"failed min length '{item}'")
             count+=1
        elif len(item) > 20:
             print(f"failed max length '{item}'")
             count+=1
        elif item.islower():
             print(f"failed case '{item}'")
             count +=1
    print    
    print(count)
    # for item in pass_file.read():
    #     print(item)
        
            

