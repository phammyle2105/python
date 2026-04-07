import math

class PhanSo:
    def __init__(self, tu, mau=1):
        if mau == 0:
            raise ValueError("Mẫu số không được bằng 0!")
        self.tu = tu
        self.mau = mau

    # rút gọn
    def toi_gian(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln
        return self

    # cộng
    def cong(self, other):
        tu = self.tu * other.mau + other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau).toi_gian()

    # trừ
    def tru(self, other):
        tu = self.tu * other.mau - other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau).toi_gian()

    # nhân
    def nhan(self, other):
        tu = self.tu * other.tu
        mau = self.mau * other.mau
        return PhanSo(tu, mau).toi_gian()

    # chia
    def chia(self, other):
        if other.tu == 0:
            raise ValueError("Không thể chia cho phân số có tử = 0!")
        tu = self.tu * other.mau
        mau = self.mau * other.tu
        return PhanSo(tu, mau).toi_gian()

    # hiển thị
    def __str__(self):
        return f"{self.tu}/{self.mau}"
ps1 = PhanSo(2, 3)
ps2 = PhanSo(4, 5)

print("Phân số 1:", ps1)
print("Phân số 2:", ps2)

print("Tổng:", ps1.cong(ps2))
print("Hiệu:", ps1.tru(ps2))
print("Tích:", ps1.nhan(ps2))
print("Thương:", ps1.chia(ps2))
