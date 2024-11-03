import pandas as pd
import matplotlib.pyplot as plot
import os


df = pd.read_csv('results.csv')

attributes = [
    "PlayingTime.MatchesPlayed"
]

# Tạo thư mục để lưu các biểu đồ
if not os.path.exists('histograms'):
    os.makedirs('histograms')

# Vẽ histogram phân bố của mỗi chỉ số của các cầu thủ trong toàn giải
for attr in attributes:
    plot.figure(figsize=(10, 6))
    df[attr].hist(bins=30, edgecolor='black')
    plot.title(f'Histogram of {attr} for all players')
    plot.xlabel(attr)
    plot.ylabel('Frequency')
    plot.savefig(f'histograms/{attr}_all_players.png')
    plot.close()

# Vẽ histogram phân bố của mỗi chỉ số của các cầu thủ trong mỗi đội
for team in df['Team'].unique():
    team_df = df[df['Team'] == team]
    
    for attr in attributes:
        plot.figure(figsize=(10, 6))
        team_df[attr].hist(bins=30, edgecolor='black')
        plot.title(f'Histogram of {attr} for {team}')
        plot.xlabel(attr)
        plot.ylabel('Frequency')
        plot.savefig(f'histograms/{attr}_{team}.png')
        plot.close()
