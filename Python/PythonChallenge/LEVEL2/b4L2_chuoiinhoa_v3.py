def convert_lines_to_uppercase():
    lines = []
    while True:
        s = input("Nhập chuỗi (nhập trống để kết thúc): ")
        if not s:
            break
        lines.append(s.upper())

input_filename = 'b4L2_INHOA.INP'
with open(input_filename, 'r') as file:
    lines = file.read().strip().split(',')
    
    
    # Ghi kết quả vào file .OUT
output_filename = "b4L2_INHOA.OUT"
with open(output_filename, 'w') as file:
    for sentence in lines:
        file.write(sentence + "\n")

    print("Đã ghi kết quả vào file", output_filename)

# Gọi hàm để thực thi chương trình
convert_lines_to_uppercase()