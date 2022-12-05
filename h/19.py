list = []
#első rész
s = 1
while s!=0:
    a = int(input("Szám:"))
    s = a
    if a == 0:
        pass
    else:
        list.append(a)
#második rész
print(list)
#harmadik rész
for i in list:
    print(i)
#negyedik rész
list.sort()
print(list)
#ötörik rész
list.sort(reverse=True)
print(list)
#hatodik rész
print(len(list))
#hetedik rész
print(sum(list))
#nyolcadik rész
print(max(list))