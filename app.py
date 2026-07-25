import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="IPL Stats Analyzer", page_icon="🏏")

st.title("🏏 IPL Stats Analyzer (2008-2024)")
st.subheader("Built by Talari Pranay")

@st.cache_data
def load_data():
    return pd.read_csv('matches.csv')

try:
    df = load_data()
except FileNotFoundError:
    st.error("Data file not found. Please check the file path.")
    st.stop()

# Dropdown - user selects what to view
option = st.selectbox(
    "📊 Choose an analysis to view:",
    ["Top 10 Teams by Wins", "Matches Per Season", "Toss Decision Analysis", "Top 10 Player of the Match"]
)

if option == "Top 10 Teams by Wins":
    st.header("🏆 Top 10 Teams by Wins")
    top_teams = df['winner'].value_counts().head(10)
    st.bar_chart(top_teams)

elif option == "Matches Per Season":
    st.header("📅 Matches Per Season")
    season = df['season'].value_counts().sort_index()
    st.bar_chart(season)

elif option == "Toss Decision Analysis":
    st.header("🎯 Toss Decision Analysis")
    toss = df['toss_decision'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(toss, labels=toss.index, autopct='%1.1f%%', colors=['skyblue', 'lightgreen'])
    ax.set_title('Field vs Bat')
    st.pyplot(fig)

elif option == "Top 10 Player of the Match":
    st.header("🌟 Top 10 Player of the Match")
    players = df['player_of_match'].value_counts().head(10)
    st.bar_chart(players)