import os
import requests
from zipfile import ZipFile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",  # lỗi
]

def download_and_extract(url, download_dir):
    try:
        # Lấy tên file từ url
        filename = url.split("/")[-1]
        zip_path = os.path.join(download_dir, filename)

        print(f"Tải: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Gây lỗi nếu URL không hợp lệ

        # Ghi nội dung tải được vào file zip
        with open(zip_path, "wb") as f:
            f.write(response.content)

        print(f"✔️ Đã tải: {filename}")

        # Giải nén file zip
        with ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(download_dir)
        print(f"📦 Đã giải nén: {filename}")

        # Xoá file zip sau khi giải nén
        os.remove(zip_path)
        print(f"🗑️ Đã xóa file zip: {filename}\n")

    except Exception as e:
        print(f"❌ Lỗi với {url}: {e}\n")

def main():
    download_dir = "downloads"

    # Tạo thư mục downloads nếu chưa có
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        print("📁 Đã tạo thư mục 'downloads'\n")

    # Tải và giải nén từng file
    for url in download_uris:
        download_and_extract(url, download_dir)


if __name__ == "__main__":
    main()
