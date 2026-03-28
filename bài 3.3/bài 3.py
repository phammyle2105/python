import time

year = time.localtime().tm_year

birth_year = int(input("Nhap nam sinh: "))
if birth_year > 0 and birth_year <= year:
    age = year - birth_year
    print(f"Nam sinh {birth_year}, vay ban {age} tuoi")
else:
    print("Nam sinh khong hop le")