import requests
import json
import math
import os


API = os.getenv('FOOTBALL_API_URL', 'https://www.footballtransfers.com/us/transfers/actions/confirmed/overview')
json_file_path = 'results4.csv'

# Số lượng mục tối đa trên mỗi yêu cầu và tổng số mục
max_item_per_req = 4848
max_items = 13353
season_id = 5847


data = []

clubs = ["Arsenal FC" ,"Aston Villa","Bournemounth","Brentford FC","Brighton & Hove Albion","Burnley FC","Chelsea","Crystal Palace"
         ,"Everton FC","Fullham FC","Ipswich Town","Leicester","Liverpool FC","Luton Town","Manchester City",
         "Manchester United","Newcastle United","Nottingham Forest","Sheff Utd","Southampton","Tottenham","Wes Ham United","Wolves"]

# Lặp qua các trang để thu thập dữ liệu
for page in range(1, math.ceil(max_items / max_item_per_req) + 1):
    body = {
        "season": season_id,
        "page": page,
        "pageItems": max_item_per_req
    }
    
    try:
        response = requests.post(API, data=body, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        rawData = response.json()
        
        for record in rawData['records']:
          if record["club_from_name"] in clubs or record["club_to_name"] in clubs:
            data.append({
                "player_id": record['player_id'],
                "player_name": record['player_name'],
                "country_name": record['country_name'],
                "age": record["age"],
                "position_name": record["position_name"],
                "club_from_name": record["club_from_name"],
                "club_to_name": record["club_to_name"],
                "amount": record["amount"],
            })
    except requests.exceptions.RequestException as e:
        continue
       


with open(json_file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


