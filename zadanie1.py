a=open('books.txt',encoding='utf-8').readlines()
a.pop(0)
for i in range(len(a)):
    a[i]=a[i].strip(',').split('%')
    print(a[i])

for i in range(len(a)):
    r=(str(float(len(a[5])/sum(a[5]))))

f=open('books.txt','w',encoding='utf-8')
f.writelines('books_new.csv')
for x in a:
    f.writelines(','.join(x))
f.close()

