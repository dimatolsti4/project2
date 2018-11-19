crypted_text = input().replace(' ','').upper()
binary_code = ''
uncrypted_text = ''
letters = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']

for letter in range (0,len(crypted_text)):
    if (64 < ord(crypted_text[letter]) < 91):
        binary_code = binary_code + '0'
    else:
        binary_code = binary_code + '1'
for letter in range (0,len(crypted_text),5):
    num = binary_code[letter:letter+5]
    num = int(num,2)
    uncrypted_text = uncrypted_text + letters[num]
print(uncrypted_text)
