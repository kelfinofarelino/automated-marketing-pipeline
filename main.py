from extractor import fetch_marketing_data
from transformer import clean_and_transform
from loader import load_to_sql

def run_pipeline():
    print("=== MEMULAI AUTOMATED MARKETING PIPELINE ===")
    
    # Tahap 1: EXTRACT (Tarik Data)
    # Di dunia nyata, ini bisa dipanggil berkali-kali untuk platform yang berbeda
    raw_data = []
    platforms = ["Facebook Ads", "Google Ads", "TikTok Ads"]
    
    for platform in platforms:
        data = fetch_marketing_data(platform)
        # Menambahkan nama platform ke dalam data
        data['platform'] = platform 
        raw_data.append(data)
        
    # Tahap 2: TRANSFORM (Bersihkan & Hitung Metrik)
    cleaned_df = clean_and_transform(raw_data)
    
    # Tahap 3: LOAD (Simpan ke Database SQL)
    load_to_sql(cleaned_df)
    
    print("=== PIPELINE SELESAI ===")

if __name__ == "__main__":
    run_pipeline()