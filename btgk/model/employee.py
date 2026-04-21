class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary
        self.projects = []
        self.performance = 0
        self.active = True
        self.contract_penalty = 0

    def add_project(self, project):
        if project not in self.projects:
            self.projects.append(project)

    def remove_project(self, project):
        if project in self.projects:
            self.projects.remove(project)

    def project_count(self):
        return len(self.projects)

    def calculate_salary(self):
        return self.base_salary

    def __str__(self):
        return f"{self.emp_id} - {self.name} - Salary: {self.calculate_salary()} - Projects: {len(self.projects)}"