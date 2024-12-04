with open('info.txt', encoding="UTF8") as file_ref:
    lines_start_with_t = [line for line in file_ref if line[0].upper() == "T"]
    #print(lines_start_with_t)
for t_line in lines_start_with_t:
        print(f'{t_line[:-1] = }')
