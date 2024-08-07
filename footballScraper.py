import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the Eredivisie schedule page
url = "https://fbref.com/en/comps/23/2015-2016/schedule/2015-2016-Eredivisie-Scores-and-Fixtures"

# Send an HTTP request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing match data
table = soup.find("table", class_="stats_table")

# Initialize empty lists to store match details
dates = []
home_teams = []
away_teams = []
scores = []
xGhome = []
xGaway = []

# Extract data from the table rows
for row in table.find_all("tr")[1:]:
    columns = row.find_all("td")
    date = columns[2].text.strip()
    home_team = columns[4].text.strip()
    away_team = columns[6].text.strip()
    score = columns[5].text.strip()
    #xGhome.append(columns[5].text.strip())
    #xGaway.append(columns[7].text.strip())

    dates.append(date)
    home_teams.append(home_team)
    away_teams.append(away_team)
    scores.append(score)

# Create a DataFrame from the extracted data
match_results_df = pd.DataFrame({
    "Date": dates,
    "Home Team": home_teams,
    "Away Team": away_teams,
    "Score": scores,
    #"xGhome": xGhome,
    #"xGaway": xGaway,
})

# Save the match results to a CSV file
match_results_df.to_csv("Eredivisie_Match_Results_2015.csv", index=False)

# Print a success message
print("Match results saved to Eredivisie_Match_Results.csv")
