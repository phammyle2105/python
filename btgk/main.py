from model.employee import Employee
from model.developer import Developer
from services.company import Company

company = Company()

def seed_data():
    e1 = Developer(1, "An", 1000, "Python")
    e2 = Developer(2, "Binh", 1200, "Java")
    e3 = Employee(3, "Cuong", 900)

    e1.add_project("AI")
    e1.add_project("Web")

    e2.add_project("Web")

    e3.add_project("AI")
    e3.add_project("ML")
    e3.add_project("Data")

    company.add_employee(e1)
    company.add_employee(e2)
    company.add_employee(e3)


def menu():
    while True:
        print("\n========= MENU =========")
        print("1. Thêm nhân viên")
        print("2. Hiển thị danh sách")
        print("3. Tìm kiếm")
        print("4. Quản lý lương")
        print("5. Quản lý dự án")
        print("6. Đánh giá hiệu suất")
        print("7. Quản lý nhân sự")
        print("8. Thống kê")
        print("9. Thoát")

        choice = input("Chọn: ")

        # =============================
        # 1. THÊM NHÂN VIÊN
        # =============================
        if choice == "1":
            emp_id = int(input("ID: "))
            name = input("Tên: ")
            salary = float(input("Lương: "))
            company.add_employee(Employee(emp_id, name, salary))

        # =============================
        # 2. HIỂN THỊ
        # =============================
        elif choice == "2":
            for e in company.employees.values():
                print(e)

        # =============================
        # 3. TÌM KIẾM
        # =============================
        elif choice == "3":
            emp_id = int(input("Nhập ID: "))
            emp = company.get_employee(emp_id)
            print(emp if emp else "Không tìm thấy")

        # =============================
        # 4. QUẢN LÝ LƯƠNG
        # =============================
        elif choice == "4":
            print("a. Tổng lương")
            print("b. Top 3 lương cao")
            sub = input("Chọn: ")

            if sub == "a":
                total = sum(e.calculate_salary() for e in company.employees.values())
                print("Tổng lương:", total)

            elif sub == "b":
                top = sorted(company.employees.values(),
                             key=lambda e: e.calculate_salary(),
                             reverse=True)[:3]
                for e in top:
                    print(e)

        # =============================
        # 5. QUẢN LÝ DỰ ÁN (🔥 thêm mới)
        # =============================
        elif choice == "5":
            print("a. Thêm NV vào dự án")
            print("b. Xóa NV khỏi dự án")
            print("c. Xem dự án của NV")
            print("d. Sắp xếp theo số dự án")
            print("e. NV theo dự án")

            sub = input("Chọn: ")

            if sub == "a":
                emp_id = int(input("ID: "))
                project = input("Dự án: ")
                company.get_employee(emp_id).add_project(project)

            elif sub == "b":
                emp_id = int(input("ID: "))
                project = input("Dự án: ")
                company.get_employee(emp_id).remove_project(project)

            elif sub == "c":
                emp_id = int(input("ID: "))
                print(company.get_employee(emp_id).projects)

            elif sub == "d":
                result = company.sort_by_project_count()
                for e in result:
                    print(e)

            elif sub == "e":
                p = input("Tên dự án: ")
                result = company.employees_in_project(p)
                for e in result:
                    print(e)

        # =============================
        # 6. HIỆU SUẤT
        # =============================
        elif choice == "6":
            emp_id = int(input("ID: "))
            score = float(input("Điểm: "))
            company.get_employee(emp_id).performance = score

        # =============================
        # 7. NHÂN SỰ (🔥 thêm mới)
        # =============================
        elif choice == "7":
            print("a. Nghỉ việc")
            print("b. Giảm lương")

            sub = input("Chọn: ")

            if sub == "a":
                emp_id = int(input("ID: "))
                penalty = float(input("Đền bù: "))
                company.resign_employee(emp_id, penalty)

            elif sub == "b":
                emp_id = int(input("ID: "))
                amount = float(input("Giảm: "))
                company.decrease_salary(emp_id, amount)

        # =============================
        # 8. THỐNG KÊ
        # =============================
        elif choice == "8":
            print("Tổng nhân viên:", len(company.employees))

        elif choice == "9":
            break


seed_data()
menu()