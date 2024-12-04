import subprocess as run


def import_sig(loc):
    global command 
    command = 'gpg'
    return run.run(command+' --import '+loc, shell=True)

def gpg_decode():
    
    try:
        file_name = input("Enter the file you want to decode: ")
        print()
        return run.run(command+' -d '+file_name, shell=True)
            
    except (OSError, SystemError, ValueError,NameError): 
        raise
        

pkey_loc = input("Enter file path to public key: ")

import_sig(pkey_loc)
print()
print(gpg_decode())
print()

