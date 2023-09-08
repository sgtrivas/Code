def infoFile():
    with open ("/home/nestor.a.rivas78/Documents/Python/info.txt", encoding="UTF8") as openFile:
        for a_line in openFile:
            print(f'{a_line.readlines()}')
infoFile()
