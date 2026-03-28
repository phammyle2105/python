# Bài 1: Nhập vào từ bàn phím hai số nguyên. Tính tổng và in ra tổng của hai số nguyên đó.

def main():
    try:
        a = int(input("Nhập số nguyên thứ nhất: "))
        b = int(input("Nhập số nguyên thứ hai: "))
    except ValueError:
        print("Giá trị không hợp lệ. Vui lòng nhập số nguyên.")
        return

    tong = a + b
    print(f"Tổng của {a} và {b} là: {tong}")


if __name__ == "__main__":
    main()
