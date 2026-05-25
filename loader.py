import sqlite3
import pandas as pd
from datetime import datetime

def load_to_sql(df, db_name="marketing_database.db"):
    """
    Menyimpan DataFrame yang sudah bersih ke dalam tabel SQL.
    """
    print(f"[{datetime.now()}] Membuka koneksi ke database SQL ({db_name})...")
    
    # Membuat koneksi ke database (otomatis membuat file .db jika belum ada)
    conn = sqlite3.connect(db_name)
    
    # Menyimpan DataFrame ke tabel bernama 'campaign_metrics'
    # if_exists='append' berarti data baru akan ditambahkan ke bawah data lama
    df.to_sql('campaign_metrics', conn, if_exists='append', index=False)
    
    print(f"[{datetime.now()}] Sukses! Data berhasil dimuat ke tabel 'campaign_metrics'.")
    
    # Menutup koneksi database
    conn.close()

if __name__ == "__main__":
    print("Modul loader siap digunakan.")