_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

chan = []
le = []

for i in _list:
    if i % 2 == 0:
        chan.append(i)
    else:
        le.append(i)

print("Số chẵn:", chan)
print("Số lẻ:", le)