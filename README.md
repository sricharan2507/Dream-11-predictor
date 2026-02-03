🏏 Dream11 Fantasy Team Predictor
This app predicts individual player performance for Dream11 fantasy cricket and recommends the best 11-player team based on predicted stats and official scoring rules.
🚀 How to Use

1. Upload Input File: Provide an Excel file named SquadPlayerNames_IndianT20League.xlsx with a sheet named Match_<number> (e.g., Match_57) and a column IsPlaying marked as "PLAYING". Available in my repository for 2025 season.
2. Hit Predict: The app scrapes player stats from Cricinfo, forecasts their next performance using linear regression, and calculates fantasy scores.
3. Get Final Team: The app returns the top 11 players with captain (C) and vice-captain (VC) assigned, and allows you to download the results.

📦 Tech Stack
Python, Pandas, NumPy, Scikit-learn
Web scraping with BeautifulSoup
Streamlit for deployment
📄 Output
CricTensors_Output.csv: Final team with roles and scores
