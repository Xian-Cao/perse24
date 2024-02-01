scrambled = input()
scrambled_list = list(scrambled)
unscrambled_list = scrambled_list[2:] + scrambled_list[:2]
unscrambled_string = ''
for i in unscrambled_list:
  unscrambled_string += i
print(unscrambled_string)
