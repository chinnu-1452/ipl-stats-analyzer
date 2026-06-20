import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('matches.csv')
print(df.head())
print(df.shape)

# Top 10 Teams by Wins
print("\n--- TOP 10 TEAMS BY WINS ---")
top_teams = df['winner'].value_counts().head(10)
print(top_teams)

# Total matches per season
print("\n--- MATCHES PER SEASON ---")
print(df['season'].value_counts().sort_index())

# Toss winner vs Match winner
print("\n--- TOSS WINNERS WHO WON MATCH ---")
toss_match = df[df['toss_winner'] == df['winner']]
print(f"Toss winner won the match: {len(toss_match)} times out of {len(df)}")

# Top 10 Teams by Wins - Bar Chart
plt.figure(figsize=(12,6))
top_teams.plot(kind='bar', color='royalblue')
plt.title('Top 10 IPL Teams by Wins (2008-2020)')
plt.xlabel('Team')
plt.ylabel('Number of Wins')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_teams.png')
plt.show()
print("Chart saved!")

# Season wise matches
plt.figure(figsize=(12,6))
df['season'].value_counts().sort_index().plot(kind='bar', color='green')
plt.title('IPL Matches Per Season (2008-2020)')
plt.xlabel('Season')
plt.ylabel('Number of Matches')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('season_matches.png')
plt.show()
print("Season chart saved!")

# Toss Decision Analysis
print("\n--- TOSS DECISION ANALYSIS ---")
print(df['toss_decision'].value_counts())

plt.figure(figsize=(8,6))
df['toss_decision'].value_counts().plot(
    kind='pie', 
    autopct='%1.1f%%',
    colors=['skyblue', 'lightgreen'],
    startangle=90
)
plt.title('Toss Decision - Field vs Bat (2008-2024)')
plt.ylabel('')
plt.tight_layout()
plt.savefig('toss_decision.png')
plt.show()
print("Toss chart saved!")

# Player of the Match Analysis
print("\n--- TOP 10 PLAYER OF THE MATCH ---")
top_players = df['player_of_match'].value_counts().head(10)
print(top_players)
# player of the match 
plt.figure(figsize=(12,6))
top_players.plot(kind='bar', color='orange')
plt.title('Top 10 Player of the Match Awards (2008-2024)')
plt.xlabel('Player')
plt.ylabel('Number of Awards')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_players.png')
plt.show()
print("Player chart saved!")