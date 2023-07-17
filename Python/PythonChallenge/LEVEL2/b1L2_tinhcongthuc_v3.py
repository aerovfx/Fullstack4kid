import math

def tinh_cong_thuc(gia_tri_d):
    c = 50
    h = 30
    result = []
    for d in gia_tri_d:
        value = [str(int(round(math.sqrt(2*c*float(val)/h)))) for val in d.split(',')]
        result.append(','.join(value))
    return result

    
    
input_file = 'b1L2_TINHSO_NHIEUDONG.INP'
output_file = 'b1L2_TINHSO_NHIEUDONG.OUT'


with open(input_file, 'r') as file:
    lines = file.readlines()

results = tinh_cong_thuc(lines)

with open(output_file, 'w') as file:
    file.write('\n'.join(results))

print("Đã tạo ra file kết quả:", output_file)

