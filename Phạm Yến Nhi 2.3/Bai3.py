# Bài 3: Nhập vào từ bàn phím ba số nguyên.
# a) Tính tổng và tích của ba số đó
# b) Hiệu của 2 số bất kỳ trong 3 số đó
# c) Phép chia lấy phần nguyên, phần dư và kết quả chính xác của 2 số bất kỳ trong 3 số

def main():
    try:
        a = int(input("Nhập số nguyên thứ nhất: "))
        b = int(input("Nhập số nguyên thứ hai: "))
        c = int(input("Nhập số nguyên thứ ba: "))
    except ValueError:
        print("Giá trị không hợp lệ. Vui lòng nhập số nguyên.")
        return

    # a) Tổng và tích
    tong = a + b + c
    tich = a * b * c
    print(f"a) Tổng: {tong}")
    print(f"a) Tích: {tich}")

    # b) Hiệu của mọi cặp (2 số bất kỳ)
    print("b) Hiệu của mỗi cặp:")
    pairs = [(a, b), (a, c), (b, c)]
    for x, y in pairs:
        print(f"   {x} - {y} = {x - y};  {y} - {x} = {y - x}")

    # c) Phép chia 2 số bất kỳ
    print("c) Phép chia của mỗi cặp (lấy số nguyên, phần dư, kết quả chính xác):")
    for x, y in pairs:
        if y != 0:
            print(f"   {x} / {y} -> nguyên: {x // y}, dư: {x % y}, chính xác: {x / y:.6f}")
        else:
            print(f"   {x} / {y} -> không chia được (chia cho 0)")

        if x != 0:
            print(f"   {y} / {x} -> nguyên: {y // x}, dư: {y % x}, chính xác: {y / x:.6f}")
        else:
            print(f"   {y} / {x} -> không chia được (chia cho 0)")


if __name__ == "__main__":
    main()
