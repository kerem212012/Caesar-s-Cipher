def cipher(mode, language, shift, letter):
    stop = 0
    english = ' '.join('abcdefghijklmnopqrstuvwxyz').split()
    russian = ' '.join('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ').lower().split()
    if language == 'english':
       if mode == 'cipher':
           numletter = len(letter)
           for i in range(numletter):
                letter = ' '.join(letter).split()
                ind =english.index(letter[i])+shift
                ind = ind % 26
                del letter[i]
                letter.insert(i,english[ind])
                letter = ''.join(letter)
       elif mode == 'decipher':
           numletter = len(letter)
           for j in range(numletter):
                letter = ' '.join(letter).split()
                ind =english.index(letter[j])+(shift*-1)
                ind = ind % 26
                del letter[j]
                letter.insert(j,english[ind])
                letter = ''.join(letter)
    elif language == 'russian':
       if mode == 'cipher':
           numletter = len(letter)
           for k in range(numletter):
                letter = ' '.join(letter).split()
                ind =russian.index(letter[k])+shift
                ind = ind % 26
                del letter[k]
                letter.insert(k,russian[ind])
                letter = ''.join(letter)
       elif mode == 'decipher':
           numletter = len(letter)
           for l in range(numletter):
                letter = ' '.join(letter).split()
                ind =russian.index(letter[l])+(shift*-1)
                ind = ind % 26
                del letter[l]
                letter.insert(l,russian[ind])
                letter = ''.join(letter)
    print('Your word:',letter)
def main():
    print('Select mode (cipher/decipher)')
    mode = input().strip()
    print('Select language(english/russian)')
    language = input().strip()
    print('How far do you want to go?')
    shift = int(input().strip())
    print('Write your word...')
    letter = input().lower().strip()
    cipher(mode, language, shift, letter)


main()
