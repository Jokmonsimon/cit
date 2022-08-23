word = "Python"

print(word[1:3]) # yt
print(word[1:-2]) # n

# my_list = [_ for _ in 'abcdefghi']
# print(my_list)

alphabet = []
# ord represent the character unicode code, A to 65.
# chr convert 65 to A.
# variable alphabet get all value.
for i in range(ord('A'), ord('Z') + 1):
    alphabet.append(chr(i))
print(alphabet)
