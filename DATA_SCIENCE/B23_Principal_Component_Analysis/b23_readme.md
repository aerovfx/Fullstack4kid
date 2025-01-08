```markdown
# Principal Component Analysis (PCA)

Principal Component Analysis (PCA) là một kỹ thuật giảm chiều dữ liệu được sử dụng để giảm số lượng biến đầu vào trong một tập dữ liệu, đồng thời giữ lại càng nhiều thông tin càng tốt.

## Table of Contents
- [1. Giới thiệu](#1-giới-thiệu)
- [2. Chuẩn bị dữ liệu](#2-chuẩn-bị-dữ-liệu)
- [3. Áp dụng PCA](#3-áp-dụng-pca)
- [4. Trực quan hóa kết quả](#4-trực-quan-hóa-kết-quả)
- [5. Ứng dụng thực tế](#5-ứng-dụng-thực-tế)
- [6. Kết luận](#6-kết-luận)

## 1. Giới thiệu
Principal Component Analysis (PCA) là một kỹ thuật giảm chiều dữ liệu được sử dụng để giảm số lượng biến đầu vào trong một tập dữ liệu, đồng thời giữ lại càng nhiều thông tin càng tốt. PCA hoạt động bằng cách tìm các trục chính (principal components) mà dữ liệu phân tán nhiều nhất.

## 2. Chuẩn bị dữ liệu
Trước khi áp dụng PCA, chúng ta cần chuẩn bị dữ liệu bằng cách xử lý các giá trị thiếu, mã hóa các đặc trưng không phải số và chuẩn hóa dữ liệu.

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Tải dữ liệu Titanic
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(url)

# Chọn các cột quan trọng
selected_features = ['Pclass', 'Sex', 'Age', 'Fare', 'SibSp', 'Parch']

# Xử lý dữ liệu bị thiếu
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Fare'].fillna(data['Fare'].median(), inplace=True)

# Mã hóa biến 'Sex'
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
X = data[selected_features]
X_scaled = scaler.fit_transform(X)
```

## 3. Áp dụng PCA
Sau khi chuẩn bị xong dữ liệu, chúng ta sẽ sử dụng PCA để giảm chiều dữ liệu xuống còn 2 chiều để có thể trực quan hóa dữ liệu.

```python
from sklearn.decomposition import PCA

# Áp dụng PCA
pca = PCA(n_components=2)
pca_components = pca.fit_transform(X_scaled)
```

## 4. Trực quan hóa kết quả
Sau khi giảm chiều dữ liệu bằng PCA, chúng ta có thể trực quan hóa kết quả bằng biểu đồ.

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Thêm kết quả PCA vào dữ liệu
data['PCA1'] = pca_components[:, 0]
data['PCA2'] = pca_components[:, 1]

# Vẽ biểu đồ phân cụm
plt.figure(figsize=(10, 6))
sns.scatterplot(x='PCA1', y='PCA2', hue='Pclass', data=data, palette='viridis', s=100)
plt.title("PCA of Titanic Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.show()
```

## 5. Ứng dụng thực tế
PCA có nhiều ứng dụng trong thực tế, bao gồm:
- Giảm chiều dữ liệu để trực quan hóa.
- Tăng tốc độ huấn luyện mô hình học máy.
- Loại bỏ nhiễu và cải thiện hiệu suất mô hình.

Trong bài toán Titanic, PCA có thể giúp giảm số lượng biến đầu vào, từ đó giúp trực quan hóa dữ liệu và phát hiện các mẫu (patterns) trong dữ liệu.

## 6. Kết luận
PCA là một kỹ thuật mạnh mẽ để giảm chiều dữ liệu, giúp trực quan hóa và cải thiện hiệu suất mô hình học máy. Trong bài toán Titanic, PCA có thể giúp giảm số lượng biến đầu vào, từ đó giúp trực quan hóa dữ liệu và phát hiện các mẫu (patterns) trong dữ liệu.
```