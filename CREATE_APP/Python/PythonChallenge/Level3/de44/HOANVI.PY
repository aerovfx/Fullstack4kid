# Định nghĩa hàm để tìm dãy nghịch thế T của hoán vị P.
def tim_nghich_the(P):
    # Độ dài của hoán vị P, tức số phần tử trong hoán vị.
    n = len(P)

    # Khởi tạo một list T với n phần tử và giá trị mỗi phần tử là 0.
    # T list này sẽ lưu dãy nghịch thế của hoán vị P.
    T = [0] * n

    # Duyệt qua từng phần tử i trong hoán vị P.
    for i in range(n):
        # Duyệt qua các phần tử j từ i+1 đến n-1 trong hoán vị P.
        # Chúng ta chỉ quan tâm các phần tử nằm bên phải của phần tử i,
        # vì nghịch thế của phần tử i được tính bằng số lượng các phần tử lớn hơn nó nằm bên trái.
        for j in range(i + 1, n):
            # Nếu phần tử j có giá trị nhỏ hơn phần tử i, tăng giá trị T[i] lên 1.
            # Điều này đồng nghĩa với việc tìm thấy một phần tử nhỏ hơn i nằm bên phải của nó.
            if P[j] < P[i]:
                T[i] += 1

    # Trả về dãy nghịch thế T của hoán vị P.
    return T

# Nhập số n từ người dùng.
n = int(input("Nhập số n: "))

# Nhập hoán vị P từ người dùng, và chuyển chuỗi thành list các số nguyên.
P_str = input("Nhập hoán vị P, các số cách nhau bằng dấu cách: ")
P = list(map(int, P_str.split()))

# Tìm và in ra dãy nghịch thế T của hoán vị P.
T = tim_nghich_the(P)
print("Dãy nghịch thế T:", T)
