Những con kiến đi kiếm ăn hay về tổ thường tổ chức đi theo từng đoàn. Trong một lần nọ, có một doàn kiến gồm m on đi trên một nhánh cây và được đánh số thứ tự từ 1 đến n,
con kiến thức i có vận tốc di chuyển riêng là v_i và có khối lượng tương ứng là k_i (với i = 1,2,...,n). 
Theo lộ trình thì đoàn kiến sẽ đi tuần tự theo số thứ tự để đi kiếm thức ăn. Tuy nhiên trên lộ trình đi có một cành cây không được đảm bảo để đoàn kiến qua lại thoải mái.
Được biết rằng nếu như tổng khối lượng của các con kiến cùng trên cành cây đó vượt qúa khối lượng m thì cành cây có thể bị cong hoặc gãy làm cho các con kiến có thể bị rơi xuống đất (tức là trong cùng một thời điểm thì tổng khối lượng các con kiến trên cành cây đó không được vượt quá khối lương m).
Chính vì thế khi qua cành cây các con kiến phải chia đoàn thành các nhóm sao cho tổng khối lượng của mỗi một nhóm không quá m, các con kiến trong từng nhóm hay các nhóm với nhau cũng phải tuân theo thứ tự ban đầu. Thêm vào đó nữa là các nhóm phải đi tuàn tự, nghĩa là nhóm thứ i chỉ được đi qua khi mà toàn bộ kiến của nhóm thứ i -1 đi qua được cành cây đó. Vận tốc đi của mỗi nhóm là hoàn toàn khác nhau và phụ thuộc vào con kiến có tốc độ chậm nhất. Nhiệm vụ của đoàn kiến là phải đi qua cành cây đó gây ra.
Yêu cầu: Hãy sắp xếp đoàn kiến đi sao cho hợp lý để tổng thời gian qua cảnh cây đó là nhỏ nhất.
Dữ liệu: Vào từ file GROUANTS.INP
-Dòng đầu là 3 số nguyên dương n, m , l với:
n là số lượng kiến của đoàn.
m là tải trọng tối đa của cành cây (tổng khối lượng tối đa của nhóm kiến có thể cùng qua được cành cây)
l là độ dài của cành cây ( 1 <= n < = 1000; 1 <= m, l <= 100).
Trong  n dòng sau, dòng thứ i là 2 số nguyên dương k_i và v_i thể hiện cho khối lượng và vận tốc của con kiến thứ i (1 <= k_i, v_i <= 100 với i = 1, 2, ...,n)
Kết quả: Ghi vào file GROUANTS.OUT tổng thời gian nhỏ nhất để đoàn kiến qua được cành cây (lấy 2 số phần thập phân)

Ví dụ:
-----------------------------------------------
| GROUANTS.INP       | GROUANTS.OUT           |
| 6 10 10            |20.00                   |  
| 3 5                |                        |  
| 6 2                |                        | 
| 5 2                |                        |  
| 7 1                |                        |  
| 1 5                |                        |
| 2 7                |                        |  
-----------------------------------------------
Ràng buộc dữ liệu:
-Có 60% test có n <= 10^6
-Có 40% test khác có n <= 10^(12)
