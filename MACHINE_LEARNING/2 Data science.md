3 In this section: Data science
Trong phần này, bạn sẽ học cách tận dụng sức mạnh của dữ liệu lớn để trích xuất thông tin, nhận diện các mẫu dữ liệu và thực hiện một loạt các trực quan hóa.
Đây là một bước rất thú vị đối với bạn, khi bạn chuyển từ phát triển web, sử dụng Python, HTML, JavaScript, CSS sang một lĩnh vực mới, đó là khoa học dữ liệu và học máy.
Tôi rất hào hứng được chỉ cho bạn những kiến thức cơ bản trong phần này, và tôi mong chờ sẽ gặp lại bạn trong bài giảng tiếp theo.

Hãy cùng bước vào một bước thú vị trong lĩnh vực khoa học dữ liệu.

Chúng ta sẽ nói về công việc cơ bản mà một nhà khoa học dữ liệu thực hiện và các ví dụ khác nhau về cách chúng ta ứng dụng khoa học dữ liệu.

Trong một bài giảng trước, chúng ta đã nói về những điều cơ bản mà nhà khoa học dữ liệu làm, ví dụ như xác định phạm vi của một dự án, thu thập dữ liệu, cách họ tiếp cận và chuẩn bị dữ liệu, cách họ khám phá dữ liệu qua phân tích dữ liệu khám phá (Exploratory Data Analysis), và cuối cùng là trực quan hóa và truyền đạt thông tin cho tất cả các bên liên quan trong dự án.

Bây giờ, hãy cùng đi qua từng bước một.

### Xác định phạm vi

Việc xác định phạm vi là rất quan trọng vì nó giúp bạn truyền đạt rõ ràng phạm vi và kết quả của dự án tới tất cả các bên liên quan. Điều này thực sự sẽ giúp bạn vượt trội so với những người khác khi ứng tuyển vào các vị trí liên quan.

Khi nói đến phạm vi, tôi đang đề cập đến các mục tiêu kinh doanh hoặc mục tiêu của bất kỳ nhóm nào mà bạn đang làm việc cùng. Vậy, mục tiêu của bạn là gì? Ngoài ra, kết quả dự kiến là gì?

Ví dụ, giả sử bạn muốn làm khoa học dữ liệu về dự báo doanh thu cho một công ty, và kết quả dự kiến của bạn là dự đoán doanh thu, nhưng có thể thêm cả những cái nhìn sâu sắc về xu hướng bán hàng nói chung.

Tiếp theo, bạn cần xác định cách tiếp cận nhiệm vụ. Khi bạn đã thực hiện vài dự án khoa học dữ liệu, bạn sẽ đủ kinh nghiệm để xác định cách bạn dự định tiếp cận nhiệm vụ này. Bạn sẽ sử dụng phương pháp nào, ví dụ như các phương pháp phân tích hay mô hình hóa nào?

Cuối cùng, bạn cần xem xét các bên liên quan liên quan đến dự án. Trong phần xác định phạm vi, bạn cần thảo luận về loại báo cáo mà các bên liên quan yêu cầu, chẳng hạn như liệu bạn có cần cung cấp biểu đồ, đồ thị hay không, và các mốc thời gian hay hạn chót sẽ như thế nào.

### Thu thập dữ liệu

Thu thập dữ liệu là bước quan trọng trong quá trình khoa học dữ liệu. Bạn có thể thu thập dữ liệu từ các nhà cung cấp dữ liệu (data brokers), những công ty bên thứ ba chuyên cung cấp dữ liệu lớn.

Ngoài ra, bạn có thể thu thập dữ liệu nội bộ từ các công ty hoặc tổ chức. Một số công ty tạo khảo sát để thu thập dữ liệu từ người dùng mà họ cần.

Dữ liệu cũng có thể được thu thập từ các mạng cảm biến. Ví dụ, nếu bạn muốn làm một dự án về dữ liệu lớn liên quan đến các vụ cháy rừng, bạn có thể thiết lập cảm biến tại một khu vực, chẳng hạn như California, nơi có nhiều vụ cháy rừng. Các cảm biến có thể đo nhiệt độ đất, độ ẩm, hàm lượng nước trong đất, và bạn có thể so sánh dữ liệu đó với thông tin về các vụ cháy rừng để thu thập dữ liệu của mình.

