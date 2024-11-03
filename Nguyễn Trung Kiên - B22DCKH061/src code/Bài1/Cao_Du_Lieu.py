import requests
from bs4 import BeautifulSoup 
import pandas as pd
import time

def geturl(url):
    res = requests.get(url)
    return BeautifulSoup(res.text, 'html.parser')

def extract_table_data(page, table_id, data_append_csv, start_col, end_col, default_count):
        
    table_data = []
    try:
        table = page.find("table", {"id": table_id})
        if table:
            for row in table.tbody.find_all('tr'):
                cols = row.find_all("td")
                if data_append_csv == row.find("th", {"data-stat": "player"}).get('data-append-csv'):
                    for col in cols[start_col:end_col]:
                        table_data.append(col.get_text() if col.get_text() != "" else "N/A")
                    return table_data
    except:
        pass
    # Nếu không có dữ liệu hợp lệ, trả về danh sách "N/A"
    return ["N/A"] * default_count

base_url = "https://fbref.com"
epl_2023_2024 = "/en/comps/9/2023-2024/2023-2024-Premier-League-Stats"
response = requests.get(base_url + epl_2023_2024)
document = BeautifulSoup(response.text, "html.parser")
players = []

for linkal in document.select('#stats_squads_keeper_for tbody tr a'):
    link = linkal['href']
    page = geturl(base_url + link)
    team = linkal.get_text()
    try:
        table = page.find("table", {"id": "stats_standard_9"})
        for row in table.tbody.find_all('tr'):
            player_data = []  
            cols = row.find_all("td")
            name = row.find("th")
            data_append_csv = name.get('data-append-csv')
            minutes_played = cols[5].get_text().replace(',', '')
            if minutes_played.isdigit() and int(minutes_played) > 90:
                player_data.append(data_append_csv)
                player_data.append(name.get_text())
                player_data.append(cols[0].get_text() if cols[0].get_text() != "" else "N/A")
                player_data.append(team)
                for col in cols[1:5]:
                    player_data.append(col.get_text() if col.get_text() != "" else "N/A")
                player_data.append(minutes_played)
                player_data.append(cols[10].get_text() if cols[10].get_text() != "" else "N/A")
                player_data.append(cols[7].get_text() if cols[7].get_text() != "" else "N/A")
                player_data.append(cols[8].get_text() if cols[8].get_text() != "" else "N/A")
                
                
                for col in cols[13:18]:
                    player_data.append(col.get_text() if col.get_text() != "" else "N/A")
                for col in cols[19:len(cols) - 1]:
                    player_data.append(col.get_text() if col.get_text() != "" else "N/A")

                # Lấy dữ liệu từ các bảng khác nhau
                player_data.extend(extract_table_data(page, "stats_keeper_9", data_append_csv, 7, 22, 15))
                player_data.extend(extract_table_data(page, "stats_shooting_9", data_append_csv, 4, 21, 17))
                player_data.extend(extract_table_data(page, "stats_passing_9", data_append_csv, 4, 27, 23))
                player_data.extend(extract_table_data(page, "stats_passing_types_9", data_append_csv, 5, 19, 14))
                player_data.extend(extract_table_data(page, "stats_gca_9", data_append_csv, 4, 20, 16))
                player_data.extend(extract_table_data(page, "stats_defense_9", data_append_csv, 4, 20, 16))
                player_data.extend(extract_table_data(page, "stats_possession_9", data_append_csv, 4, 26, 22))
                
                # Đặc biệt cho bảng "stats_playing_time_9"
                player_data.extend(extract_table_data(page, "stats_playing_time_9", data_append_csv, 8, 17, 9))
                player_data.extend(extract_table_data(page, "stats_playing_time_9", data_append_csv, 20, 22, 2))
                
                # Bảng cuối cùng "stats_misc_9"
                player_data.extend(extract_table_data(page, "stats_misc_9", data_append_csv, 7, 11, 4))
                player_data.extend(extract_table_data(page, "stats_misc_9", data_append_csv, 15, 20, 5))

                players.append(player_data)
                
    except:
        continue
    time.sleep(5)


