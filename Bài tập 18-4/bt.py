import sqlite3

# Kết nối database (nếu chưa có sẽ tự tạo file)
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# =========================
# A) Lấy danh sách MANAGER
# =========================
print("A) Danh sách nhân viên là MANAGER:")
cursor.execute("SELECT * FROM employee WHERE job = 'MANAGER'")
managers = cursor.fetchall()

for m in managers:
    print(m)

# =========================
# B) Insert phòng ban
# =========================
print("\nB) Thêm phòng ban mới:")

cursor.execute("""
INSERT INTO department (id, name, location)
VALUES (?, ?, ?)
""", (99, "IT Department", "Ha Noi"))

print("Đã thêm phòng ban!")

# =========================
# C) Insert bản thân vào employee
# =========================
print("\nC) Thêm nhân viên (bạn):")

cursor.execute("""
INSERT INTO employee (id, name, job, salary, dept_id)
VALUES (?, ?, ?, ?, ?)
""", (999, "Nih", "DEVELOPER", 1000, 99))

print("Đã thêm nhân viên!")

# =========================
# D) Update CLARK thành bạn
# =========================
print("\nD) Cập nhật CLARK:")

cursor.execute("""
UPDATE employee
SET name = ?, job = ?, salary = ?, dept_id = ?
WHERE name = 'CLARK'
""", ("Nih", "DEVELOPER", 1000, 99))

print("Đã cập nhật CLARK!")

# =========================
# E) Xóa MILLER
# =========================
print("\nE) Xóa nhân viên MILLER:")

cursor.execute("""
DELETE FROM employee
WHERE name = 'MILLER'
""")

print("Đã xóa MILLER!")

# Lưu thay đổi
conn.commit()

# Đóng kết nối
conn.close()