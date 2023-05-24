def convert_lines_to_uppercase(input_file, output_file):
    lines = []
    with open(input_file, 'r') as file:
        lines = file.readlines()

    lines = [line.strip().upper() for line in lines]

    with open(output_file, 'w') as file:
        file.write('\n'.join(lines))

# Nhập tên file đầu vào và đầu ra từ người dùng
input_file = input("Nhập tên file đầu vào: ")
output_file = input("Nhập tên file đầu ra: ")

# Gọi hàm để thực thi chương trình
convert_lines_to_uppercase(input_file, output_file)
