import subprocess as run


def import_sig(loc):
    global command 
    command = 'gpg'
    return run.run([command, '--import '+loc])

def gpg_decode():
    file_name = input("Enter the file you want to decode: ")
    return run.run([command, '-d '+file_name])


pkey_loc = r"/home/nestor.a.rivas78/Documents/CND practical/Messages_(2)/Messages/Butters.asc"
import_sig(pkey_loc)
print(gpg_decode())
#pkey_loc = input("Enter file path to public key: ")
