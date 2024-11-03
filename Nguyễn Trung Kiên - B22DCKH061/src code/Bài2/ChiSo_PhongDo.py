import pandas as pd


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

# Tìm đội bóng có chỉ số cao nhất ở mỗi chỉ số
top_teams = {}
phong_do={}
for attr in attributes:
    top_team = df.loc[df[attr].idxmax()]['Team']
    top_teams[attr] = top_team
    if top_team in phong_do:
        phong_do[top_team] += 1
    else:
        phong_do[top_team] = 1


top_teams_df = pd.DataFrame(list(top_teams.items()), columns=['Attribute', 'Top Team'])


# Tìm đội có thành tích tốt nhất
max_value = float('-inf') 
max_key = None
for key, value in phong_do.items():
    if value > max_value:
        max_value = value
        max_key = key


best_performance_df = pd.DataFrame({'Attribute': ['Best Performance'], 'Top Team': [max_key]})
combined_df = pd.concat([top_teams_df, best_performance_df])


combined_df.to_csv('results_Chiso-Phongdo.csv', index=False)


