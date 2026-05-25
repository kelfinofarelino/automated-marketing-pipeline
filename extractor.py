import json
from datetime import datetime

def fetch_marketing_data(source_name):
    """
    Simulasi ekstraksi data metrik dari API sumber marketing.
    Nantinya data ini akan dihubungkan ke pipeline SQL.
    """
    print(f"[{datetime.now()}] Memulai ekstraksi data dari: {source_name}...")
    
    # Mock data untuk inisialisasi struktur
    mock_data = {
        "campaign_id": "CMP-001",
        "impressions": 15000,
        "clicks": 350
    }
    
    print("Ekstraksi berhasil.")
    return mock_data

if __name__ == "__main__":
    data = fetch_marketing_data("Social Media Ads")
    print(json.dumps(data, indent=4))