### Chuẩn bị dữ liệu

Một công việc lớn mà nhiều nhà khoa học dữ liệu dành phần lớn thời gian cho là chuẩn bị và làm sạch dữ liệu, thay vì chỉ xây dựng bộ dữ liệu huấn luyện hay làm việc với các thuật toán học máy. Đây là lý do tôi muốn nhấn mạnh "chuẩn bị dữ liệu" trong phần này.

Mặc dù khoa học dữ liệu có thể là một lĩnh vực rất thú vị, nhưng có rất nhiều công đoạn chuẩn bị cần thực hiện và bạn sẽ quen với việc này khá nhanh. 

**Công việc chuẩn bị dữ liệu bao gồm:**
- **Chuyển đổi dữ liệu**: Bạn cần chuyển đổi dữ liệu thành định dạng phù hợp để có thể đưa vào các mô hình học máy.
- **Điền các giá trị bị thiếu**: Ví dụ, nếu bạn thu thập dữ liệu từ các cuộc khảo sát và một số người không điền đầy đủ các trường yêu cầu, bạn sẽ cần phải xử lý các giá trị thiếu này.
- **Sửa lỗi chính tả và thông tin sai lệch**: Ví dụ, nếu ai đó nhập sai một giá trị, như viết tuổi là "40" sai chính tả hoặc nhầm lẫn khi nhập giới tính vào trường "tuổi".
- **Xử lý ngoại lệ**: Dữ liệu có thể có những giá trị không hợp lệ hoặc bị sai lệch, và điều này có thể ảnh hưởng đến tính chính xác của phân tích. Việc loại bỏ hoặc xử lý các ngoại lệ này rất quan trọng.

### Phân tích dữ liệu khám phá (Exploratory Data Analysis - EDA)

Phân tích dữ liệu khám phá là phần thú vị trong khoa học dữ liệu. Các nhóm khoa học dữ liệu sẽ sử dụng EDA để chọn ra các đặc trưng quan trọng nhất trong dữ liệu giúp đạt được mục tiêu.

Bạn sẽ sử dụng EDA để chọn các đặc trưng quan trọng và có thể trình bày những phát hiện này cho các bên liên quan, chẳng hạn như: "Chúng tôi đã phát hiện rằng đặc trưng X và đặc trưng Y có sự tương quan cao với mục tiêu Z của chúng tôi."

**Ví dụ**: Nếu bạn đang làm dự báo doanh thu cho một công ty kem, bạn có thể nhận thấy rằng nhiệt độ ngoài trời và thời gian trong năm có mối tương quan cao với doanh số bán kem.

Một phần của EDA là **chọn đặc trưng**. Ví dụ, nếu bạn có dữ liệu về nhiều yếu tố như thời gian trong năm, nhiệt độ, khoảng cách từ trường học, và những yếu tố không liên quan như số lượng cây cối trong khu vực, bạn có thể chọn loại bỏ các đặc trưng không hữu ích đối với mô hình học máy của bạn.

**Ví dụ khác**: Khi dự đoán giá nhà, số phòng và khoảng cách từ trường học là những đặc trưng hữu ích, nhưng khoảng cách từ quốc gia Iceland có thể không có liên quan đến giá nhà.

Visualizations (Trực quan hóa) là một phần không thể thiếu trong EDA. Chúng giúp bạn dễ dàng nhận thấy các mối tương quan và trực quan hóa các mối quan hệ trong dữ liệu, và cũng rất hữu ích khi bạn cần trình bày những phát hiện này cho các bên liên quan.

### Tóm tắt

Bây giờ, chúng ta đã đi qua các bước cơ bản trong khoa học dữ liệu. Hãy chuẩn bị sẵn sàng để bạn có thể bắt đầu thực hành và làm khoa học dữ liệu ngay hôm nay!
