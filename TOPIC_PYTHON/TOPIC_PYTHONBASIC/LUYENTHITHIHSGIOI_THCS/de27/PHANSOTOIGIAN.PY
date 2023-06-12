def simplify_fraction(fraction):
    # Tách tử số và mẫu số từ chuỗi phân số
    tu, mau = fraction.split('/')
    tu = int(tu)
    mau = int(mau)

    # Tìm ước chung lớn nhất (UCLN) của tử số và mẫu số
    ucln = find_ucln(tu, mau)

    # Chia tử số và mẫu số cho UCLN để đưa về dạng tối giản
    simplified_numerator = tu // ucln
    simplified_denominator = mau // ucln

    # Trả về chuỗi dạng tối giản của phân số
    simplified_fraction = str(simplified_numerator) + '/' + str(simplified_denominator)
    return simplified_fraction

def find_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Nhập chuỗi phân số
fraction_string = input("Nhập chuỗi phân số: ")

# Tối giản phân số và in ra kết quả
simplified_fraction = simplify_fraction(fraction_string)
print("Dạng tối giản của phân số:", simplified_fraction)
