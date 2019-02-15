S = str(input('Enter a word: '))
even_indices = [elem for i, elem in enumerate(list(S)) if i % 2 == 0]
odd_indices = [elem for i, elem in enumerate(list(S)) if i % 2 != 0]

even_str = str1 = ''.join(str(e) for e in even_indices)
odd_str = str1 = ''.join(str(e) for e in odd_indices)
print(even_str + "  " + odd_str)
