string = input(" Please enter a String:")
freq = {}

for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Output:\n "
      + str(freq))
