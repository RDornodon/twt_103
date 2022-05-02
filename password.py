from random import choice, shuffle, choices, seed

seed('website.name')
pw_len = 10

abc = [chr(c) for c in range(65,91)]
ABC = [chr(c) for c in range(97,123)]
num = [*map(str,range(10))]
spc = [*'!+-_,.#&@']

result = [choice(abc),choice(ABC),choice(num),choice(spc)] + choices(abc+ABC+num+spc, k=pw_len-4)
shuffle(result)
print(''.join(result))

