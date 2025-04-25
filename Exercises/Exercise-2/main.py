import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL của trang chứa dữ liệu
url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"

# Thư mục để lưu tệp tải về
download_dir = 'downloads'

# Tạo thư mục 'downloads' nếu chưa tồn tại
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Lấy nội dung HTML của trang
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Tìm tất cả các liên kết trong trang
links = soup.find_all('a')

# Lọc các liên kết có đuôi .csv
csv_links = [link.get('href') for link in links if link.get('href') and link.get('href').endswith('.csv')]

if not csv_links:
    print("Không tìm thấy tệp CSV.")
else:
    # Tải xuống các tệp CSV
    for file_name in csv_links:
        file_url = f"{url}{file_name}"
        print(f"Tải về tệp: {file_url}")

        file_response = requests.get(file_url)
        zip_file_path = os.path.join(download_dir, file_name)
        
        # Lưu tệp CSV vào thư mục downloads
        with open(zip_file_path, 'wb') as f:
            f.write(file_response.content)
        print(f"Tệp {file_name} đã được tải về thành công.")

        # Đọc tệp CSV vào DataFrame của Pandas
        df = pd.read_csv(zip_file_path)

        if 'HourlyDryBulbTemperature' in df.columns:
            # Chuyển đổi nhiệt độ sang kiểu số
            df['HourlyDryBulbTemperature'] = pd.to_numeric(df['HourlyDryBulbTemperature'], errors='coerce')

            # Tìm bản ghi có HourlyDryBulbTemperature cao nhất
            max_temp_row = df.loc[df['HourlyDryBulbTemperature'].idxmax()]
            print("Bản ghi có HourlyDryBulbTemperature cao nhất:")
            print(max_temp_row)
        else:
            print("Không tìm thấy cột 'HourlyDryBulbTemperature' trong tệp.")
