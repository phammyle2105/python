class NhanVien:
    dem = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        NhanVien.dem += 1

    def hien_thi_so_luong(self):
        print("Tổng số nhân viên được tạo:", NhanVien.dem)

    def hien_thi_nhan_vien(self):
        print("Tên:", self.name, ", Lương:", self.salary)

    def cap_nhat(self, name=None, salary=None):
        if name:
            self.name = name
        if salary:
            self.salary = salary


# tạo đối tượng
nhan_vien_dev = NhanVien('Nguyen Van A', 1000)
nhan_vien_test = NhanVien('Nguyen Van B', 1200)

# gọi hàm
nhan_vien_dev.hien_thi_nhan_vien()
nhan_vien_test.hien_thi_nhan_vien()

# in số lượng
print("Số nhân viên:", nhan_vien_dev.dem)

# in thuộc tính
print(nhan_vien_dev.name)
print(nhan_vien_test.name)