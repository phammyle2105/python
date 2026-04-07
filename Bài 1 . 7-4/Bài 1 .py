class HocVien:
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    # b) hiển thị thông tin
    def show_info(self):
        print("Họ tên:", self.ho_ten)
        print("Ngày sinh:", self.ngay_sinh)
        print("Email:", self.email)
        print("Điện thoại:", self.dien_thoai)
        print("Địa chỉ:", self.dia_chi)
        print("Lớp:", self.lop)

    # c) cập nhật thông tin
    def change_info(self, dia_chi=None, lop=None):
        if dia_chi:
            self.dia_chi = dia_chi
        if lop:
            self.lop = lop
 # tạo đối tượng
hv = HocVien(
    "Phạm Yến Nhi",
    "21/05/2005",
    "nhi@gmail.com",
    "0123456789",
    "Hải Phòng",
    "IT1.1"
)

# hiển thị ban đầu
print("=== Thông tin ban đầu ===")
hv.show_info()

# cập nhật thông tin
hv.change_info(dia_chi="Hà Nội", lop="IT12.x")

# hiển thị sau khi cập nhật
print("\n=== Sau khi cập nhật ===")
hv.show_info()