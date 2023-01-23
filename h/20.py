names = []
addresses = []

while True:
    name = input("Név:")
    if name == "Vége":
        break
    address = input("Cím: ")
    names.append(name)
    addresses.append(address)

print("Nevek és címek listája:")
for i in range(len(names)):
    print(names[i] + ": " + addresses[i])

name_to_search = input("Név amit keresünk: ")

for i in range(len(names)):
    if names[i] == name_to_search:
        print(name_to_search + " címe:  " + addresses[i])
        break
    else:
        print("Name not found in the list.")

while True:
    name = input("Név:")
    if name == "Vége":
        break
    if name in names:
        print("Már benne van.")
    else:
        address = input("Cím: ")
        names.append(name)
        addresses.append(address)