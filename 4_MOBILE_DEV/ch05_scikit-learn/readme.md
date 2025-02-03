# Giới thiệu về Scikit-learn

Scikit-learn là một thư viện mã nguồn mở mạnh mẽ dành cho học máy trong Python. Nó cung cấp một loạt các công cụ hiệu quả để khai thác và phân tích dữ liệu, bao gồm các thuật toán phân loại, hồi quy, cụm, và giảm chiều dữ liệu. Scikit-learn được xây dựng trên các thư viện NumPy, SciPy và matplotlib, giúp dễ dàng tích hợp vào các dự án khoa học dữ liệu và học máy.

## Các tính năng chính của Scikit-learn

- **Phân loại (Classification)**: Xác định danh mục mà một mẫu thuộc về.
- **Hồi quy (Regression)**: Dự đoán một giá trị liên tục.
- **Cụm (Clustering)**: Tự động nhóm các mẫu tương tự nhau.
- **Giảm chiều dữ liệu (Dimensionality Reduction)**: Giảm số lượng biến ngẫu nhiên để đơn giản hóa mô hình.
- **Tiền xử lý dữ liệu (Data Preprocessing)**: Chuẩn hóa và biến đổi dữ liệu.

## Cài đặt

Bạn có thể cài đặt Scikit-learn thông qua pip:

```bash
pip install scikit-learn
```

## Ví dụ cơ bản

Dưới đây là một ví dụ cơ bản về cách sử dụng Scikit-learn để huấn luyện một mô hình phân loại:

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Tải dữ liệu mẫu
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Khởi tạo và huấn luyện mô hình
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# Dự đoán và đánh giá mô hình
y_pred = clf.predict(X_test)
print(f"Độ chính xác: {accuracy_score(y_test, y_pred)}")
```

Scikit-learn là một công cụ tuyệt vời cho các nhà khoa học dữ liệu và kỹ sư học máy, giúp họ nhanh chóng xây dựng và triển khai các mô hình học máy hiệu quả.