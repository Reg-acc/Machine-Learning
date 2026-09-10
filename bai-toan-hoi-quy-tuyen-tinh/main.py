import os
import numpy as np
import pandas as pd

def main():
    print("=== GIẢI BÀI TOÁN HỒI QUY TUYẾN TÍNH THUẦN TÚY ===\n")
    
    # 1. Đọc dữ liệu bài toán
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, "du_lieu.csv")
    df = pd.read_csv(file_path)
    
    X_raw = df["X"].values
    Y = df["Y"].values.reshape(-1, 1)
    
    # 2. Xây dựng ma trận X (thêm cột 1 cho hằng số beta_0)
    # X_mat = [1, x_i]
    X_mat = np.column_stack((np.ones(len(X_raw)), X_raw))
    
    print("Ma trận X (bao gồm cột hằng số 1):")
    print(X_mat)
    print("\nMa trận Y:")
    print(Y)
    
    # 3. Tính toán nghiệm theo công thức OLS: beta = (X^T * X)^(-1) * X^T * Y
    XT = X_mat.T
    XT_X = np.dot(XT, X_mat)
    XT_X_inv = np.linalg.inv(XT_X)
    XT_Y = np.dot(XT, Y)
    
    beta = np.dot(XT_X_inv, XT_Y)
    
    beta_0 = beta[0][0]
    beta_1 = beta[1][0]
    
    # 4. Hiển thị kết quả lời giải
    print("\n=== KẾT QUẢ TÍNH TOÁN HỆ SỐ ===")
    print(f"Hệ số tự do (beta_0)  : {beta_0:.4f}")
    print(f"Hệ số góc (beta_1)   : {beta_1:.4f}")
    print(f"\n=> Phương trình đường thẳng hồi quy: Y = {beta_0:.4f} + {beta_1:.4f} * X")

if __name__ == "__main__":
    main()