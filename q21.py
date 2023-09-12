def digital_root(n):
    x =\
    lambda n :sum(list(map(int," "\
		.join(str(n))\
		.split())))
    out=n
    while len(str(out)) > 1:
        out = x(out)
    return out_

print(digital_root("5550"))
