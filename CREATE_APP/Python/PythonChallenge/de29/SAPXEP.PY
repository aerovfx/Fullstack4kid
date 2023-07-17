danh_sach = [7,90,2,15,3,35, 76, 8, 0, 56]
def sap_xep(a):
    ch7 = []
    ch5 = []
    other_nums = []
    for i in range(len(a)):
        num = a[i]
        if num % 7 == 0:
            ch7.append(num)
        elif num%5 == 0:
            ch5.append(num)
        else:
            other_nums.append(num)

    sorted_nums = sorted(ch7) + sorted(other_nums) + sorted(ch5)
    return sorted_nums
sap_xep(danh_sach)
print(sap_xep(danh_sach))