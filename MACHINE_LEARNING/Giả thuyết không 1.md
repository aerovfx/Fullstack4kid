1. Giả thuyết không 1:
$𝐻_0: Tỷ lệ sống sót không phụ thuộc vào giới tính.
$H_a: Tỷ lệ sống sót phụ thuộc vào giới tính.
​
Bước kiểm tra giả thuyết:
Phân tích dữ liệu:

Tạo bảng chéo giữa Sex và Survived.
Tính tỷ lệ sống sót theo giới tính.
Thực hiện kiểm định Chi-square:

Sử dụng kiểm định Chi-square để kiểm tra mối quan hệ giữa giới tính và khả năng sống sót.
# Đây là mã lệnh trong Python

```python
from scipy.stats import chi2_contingency

crosstab = pd.crosstab(df['Sex'], df['Survived'])
chi2, p, dof, expected = chi2_contingency(crosstab)
print(f"P-value = {p}")
if p < 0.05:
    print("Bác bỏ giả thuyết không: Tỷ lệ sống sót có phụ thuộc vào giới tính.")
else:
    print("Không đủ bằng chứng bác bỏ giả thuyết không: Tỷ lệ sống sót không phụ thuộc vào giới tính.")

```