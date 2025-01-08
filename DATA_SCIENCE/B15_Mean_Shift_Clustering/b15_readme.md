# Mean Shift Clustering

Mean Shift Clustering là một thuật toán phân cụm không giám sát, được sử dụng để tìm các cụm trong dữ liệu mà không cần biết trước số lượng cụm.

## Table of Contents
- [1. Giới thiệu](#1-giới-thiệu)
- [2. Nguyên lý hoạt động](#2-nguyên-lý-hoạt-động)
- [3. Tham số của Mean Shift](#3-tham-số-của-mean-shift)
- [4. Đánh giá mô hình Mean Shift](#4-đánh-giá-mô-hình-mean-shift)
- [5. Ứng dụng thực tế](#5-ứng-dụng-thực-tế)

## 1. Giới thiệu
Mean Shift Clustering là một thuật toán phân cụm không giám sát, được sử dụng để tìm các cụm trong dữ liệu mà không cần biết trước số lượng cụm.

## 2. Nguyên lý hoạt động
Mean Shift hoạt động bằng cách:
- Di chuyển các điểm dữ liệu về phía trung tâm của các điểm lân cận mật độ cao.
- Lặp lại quá trình này cho đến khi các điểm hội tụ vào các cụm.

## 3. Tham số của Mean Shift
- Bandwidth: Bán kính lân cận để xác định các điểm lân cận mật độ cao.

## 4. Đánh giá mô hình Mean Shift
Đánh giá mô hình Mean Shift bằng cách xem xét các cụm được tạo ra và các điểm hội tụ.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets import make_blobs

# Tạo dữ liệu mẫu
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Ước lượng bandwidth
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=300)

# Áp dụng Mean Shift
mean_shift = MeanShift(bandwidth=bandwidth, bin_seeding=True)
labels = mean_shift.fit_predict(X)

# Vẽ biểu đồ phân cụm
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='plasma')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Mean Shift Clustering')
plt.show()


5. Ứng dụng thực tế
Mean Shift Clustering có nhiều ứng dụng trong thực tế, bao gồm:

Phân tích khách hàng trong lĩnh vực marketing.
Phân cụm các bài viết trong lĩnh vực xử lý ngôn ngữ tự nhiên.
Phân tích dữ liệu y tế để tìm ra các nhóm bệnh nhân có đặc điểm tương đồng.
Trong bài toán Titanic, Mean Shift có thể giúp phân nhóm hành khách dựa trên các đặc trưng như giới tính, tuổi, hạng vé và mức chi tiêu, từ đó phân tích các hành vi của hành khách và đưa ra các chiến lược cứu hộ và tiếp thị hiệu quả. ```