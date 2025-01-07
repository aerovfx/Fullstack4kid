Trong bài học trước, chúng ta đã tìm hiểu cách vẽ các bản đồ một cách thủ công, tức là vẽ chúng một cách trực tiếp.
Tuy nhiên, có một framework rất hữu ích trong Python gọi là Matplotlib mà chúng ta có thể sử dụng để làm điều tương tự, tức là chúng ta có thể vẽ đồ thị bằng Matplotlib.
Vậy bước đầu tiên tôi sẽ làm là nhập thư viện này vào.
Nếu bạn chưa thử, đầu tiên hãy thử nhập thư viện này.
Gõ matplotlib.
Nếu bạn gặp lỗi nhập khẩu, hãy chắc chắn rằng bạn đã viết đúng chính tả, nếu không có, có thể thư viện này chưa được cài đặt trên hệ thống của bạn.
Tất cả những gì bạn cần làm là vào dòng lệnh.
Để tôi tạm dừng Jupyter Notebook một chút, bạn chỉ cần gõ pip install matplotlib.
Sau đó bạn chỉ cần làm như vậy và matplotlib sẽ hoạt động trên hệ thống của bạn.
Bây giờ hãy khởi động lại Jupyter Notebooks.
Tốt, chúng ta muốn sử dụng một cái gọi là pyplot.
Vì vậy, tôi sẽ viết from matplotlib import và tôi sẽ thay tên nó.
Thực ra tôi muốn gọi nó là plt vì mỗi lần viết pyplot thì khá là dài dòng.
Vậy, sau một thời gian, bạn sẽ trở nên lười biếng với những thứ như thế này, vì vậy dùng plt sẽ dễ dàng hơn.
Vậy nên tôi sẽ nhập matplotlib.pyplot như là plt.
Đảm bảo rằng kernel đã kết nối.
Rồi, giờ chúng ta đã nhập matplotlib dưới tên plt.
Bây giờ chúng ta sẽ tạo một đồ thị.
Tôi sẽ tạo ra một biến x và lưu trữ nó trong một danh sách.
Tôi sẽ bắt đầu với một danh sách đơn giản như [1, 2, 3, 4, 5].
Và tôi cũng sẽ làm tương tự với y.
[1, 2, 3, 4, 5].
Như bạn nhớ, x là trục hoành và là biến độc lập.
Còn y là trục tung và là biến phụ thuộc.
Bây giờ tôi sẽ chạy nó.
Chúng ta đã lưu trữ dữ liệu xong và giờ rất dễ dàng để vẽ đồ thị này.
Chỉ cần gọi plt.plot(x, y).
Sau đó, chỉ cần gọi plt.show() và sẽ thấy đồ thị đã được vẽ đẹp mắt.
Một điều tôi muốn làm là thêm nhãn cho các trục để chúng ta có thể nhìn rõ trục nào đại diện cho cái gì.
Vậy tôi sẽ thêm vào trên đây, tôi sẽ viết plt.xlabel và thêm tên cho trục x, chẳng hạn là X.
Sau đó làm tương tự cho trục y, tôi sẽ gọi plt.ylabel và thêm tên là Y.
Cuối cùng, tôi sẽ thêm một tiêu đề cho đồ thị bằng cách sử dụng plt.title để mô tả đồ thị, ví dụ: "Graph to show the effect of X on Y".
Trong thực tế, x và y sẽ có tên gọi chính xác hơn, và chúng ta sẽ cùng xem qua một ví dụ thực tế.
Bây giờ, tôi muốn xem tác động của các quảng cáo Facebook.
Giả sử tôi muốn xem ảnh hưởng của việc chi tiền vào quảng cáo Facebook như thế nào đến số lượng doanh thu.
Vậy đầu tiên, cần xác định biến độc lập và biến phụ thuộc.
Cái mà chúng ta thay đổi sẽ là biến độc lập, tức là số tiền chi cho quảng cáo, và biến phụ thuộc sẽ là số lượng doanh thu đạt được.
Thay vì gọi danh sách này là x, tôi sẽ gọi nó là ad_budget và cho vào danh sách [1, 10, 50, 100, 1000].
Sau đó, tôi sẽ gọi danh sách thứ hai là sales và điền các số liệu doanh thu tương ứng như sau: [1, 10, 100, 1000, 5000].
Giờ chúng ta đã có hai trục: trục x là ad_budget và trục y là sales.
Hãy vẽ đồ thị này ra.
Chúng ta sẽ gọi plt.plot(ad_budget, sales) để vẽ đồ thị.
Chưa có nhãn hay tiêu đề gì, vì vậy chúng ta sẽ thêm vào.
Gọi plt.xlabel("Amount spent on Facebook ads (in pounds)") để chỉ rõ trục x là chi phí quảng cáo.
Và plt.ylabel("Sales (in pounds)") cho trục y là doanh thu.
Cuối cùng, thêm tiêu đề cho đồ thị với plt.title("Graph to show the effects of ad budgeting on sales").
Chạy lệnh plt.show() để hiển thị đồ thị.
Vậy là xong, đồ thị của chúng ta trông đẹp mắt hơn nhiều.
Đây là cách bạn có thể vẽ đồ thị của riêng mình.
Hãy thử tạo một bộ dữ liệu và vẽ đồ thị bằng Matplotlib, rồi tôi sẽ gặp bạn trong bài học tiếp theo.

