import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


df = pd.read_csv('results.csv')


attributes = [
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
]

# Lấy dữ liệu các thuộc tính cần tính toán và điền giá trị trung bình cho các giá trị bị thiếu
X = df[attributes].fillna(df[attributes].mean())

# Chuẩn hóa dữ liệu
CHoa = StandardScaler()
X_CHoa = CHoa.fit_transform(X)
# Sử dụng thuật toán PCA để giảm số chiều dữ liệu xuống 2 chiều
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_CHoa)
# Vẽ hình phân cụm các điểm dữ liệu trên mặt 2D
plt.figure(figsize=(10, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c='blue', edgecolor='k', s=50)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Player Attributes')
plt.show()
