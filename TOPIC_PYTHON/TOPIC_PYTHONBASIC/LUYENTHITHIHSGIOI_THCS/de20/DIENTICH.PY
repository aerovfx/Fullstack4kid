import math

def calculate_square_area():
    side = float(input("Nhập độ dài cạnh hình vuông: "))
    area = side ** 2
    print("Diện tích hình vuông là:", area)

def calculate_circle_area():
    radius = float(input("Nhập bán kính hình tròn: "))
    area = math.pi * radius ** 2
    print("Diện tích hình tròn là:", area)

def calculate_triangle_area():
    base = float(input("Nhập độ dài cạnh đáy tam giác: "))
    height = float(input("Nhập chiều cao của tam giác: "))
    area = 0.5 * base * height
    print("Diện tích tam giác là:", area)

def calculate_rectangle_area():
    length = float(input("Nhập chiều dài hình chữ nhật: "))
    width = float(input("Nhập chiều rộng hình chữ nhật: "))
    area = length * width
    print("Diện tích hình chữ nhật là:", area)

def main():
    while True:
        print("\nBảng chọn lệnh:")
        print("1. Không làm gì hết và trở về màn hình soạn thảo.")
        print("2. Tính diện tích hình vuông.")
        print("3. Tính diện tích hình tròn.")
        print("4. Tính diện tích tam giác.")
        print("5. Tính diện tích hình chữ nhật.")

        choice = input("Chọn một lệnh (1-5): ")

        if choice == "1":
            break
        elif choice == "2":
            calculate_square_area()
        elif choice == "3":
            calculate_circle_area()
        elif choice == "4":
            calculate_triangle_area()
        elif choice == "5":
            calculate_rectangle_area()
        else:
            print("Lệnh không hợp lệ. Vui lòng chọn lại.")

main()
