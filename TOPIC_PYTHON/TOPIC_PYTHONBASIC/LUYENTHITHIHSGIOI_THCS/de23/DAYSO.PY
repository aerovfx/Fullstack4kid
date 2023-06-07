def min_max_average():
    # Mở file input để đọc dãy số
    with open("DAYSO.INP", "r") as file_input:
        lines = file_input.readlines()

    with open("DAYSO.OUT", "w") as file_output:
        for line in lines:
            numbers = [int(num) for num in line.split()]

            n = len(numbers)

            # Khởi tạo biến lưu giá trị nhỏ nhất, lớn nhất và tổng các phần tử
            min_value = None
            max_value = None
            total = 0

            for num in numbers:
                # Cập nhật giá trị nhỏ nhất và lớn nhất
                if min_value is None or num < min_value:
                    min_value = num
                if max_value is None or num > max_value:
                    max_value = num

                # Cộng giá trị vào tổng
                total += num

            # Tính giá trị trung bình
            average = total / n

            # Ghi kết quả vào file output
            file_output.write(f"{min_value} {max_value} {average}\n")

min_max_average()
