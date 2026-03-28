# Bài 5: Tính toán và in ra Chu vi, diện tích của hình tròn.
# Giá trị bán kính được nhập từ bàn phím.
# Công thức:
# CV = 2 * pi * R
# DT = pi * R * R
# Với pi = 3.14


def main():
    try:
        r = float(input("Nhập bán kính R (số thực): "))
    except ValueError:
        print("Giá trị không hợp lệ. Vui lòng nhập một số.")
        return

    if r < 0:
        print("Bán kính phải là số >= 0.")
        return

    pi = 3.14
    cv = 2 * pi * r
    dt = pi * r * r

    print(f"Chu vi hình tròn (CV) với R={r}: {cv:.4f}")
    print(f"Diện tích hình tròn (DT) với R={r}: {dt:.4f}")


if __name__ == "__main__":
    main()
