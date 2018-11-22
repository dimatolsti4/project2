import os

crypted_text = input('Введите зашифрованный текст').replace(' ','').upper()
while (crypted_text.isalpha() == 0) or (len(crypted_text) % 5 != 0):
    print('В строке должны быть только буквы')
    print('Количество символов должно делится на 5')
    crypted_text = input('Введите зашифрованный текст').replace(' ','').upper()
binary_code = ''
uncrypted_text = ''
letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

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
os.system('pause')
