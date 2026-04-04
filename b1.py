# bảng mã
code = {'a': '!', 'b': '@', 'c': '#', 'd': '$'}

# tạo bảng giải mã (đảo ngược)
decode = {v: k for k, v in code.items()}

# nhập chuỗi
text = input("Nhập chuỗi: ")

# mã hóa
encoded = ""
for ch in text:
    if ch in code:
        encoded += code[ch]
    else:
        encoded += ch

print("Mã hóa:", encoded)

# giải mã
decoded = ""
for ch in encoded:
    if ch in decode:
        decoded += decode[ch]
    else:
        decoded += ch

print("Giải mã:", decoded)