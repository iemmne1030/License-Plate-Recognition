import requests
from bs4 import BeautifulSoup

# Link đến trang web bạn muốn đọc dữ liệu
url = "https://archive.ics.uci.edu/dataset/73/mushroom"

# Sử dụng thư viện requests để tải trang web
response = requests.get(url)

# Kiểm tra nếu yêu cầu tải trang thành công (status code 200)
if response.status_code == 200:
    # Sử dụng BeautifulSoup để phân tích nội dung trang web
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ở đây, bạn có thể tiếp tục phân tích trang web để đọc dữ liệu bạn cần

    # Ví dụ: In ra toàn bộ nội dung của trang web
    print(soup.prettify())

else:
    print("Không thể tải trang web. Mã trạng thái:", response.status_code)
