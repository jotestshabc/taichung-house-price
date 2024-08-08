import requests
from bs4 import BeautifulSoup
import pandas as pd

# 目標網站的 URL
url = 'https://lvr.land.moi.gov.tw/'

# 發送 HTTP 請求並獲取網頁內容
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 根據網頁結構提取房屋信息
house_list = []
for listing in soup.find_all('div', class_='property-listing'):
    price = listing.find('span', class_='price').text
    location = listing.find('span', class_='location').text
    size = listing.find('span', class_='size').text
    
    house_list.append({
        'Price': price,
        'Location': location,
        'Size': size
    })

# 將數據轉換為 DataFrame
df = pd.DataFrame(house_list)

# 儲存數據到 CSV 文件
df.to_csv('real_estate_data.csv', index=False)

print("Data saved to real_estate_data.csv")
