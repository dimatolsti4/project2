S = input().replace(' ','').upper()
a = ''
t = ''
asd = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']

for i in range (0,len(S)):
    if (64 < ord(S[i]) < 91):
        a = a + '0'
    else:
        a = a + '1'
for i in range (0,len(S),5):
    b = a[i:i+5]
    b = int(b,2)
    t = t + asd[b]
print(t)
