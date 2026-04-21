class Company:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp):
        self.employees[emp.emp_id] = emp

    def get_employee(self, emp_id):
        return self.employees.get(emp_id)

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]

    # ===============================
    # 🔥 1. Sắp xếp theo số dự án
    # ===============================
    def sort_by_project_count(self):
        return sorted(self.employees.values(),
                      key=lambda e: e.project_count(),
                      reverse=True)

    # ===============================
    # 🔥 2. Nhân viên theo dự án
    # ===============================
    def employees_in_project(self, project):
        return [e for e in self.employees.values() if project in e.projects]

    # ===============================
    # 🔥 3. Nghỉ việc + đền bù
    # ===============================
    def resign_employee(self, emp_id, penalty):
        emp = self.get_employee(emp_id)
        if emp:
            emp.active = False
            emp.contract_penalty = penalty
            print(f"{emp.name} đã nghỉ việc. Đền bù: {penalty}")

    # ===============================
    # 🔥 4. Giảm lương
    # ===============================
    def decrease_salary(self, emp_id, amount):
        emp = self.get_employee(emp_id)
        if emp:
            emp.base_salary -= amount
            print(f"Đã giảm {amount} lương của {emp.name}")