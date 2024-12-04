def hamming_distance(s0, s1):
    return sum(s0[i] != s1[i] for i in range(len(s0)))

print(hamming_distance("abcde", "bcdef")) # 5
print(hamming_distance("abcde", "abcde")) # 0
print(hamming_distance("strong", "strung")) # 1