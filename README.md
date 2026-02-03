#  🏏 Dream11 Fantasy Team Predictor

A data-driven application that predicts individual player performance for Dream11 fantasy cricket and recommends the best 11-player team based on predicted stats and official Dream11 scoring rules.

#  🚀 How It Works
1. Upload Input File

   Upload an Excel file named SquadPlayerNames_IndianT20League.xlsx

  The file should contain a sheet named Match_<number> (for example, Match_57)

  Players selected for the match must be marked as PLAYING in the IsPlaying column

  Sample input files for the 2025 season are available in the repository

2. Predict Player Performance

  The app scrapes historical player statistics from Cricinfo

  Uses Linear Regression to forecast each player’s next-match performance

  Calculates fantasy points based on official Dream11 scoring rules

3️.  Generate Final Team

  Selects the top 11 players based on predicted fantasy scores

  Automatically assigns Captain (C) and Vice-Captain (VC)

  Allows users to download the final team as a CSV file

#  📦 Tech Stack

Python

Pandas, NumPy

Scikit-learn (Linear Regression)

BeautifulSoup (Web Scraping)

Streamlit (Web App Deployment)

#  📄 Output

CricTensors_Output.csv

Contains the final 11-player fantasy team

Includes player roles, predicted fantasy scores, and C/VC assignments