# Tạo DataFrame và sắp xếp dữ liệu
dataFrame = pd.DataFrame(players,columns = [
    "id" , "Name","Nation", "Team", "Position", "Age",
    "PlayingTime.MatchesPlayed", "PlayingTime.Starts", "PlayingTime.Minutes",
    "Performance.NonPenaltyGoals", "Performance.PenaltyGoals", "Performance.Assists", 
    "Performance.YellowCards", "Performance.RedCards",
    "Expected.xG", "Expected.npxG", "Expected.xAG",
    "Progression.PrgC", "Progression.PrgP", "Progression.PrgR",
    "Per90.Gls", "Per90.Ast", "Per90.G+A", "Per90.G-PK", "Per90.G+A-PK", 
    "Per90.xG", "Per90.xAG", "Per90.xG+xAG", "Per90.npxG", "Per90.npxG+xAG",
    "Goalkeeping.Performance.GA", "Goalkeeping.Performance.GA90", 
    "Goalkeeping.Performance.SoTA", "Goalkeeping.Performance.Saves", 
    "Goalkeeping.Performance.Save%", "Goalkeeping.Performance.W", 
    "Goalkeeping.Performance.D", "Goalkeeping.Performance.L", 
    "Goalkeeping.Performance.CS", "Goalkeeping.Performance.CS%",
    "Goalkeeping.PenaltyKicks.PKatt", "Goalkeeping.PenaltyKicks.PKA", 
    "Goalkeeping.PenaltyKicks.PKsv", "Goalkeeping.PenaltyKicks.PKm", 
    "Goalkeeping.PenaltyKicks.Save%",
    "Shooting.Standard.Gls", "Shooting.Standard.Sh", "Shooting.Standard.SoT", 
    "Shooting.Standard.SoT%", "Shooting.Standard.Sh/90", "Shooting.Standard.SoT/90", 
    "Shooting.Standard.G/Sh", "Shooting.Standard.G/SoT", "Shooting.Standard.Dist", 
    "Shooting.Standard.FK", "Shooting.Standard.PK", "Shooting.Standard.PKatt",
    "Shooting.Expected.xG", "Shooting.Expected.npxG", "Shooting.Expected.npxG/Sh", 
    "Shooting.Expected.G-xG", "Shooting.Expected.np:G-xG",
    "Passing.Total.Cmp", "Passing.Total.Att", "Passing.Total.Cmp%", 
    "Passing.Total.TotDist", "Passing.Total.PrgDist",
    "Passing.Short.Cmp", "Passing.Short.Att", "Passing.Short.Cmp%",
    "Passing.Medium.Cmp", "Passing.Medium.Att", "Passing.Medium.Cmp%",
    "Passing.Long.Cmp", "Passing.Long.Att", "Passing.Long.Cmp%",
    "Passing.Expected.Ast", "Passing.Expected.xAG", "Passing.Expected.xA", 
    "Passing.Expected.A-xAG", "Passing.Expected.KP", "Passing.Expected.1/3", 
    "Passing.Expected.PPA", "Passing.Expected.CrsPA", "Passing.Expected.PrgP",
    "PassTypes.Live", "PassTypes.Dead", "PassTypes.FK", "PassTypes.TB", 
    "PassTypes.Sw", "PassTypes.Crs", "PassTypes.TI", "PassTypes.CK",
    "PassTypes.CornerKicks.In", "PassTypes.CornerKicks.Out", 
    "PassTypes.CornerKicks.Str", "PassTypes.Outcomes.Cmp", 
    "PassTypes.Outcomes.Off", "PassTypes.Outcomes.Blocks",
    "GoalAndShotCreation.SCA", "GoalAndShotCreation.SCA90",
    "GoalAndShotCreation.SCAType.PassLive", "GoalAndShotCreation.SCAType.PassDead", 
    "GoalAndShotCreation.SCAType.TO", "GoalAndShotCreation.SCAType.Sh", 
    "GoalAndShotCreation.SCAType.Fld", "GoalAndShotCreation.SCAType.Def",
    "GoalAndShotCreation.GCA", "GoalAndShotCreation.GCA90",
    "GoalAndShotCreation.GCAType.PassLive", "GoalAndShotCreation.GCAType.PassDead", 
    "GoalAndShotCreation.GCAType.TO", "GoalAndShotCreation.GCAType.Sh", 
    "GoalAndShotCreation.GCAType.Fld", "GoalAndShotCreation.GCAType.Def",
    "DefensiveActions.Tackles.Tkl", "DefensiveActions.Tackles.TklW", 
    "DefensiveActions.Tackles.Def3rd", "DefensiveActions.Tackles.Mid3rd", 
    "DefensiveActions.Tackles.Att3rd",
    "DefensiveActions.Challenges.Tkl", "DefensiveActions.Challenges.Att", 
    "DefensiveActions.Challenges.Tkl%", "DefensiveActions.Challenges.Lost",
    "DefensiveActions.Blocks.Blocks", "DefensiveActions.Blocks.Sh", 
    "DefensiveActions.Blocks.Pass", "DefensiveActions.Blocks.Int", 
    "DefensiveActions.Blocks.Tkl+Int", "DefensiveActions.Blocks.Clr", 
    "DefensiveActions.Blocks.Err",
    "Possession.Touches.Touches", "Possession.Touches.DefPen", 
    "Possession.Touches.Def3rd", "Possession.Touches.Mid3rd", 
    "Possession.Touches.Att3rd", "Possession.Touches.AttPen", 
    "Possession.Touches.Live",
    "Possession.TakeOns.Att", "Possession.TakeOns.Succ", "Possession.TakeOns.Succ%", 
    "Possession.TakeOns.Tkld", "Possession.TakeOns.Tkld%",
    "Possession.Carries.Carries", "Possession.Carries.TotDist", 
    "Possession.Carries.ProDist", "Possession.Carries.ProgC", 
    "Possession.Carries.1/3", "Possession.Carries.CPA", 
    "Possession.Carries.Mis", "Possession.Carries.Dis",
    "Possession.Receiving.Rec", "Possession.Receiving.PrgR",
    "PlayingTime.Starts", "PlayingTime.Mn/Start", "PlayingTime.Compl",
    "PlayingTime.Subs", "PlayingTime.Mn/Sub", "PlayingTime.unSub",
    "PlayingTime.TeamSuccess.PPM", "PlayingTime.TeamSuccess.onG", 
    "PlayingTime.TeamSuccess.onGA",
    "PlayingTime.TeamSuccessxG.onxG", "PlayingTime.TeamSuccessxG.onxGA",
    "MiscellaneousStats.Performance.Fls", "MiscellaneousStats.Performance.Fld", 
    "MiscellaneousStats.Performance.Off", "MiscellaneousStats.Performance.Crs", 
    "MiscellaneousStats.Performance.OG", "MiscellaneousStats.Performance.Recov",
    "MiscellaneousStats.AerialDuels.Won", "MiscellaneousStats.AerialDuels.Lost", 
    "MiscellaneousStats.AerialDuels.Won%"
])

dataFrame['first_word'] = dataFrame["Name"].str.split().str[0]
dataFrame = dataFrame.sort_values(by=['first_word', 'Age'], ascending=[True, False])
dataFrame.drop(columns=['first_word'], inplace=True)
dataFrame.to_csv('results.csv')
