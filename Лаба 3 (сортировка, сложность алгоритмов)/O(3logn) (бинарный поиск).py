print('Введите элементы массива через пробел')
spisok=list(map(int,input().split(" ")))
num=int(input())
count=0
spisok.sort()
print(spisok)
l=0
r=len(spisok)
while l<r-1:
    s=(r+l)//2
    if num<spisok[s]:
        r=s
    else:
        l=s
    count=count+1
if spisok[l]==num:
    print('Число',num,'находится в массиве')
else:
    print('Число',num,'не находится  в массиве')
print('Потребовалось',count,'операции(ий)')