_list = ['abc', 'hello', 'hi', 'python', 'ok']

n = int(input("Nhập n: "))

ket_qua = [x for x in _list if len(x) > n]

print(ket_qua)