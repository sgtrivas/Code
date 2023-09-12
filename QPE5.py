
def tilde_backspace(string_in):
    string_out = ''
    for i in range(len(string_in)):
        if string_in[i] != '~':
            string_out += string_in[i]
        else:
            string_out = string_out[:-1]
    return string_out

print(tilde_backspace("abc~~~c")) # "c"
print(tilde_backspace("abcdef~~~c")) # "abcc"
print(tilde_backspace("abc~~d~~~~~~")) # ""
print(tilde_backspace("~~~~~~~")) # ""
print(tilde_backspace("Hello World!?~")) # "Hello World!"