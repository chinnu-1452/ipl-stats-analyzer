import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="IPL Stats Analyzer", page_icon="🏏")

st.title("🏏 IPL Stats Analyzer (2008-2024)")
st.subheader("Built by Talari Pranay | 90 Day DS Journey")

df = pd.read_csv('matches.csv')

# Top Teams
st.header("🏆 Top 10 Teams by Wins")
top_teams = df['winner'].value_counts().head(10)
st.bar_chart(top_teams)

# Season Wise
st.header("📅 Matches Per Season")
season = df['season'].value_counts().sort_index()
st.bar_chart(season)

# Toss Decision
st.header("🎯 Toss Decision Analysis")
toss = df['toss_decision'].value_counts()
fig, ax = plt.subplots()
ax.pie(toss, labels=toss.index, autopct='%1.1f%%', colors=['skyblue','lightgreen'])
ax.set_title('Field vs Bat')
st.pyplot(fig)

# Player of the Match
st.header("🌟 Top 10 Player of the Match")
players = df['player_of_match'].value_counts().head(10)
st.bar_chart(players)

st.success("Project by Talari Pranay | #BuildingInPublic")