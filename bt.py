def tong_hai_so(a, b):
    """Trả về tổng 2 số a và b."""
    return a + b


def tong_danh_sach(ds):
    """Trả về tổng các phần tử trong danh sách số nguyên hoặc số thực."""
    return sum(ds)


def la_so_nguyen_to(n):
    """Trả về True nếu n là số nguyên tố (n>=2)."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def cac_so_nguyen_to_trong_khoang(a, b):
    """Trả về danh sách số nguyên tố trong khoảng [a,b]."""
    if a > b:
        a, b = b, a
    return [x for x in range(max(2, a), b + 1) if la_so_nguyen_to(x)]


def la_so_hoan_hao(n):
    """Trả về True nếu n là số hoàn hảo."""
    if n <= 1:
        return False
    tong = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            tong += i
            j = n // i
            if j != i:
                tong += j
        i += 1
    return tong == n


def cac_so_hoan_hao_trong_khoang(a, b):
    """Trả về danh sách số hoàn hảo trong khoảng [a,b]."""
    if a > b:
        a, b = b, a
    return [x for x in range(max(2, a), b + 1) if la_so_hoan_hao(x)]


def nhap_so_nguyen(thong_bao):
    while True:
        try:
            return int(input(thong_bao))
        except ValueError:
            print("Giá trị nhập không hợp lệ. Vui lòng nhập số nguyên.")


def nhap_danh_sach_so(thong_bao):
    while True:
        try:
            dong = input(thong_bao).strip()
            if dong == "":
                return []
            return [float(x) if '.' in x else int(x) for x in dong.split()]
        except ValueError:
            print("Giá trị nhập không hợp lệ. Hãy nhập dãy số cách nhau bởi dấu cách.")


def menu():
    print("""\n===== MENU LUYỆN TẬP =====""")
    print("1. Tính tổng 2 số")
    print("2. Tính tổng các số trong danh sách")
    print("3. Kiểm tra số nguyên tố")
    print("4. Tìm các số nguyên tố trong khoảng [a,b]")
    print("5. Kiểm tra số hoàn hảo")
    print("6. Tìm các số hoàn hảo trong khoảng [a,b]")
    print("7. Thoát")


def main():
    while True:
        menu()
        chon = nhap_so_nguyen("Chọn chức năng (1-7): ")

        if chon == 1:
            a = nhap_so_nguyen("Nhập số thứ nhất: ")
            b = nhap_so_nguyen("Nhập số thứ hai: ")
            print(f"Tổng {a} + {b} = {tong_hai_so(a, b)}")

        elif chon == 2:
            ds = nhap_danh_sach_so("Nhập dãy số (cách nhau bằng khoảng trắng): ")
            print(f"Tổng danh sách = {tong_danh_sach(ds)}")

        elif chon == 3:
            n = nhap_so_nguyen("Nhập số cần kiểm tra: ")
            print(f"{n} {'là' if la_so_nguyen_to(n) else 'không là'} số nguyên tố")

        elif chon == 4:
            a = nhap_so_nguyen("Nhập a: ")
            b = nhap_so_nguyen("Nhập b: ")
            lst = cac_so_nguyen_to_trong_khoang(a, b)
            print(f"Các số nguyên tố trong [{a},{b}]: {lst}")

        elif chon == 5:
            n = nhap_so_nguyen("Nhập số cần kiểm tra: ")
            print(f"{n} {'là' if la_so_hoan_hao(n) else 'không là'} số hoàn hảo")

        elif chon == 6:
            a = nhap_so_nguyen("Nhập a: ")
            b = nhap_so_nguyen("Nhập b: ")
            lst = cac_so_hoan_hao_trong_khoang(a, b)
            print(f"Các số hoàn hảo trong [{a},{b}]: {lst}")

        elif chon == 7:
            print("Cảm ơn, tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    main()
