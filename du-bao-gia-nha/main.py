import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

def main():
    # 1. Đọc dữ liệu
    print("Đang tải dữ liệu...")
    df = pd.read_csv("du_lieu.csv")
    
    # 2. Phân chia đặc trưng (X) và mục tiêu dự báo (y)
    X = df[["DienTich", "PhongNgu", "PhongTam", "TuoiNha"]]
    y = df["GiaNha"]
    
    # 3. Chia tập huấn luyện và tập kiểm tra (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # 4. Huấn luyện mô hình
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("Đã hoàn tất huấn luyện mô hình.")
    
    # 5. Đánh giá mô hình
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Sai số tuyệt đối trung bình (MAE): {mae:,.0f} VNĐ")
    print(f"Độ chính xác (R2 Score): {r2:.2f}")
    
    # 6. Dự báo cho một ngôi nhà mới
    # Ví dụ: Diện tích = 80m2, 2 phòng ngủ, 2 phòng tắm, tuổi nhà = 3 năm
    nha_moi = pd.DataFrame([[80, 2, 2, 3]], columns=["DienTich", "PhongNgu", "PhongTam", "TuoiNha"])
    gia_du_bao = model.predict(nha_moi)[0]
    print(f"\nGiá dự báo cho căn nhà 80m2 (2 PN, 2 PT, 3 năm tuổi): {gia_du_bao:,.0f} VNĐ")

if __name__ == "__main__":
    main()