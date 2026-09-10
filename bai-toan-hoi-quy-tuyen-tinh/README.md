# Bài Toán Hồi Quy Tuyến Tính (Linear Regression Problem)

Chương trình giải bài toán tìm đường thẳng hồi quy tối ưu đi qua tập hợp các điểm dữ liệu $(X, Y)$ bằng **Phương pháp Bình phương Tối thiểu (OLS)** sử dụng đại số tuyến tính.

## Phát biểu bài toán

Cho tập dữ liệu gồm $n$ điểm $(x_i, y_i)$. Tìm đường thẳng $Y = \beta_0 + \beta_1 X$ sao cho tổng bình phương các sai số là nhỏ nhất:

$$\min_{\beta_0, \beta_1} \sum_{i=1}^{n} (y_i - (\beta_0 + \beta_1 x_i))^2$$

## Công thức nghiệm ma trận

Dạng ma trận của bài toán: $Y = X\beta + \epsilon$

Véc-tơ hệ số $\beta = \begin{bmatrix} \beta_0 \\ \beta_1 \end{bmatrix}$ được tính bằng công thức:

$$\beta = (X^T X)^{-1} X^T Y$$

Trong đó:
- $X$ là ma trận kích thước $n \times 2$ với cột đầu tiên chứa toàn số 1.
- $Y$ là véc-tơ cột kích thước $n \times 1$ chứa các giá trị biến phụ thuộc.

## Yêu cầu cài đặt
Cài đặt thư viện tính toán số học:

```bash
pip install numpy pandas