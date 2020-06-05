morse = '. .       . . . .   . -   -   .       - . - -   - - -   . . -'
letter = []
spaces = 0
morseword = []
alphabet = 'abcdefghijklmnopqrstuvwxyz '
morsecode = ['. -','- . . .','- . - .','- . .','.','. . - .','- - .','. . . .','. .','. - - -','- . -','. - . .','- -','- .','- - -','. - - .','- - . -','. - .','. . .','-','. . -','. . . -','. - -','- . . -','- . - -','- - . .',' ']
word = []
for d in range(len(morse)):
    if morse[d] == '.':
        if spaces == 3:
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            morseword.append(''.join(letter))
            letter = []
        elif spaces == 7:
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            morseword.append(''.join(letter))
            morseword.append(' ')
            letter = []
        letter.append('.')
        if d == len(morse) - 1:
            morseword.append(''.join(letter))
            letter = []
        spaces = 0
    elif morse[d] == '-':
        if spaces == 3:
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            morseword.append(''.join(letter))
            letter = []
        elif spaces == 7:
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            morseword.append(''.join(letter))
            morseword.append(' ')
            letter = []
        letter.append('-')
        if d == len(morse) - 1:
            morseword.append(''.join(letter))
            letter = []
        spaces = 0
    else:
        letter.append(' ')
        spaces += 1

for c in morseword:
    for b in range(27):
        if c == morsecode[b]:
            word.append(alphabet[b])

print(''.join(word))
