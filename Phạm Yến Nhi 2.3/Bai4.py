# Bài 4: Nhập vào từ bàn phím ba chuỗi ký tự. In ra màn hình một chuỗi ký tự được ghép từ ba chuỗi nhập vào.

def main():
    s1 = input("Nhập chuỗi 1: ")
    s2 = input("Nhập chuỗi 2: ")
    s3 = input("Nhập chuỗi 3: ")

    ket_qua = f"{s1} {s2} {s3}"
    print("Kết quả ghép: ", ket_qua)


if __name__ == "__main__":
    main()
