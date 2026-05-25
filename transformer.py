import pandas as pd
from datetime import datetime

def clean_and_transform(raw_data):
    """
    Fungsi untuk membersihkan data mentah dan menambahkan metrik kalkulasi.
    """
    print(f"[{datetime.now()}] Memulai transformasi data...")
    
    # 1. Konversi data mentah (List of Dictionaries) menjadi Pandas DataFrame
    df = pd.DataFrame(raw_data)
    
    # 2. Data Cleaning: Mengisi nilai kosong (NaN) pada kolom 'clicks' dengan angka 0
    # Ini penting karena data dari API kadang bolong/hilang
    df['clicks'] = df['clicks'].fillna(0)
    
    # 3. Feature Engineering: Menghitung metrik CTR (Click-Through Rate)
    # Rumus: (Clicks / Impressions) * 100
    df['ctr_percentage'] = (df['clicks'] / df['impressions']) * 100
    
    # 4. Formatting: Membulatkan angka persentase menjadi 2 angka di belakang koma
    df['ctr_percentage'] = df['ctr_percentage'].round(2)
    
    print("Transformasi berhasil! Berikut preview data yang sudah bersih:")
    print("-" * 50)
    print(df)
    print("-" * 50)
    
    return df

if __name__ == "__main__":
    # Ini adalah simulasi data mentah yang didapat dari extractor.py sebelumnya
    # Perhatikan ada data 'None' untuk menyimulasikan data yang kotor/bolong
    mock_raw_data = [
        {"campaign_id": "CMP-001", "platform": "Instagram", "impressions": 15000, "clicks": 350},
        {"campaign_id": "CMP-002", "platform": "Facebook", "impressions": 20000, "clicks": None}, 
        {"campaign_id": "CMP-003", "platform": "Google Ads", "impressions": 5000, "clicks": 120}
    ]
    
    # Menjalankan fungsi transformasi
    clean_and_transform(mock_raw_data)