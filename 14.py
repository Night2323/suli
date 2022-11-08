a = input("Mondat: ")
h = len(a)
for i in range(h):
    if a[i]=="a":
        print(end="e")
    else:
        print(end=a[i])
al = list(a)
for i in al:
    if i == a:
        al[i] = "e"
    else:
        pass
print(al)


