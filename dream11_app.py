import streamlit as st
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from sklearn.linear_model import LinearRegression
from io import BytesIO
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(page_title="Dream11 Team Predictor", layout="wide")
st.title("🏏 Dream11 AI-Powered Team Selector")

# Upload Excel file
uploaded_file = st.file_uploader("Upload SquadPlayerNames_IndianT20League.xlsx", type=["xlsx"])
match_number = st.number_input("Enter Match Number", min_value=1, step=1)

if uploaded_file and match_number:

    st.info("Processing... Please wait 1-2 minutes for live stats scraping and predictions.")

    player_map = {'Vansh Bedi': 1413379,
        'Andre Siddharth': 1440190,
        'Ramakrishna Ghosh': 1339053,
        'Shaik Rasheed': 1292497,
        'Gurjapneet Singh': 1269869,
        'Matheesha Pathirana': 1194795,
        'Noor Ahmad': 1182529,
        'Anshul Kamboj': 1175428,
        'Nathan Ellis': 826915,
        'Mukesh Choudhary': 1125688,
        'Ruturaj Gaikwad': 1060380,
        'Kamlesh Nagarkoti': 1070188,
        'Rachin Ravindra': 959767,
        'Khaleel Ahmed': 942645,
        'Shivam Dube': 714451,
        'Rahul Tripathi': 446763,
        'Sam Curran': 662973,
        'Shreyas Gopal': 344580,
        'Deepak Hooda': 497121,
        'Devon Conway': 379140,
        'Jamie Overton': 510530,
        'Vijay Shankar': 477021,
        'Ravichandran Ashwin': 26421,
        'Ravindra Jadeja': 234675,
        'MS Dhoni': 28081,
        'Madhav Tiwari': 1460385,
        'Manvanth Kumar L': 1392186,
        'Tripurana Vijay': 1292527,
        'Vipraj Nigam': 1449074,
        'Tristan Stubbs': 595978,
        'Abishek Porel': 1277545,
        'Ashutosh Sharma': 1131978,
        'Donovan Ferreira': 698315,
        'Sameer Rizvi': 1175489,
        'Jake Fraser-McGurk': 1168049,
        'Ajay Mandal': 1059570,
        'Darshan Nalkande': 1111917,
        'T Natarajan': 802575,
        'Mukesh Kumar': 926851,
        'Kuldeep Yadav': 559235,
        'Mohit Sharma': 537119,
        'Lokesh Rahul': 422108,
        'Axar Patel': 554691,
        'Dushmantha Chameera': 552152,
        'Karun Nair': 398439,
        'Faf du Plessis': 44828,
        'Mitchell Starc': 311592,
        'Gurnoor Brar Singh': 1287033,
        'Nishant Sindhu': 1292506,
        'Arshad Khan': 1244751,
        'Sai Sudharsan': 1151288,
        'Kumar Kushagra': 1207295,
        'Manav Suthar': 1175426,
        'Sherfane Rutherford': 914541,
        'Gerald Coetzee': 596010,
        'Anuj Rawat': 1123073,
        'Kulwant Khejroliya': 1083033,
        'Shubman Gill': 1070173,
        'Ravisrinivasan Sai Kishore': 1048739,
        'Mahipal Lomror': 853265,
        'Karim Janat': 793467,
        'Washington Sundar': 719715,
        'Mohammed Siraj': 940973,
        'Glenn Phillips': 823509,
        'Rashid-Khan': 793463,
        'Prasidh Krishna': 917159,
        'Jayant Yadav': 447587,
        'Rahul Tewatia': 423838,
        'Kagiso Rabada': 550215,
        'Jos Buttler': 308967,
        'Ishant Sharma': 236779,
        'Harshit Rana': 1312645,
        'Angkrish Raghuvanshi': 1292495,
        'Vaibhav Arora': 1209292,
        'Luvnith Sisodia': 1155253,
        'Mayank Markande': 1081442,
        'Chetan Sakariya': 1131754,
        'Rahmanullah Gurbaz': 974087,
        'Spencer Johnson': 1123718,
        'Varun Chakravarthy': 1108375,
        'Anrich Nortje': 481979,
        'Ramandeep Singh': 1079470,
        'Rovman Powell': 820351,
        'Rinku Singh': 723105,
        'Venkatesh Iyer': 851403,
        'Moeen Ali': 8917,
        'Quinton de Kock': 379143,
        'Andre Russell': 276298,
        'Sunil Narine': 230558,
        'Manish Pandey': 290630,
        'Ajinkya Rahane': 277916,
        'Umran Malik': 1246528,
        'Digvesh Singh': 1460529,
        'Prince Yadav': 1300836,
        'Shamar Joseph': 1356971,
        'Mayank Yadav': 1292563,
        'Arshin Kulkarni': 1403153,
        'Akash Deep': 1176959,
        'Akash Singh': 1175458,
        'Yuvraj Chaudhary': 1175463,
        'Ravi Bishnoi': 1175441,
        'Abdul Samad': 1175485,
        'Shahbaz Ahmed': 1159711,
        'Rajvardhan Hangargekar': 1175429,
        'Ayush Badoni': 1151270,
        'Aryan Juyal': 1130300,
        'Mohsin Khan': 1132005,
        'Matthew Breetzke': 595267,
        'Manimaran Siddharth': 1151286,
        'Rishabh Pant': 931581,
        'Himmat Singh': 805235,
        'Aiden Markram': 600498,
        'Avesh Khan': 694211,
        'Nicholas Pooran': 604302,
        'David Miller': 321777,
        'Mitchell Marsh': 272450,
        'Bevon Jacobs': 1410577,
        'Naman Dhir': 1287032,
        'Robin Minz': 1350762,
        'Raj Angad Bawa': 1292502,
        'Vignesh Puthur': 1460388,
        'Satyanarayana Raju': 1392201,
        'Ashwani Kumar': 1209126,
        'Tilak Varma': 1170265,
        'KL Shrijith': 778241,
        'Mujeeb-ur-Rahman': 974109,
        'Ryan Rickelton': 605661,
        'Arjun Tendulkar': 1148776,
        'Will Jacks': 897549,
        'Hardik Pandya': 625371,
        'Mitchell Santner': 502714,
        'Reece Topley': 461632,
        'Corbin Bosch': 594322,
        'Jasprit Bumrah': 625383,
        'Trent Boult': 277912,
        'Suryakumar Yadav': 446507,
        'Deepak Chahar': 447261,
        'Karn Sharma': 30288,
        'Rohit Sharma': 34102,
        'Musheer Khan': 1316430,
        'Harnoor Singh Pannu': 1292496,
        'Pyla Avinash': 1324449,
        'Suryansh Shedge': 1339698,
        'Harpreet Brar': 1168641,
        'Priyansh Arya': 1175456,
        'Kuldeep Sen': 1163695,
        'Marco Jansen': 696401,
        'Nehal Wadhera': 1151273,
        'Prabhsimran Singh': 1161024,
        'Aaron Hardie': 1124283,
        'Arshdeep Singh': 1125976,
        'Azmatullah Omarzai': 819429,
        'Vishnu Vinod': 732293,
        'Xavier Bartlett': 1050545,
        'Shashank Singh': 377534,
        'Lockie Ferguson': 493773,
        'Josh Inglis': 662235,
        'Vyshak Vijaykumar': 777815,
        'Pravin Dubey': 777515,
        'Yash Thakur': 1070196,
        'Shreyas Iyer': 642519,
        'Marcus Stoinis': 325012,
        'Yuzvendra Chahal': 430246,
        'Glenn Maxwell': 325026,
        'Abhinandan Singh': 1449085,
        'Swastik Chikara': 1403198,
        'Mohit Rathee': 1349361,
        'Suyash Sharma': 1350792,
        'Jacob Bethell': 1194959,
        'Rasikh Salam': 1161489,
        'Yash Dayal': 1159720,
        'Manoj Bhandage': 1057399,
        'Nuwan Thushara': 955235,
        'Romario Shepherd': 677077,
        'Tim David': 892749,
        'Devdutt Padikkal': 1119026,
        'Krunal Pandya': 471342,
        'Rajat Patidar': 823703,
        'Jitesh Sharma': 721867,
        'Lungi Ngidi': 542023,
        'Philip Salt': 669365,
        'Liam Livingstone': 403902,
        'Josh Hazlewood': 288284,
        'Bhuvneshwar Kumar': 326016,
        'Swapnil Singh': 232292,
        'Virat Kohli': 253802,
        'Vaibhav Suryavanshi': 1408688,
        'Ashok Sharma': 1299879,
        'Kwena Maphaka': 1294342,
        'Kunal Singh Rathore': 1339031,
        'Akash Madhwal': 1206039,
        'Shubham Dubey': 1252585,
        'Yudhvir Singh Charak': 1206052,
        'Maheesh Theekshana': 1138316,
        'Dhruv Jurel': 1175488,
        'Kumar Kartikeya': 1159843,
        'Yashasvi Jaiswal': 1151278,
        'FazalHaq Farooqi': 974175,
        'Riyan Parag': 1079434,
        'Tushar Deshpande': 822553,
        'Jofra Archer': 669855,
        'Wanindu Hasaranga': 784379,
        'Nitish Rana': 604527,
        'Shimron Hetmyer': 670025,
        'Sandeep Sharma': 438362,
        'Sanju Samson': 425943,
        'Aniket Verma': 1409976,
        'Eshan Malinga': 1306214,
        'K Nitish Reddy': 1175496,
        'Abhinav Manohar': 778963,
        'Atharva Taide': 1125958,
        'Simarjeet- Singh': 1159722,
        'Rahul Chahar': 1064812,
        'Abhishek Sharma': 1070183,
        'Kamindu Mendis': 784373,
        'Wiaan Mulder': 698189,
        'Zeeshan Ansari': 942371,
        'Ishan Kishan': 720471,
        'Heinrich Klaasen': 436757,
        'Sachin Baby': 432783,
        'Travis Head': 530011,
        'Adam Zampa': 379504,
        'Harshal Patel': 390481,
        'Pat Cummins': 489889,
        'Mohammed Shami': 481896,
        'Jaydev Unadkat': 390484,
        'Ayush Mhatre': 1452455,
        'Dewald Brevis': 1070665,
        'Shardul Thakur': 475281} 

    def get_playing_xi(file_bytes, match_number):
        xls = pd.ExcelFile(file_bytes)
        sheet_name = f"Match_{match_number}"
        if sheet_name not in xls.sheet_names:
            return None
        df = pd.read_excel(xls, sheet_name=sheet_name)
        return df[df["IsPlaying"] == "PLAYING"].sort_values(by="lineupOrder")

    def fetch_player_stats(player_name, player_type, stats_dict):
        if player_name not in player_map:
            return
        player_id = player_map[player_name]
        headers = {"User-Agent": "Mozilla/5.0"}

        def scrape(url):
            soup = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
            tables = soup.find_all("table", class_="engineTable")
            return pd.read_html(str(tables[3]))[0].head(16).iloc[::-1] if len(tables) >= 4 else None

        if player_name not in stats_dict:
            stats_dict[player_name] = {"Batting": None, "Bowling": None, "Fielding": None}

        if player_type in ["BAT", "ALL", "WK", "BOWL"]:
            url = f"https://stats.espncricinfo.com/ci/engine/player/{player_id}.html?class=6;host=6;orderby=start;orderbyad=reverse;template=results;type=batting;view=innings"
            stats_dict[player_name]["Batting"] = scrape(url)

        if player_type in ["BOWL", "ALL"]:
            url = f"https://stats.espncricinfo.com/ci/engine/player/{player_id}.html?class=6;host=6;orderby=start;orderbyad=reverse;template=results;type=bowling;view=innings"
            stats_dict[player_name]["Bowling"] = scrape(url)

        if player_type in ["BAT", "ALL", "WK", "BOWL"]:
            url = f"https://stats.espncricinfo.com/ci/engine/player/{player_id}.html?class=6;host=6;orderby=start;orderbyad=reverse;template=results;type=fielding;view=innings"
            stats_dict[player_name]["Fielding"] = scrape(url)

    def create_lagged_features(scores, lag=1):
        return np.array([scores[i:i+lag] for i in range(len(scores) - lag)]), np.array(scores[lag:])

    def train_and_predict(scores):
        if len(scores) < 3:
            return "N/A"
        scores = np.convolve(scores, np.ones(3)/3, mode='valid')
        X, y = create_lagged_features(scores)
        model = LinearRegression().fit(X, y)
        pred = model.predict(np.array([[np.mean(scores[-3:])]]))
        return max(0, round(pred[0], 2))

    def calculate_dream11_score(df):
        scores = {}
        for player, stats in df.iterrows():
            s = 0
            for col in df.columns:
                stats[col] = pd.to_numeric(stats[col], errors='coerce')
            if not pd.isna(stats["Runs"]):
                s += stats["Runs"]
                if stats["Runs"] >= 25: s += 4
                if stats["Runs"] >= 50: s += 4
                if stats["Runs"] >= 75: s += 4
                if stats["Runs"] >= 100: s += 4
                if stats["Runs"] == 0: s -= 2
            if not pd.isna(stats["4s"]): s += stats["4s"] * 4
            if not pd.isna(stats["6s"]): s += stats["6s"] * 6
            if not pd.isna(stats["Wkts"]): s += stats["Wkts"] * 31
            if not pd.isna(stats["Econ"]):
                e = stats["Econ"]
                if e < 5: s += 6
                elif e < 6: s += 4
                elif e < 7: s += 2
                elif e >= 10: s -= 2
                if e >= 11: s -= 4
                if e >= 12: s -= 6
            if not pd.isna(stats["SR"]) and not pd.isna(stats["BF"]) and stats["BF"] >= 10:
                sr = stats["SR"]
                if sr > 170: s += 6
                elif sr > 150: s += 4
                elif sr > 130: s += 2
                elif sr < 70: s -= 2
                elif sr < 60: s -= 4
                elif sr < 50: s -= 6
            if not pd.isna(stats["Ct"]): s += stats["Ct"] * 8
            if not pd.isna(stats["St"]): s += stats["St"] * 12
            scores[player] = s
        return pd.DataFrame.from_dict(scores, orient='index', columns=['Dream11 Score'])

    main_df = get_playing_xi(uploaded_file, match_number)
    playing_22 = main_df[["Player Name", "Player Type"]].values.tolist()
    player_stats = {}
    for pname, ptype in playing_22:
        fetch_player_stats(pname, ptype, player_stats)

    columns = ["4s", "6s", "SR", "Runs", "Wkts", "Econ", "Ct", "St", "BF"]
    all_predictions = {}

    for pname, stats in player_stats.items():
        preds = {col: "N/A" for col in columns}
        if stats["Batting"] is not None:
            df = stats["Batting"]
            for col in ["4s", "6s", "SR", "Runs", "BF"]:
                if col in df.columns:
                    df[col] = df[col].astype(str).str.replace("*", "").replace(["-", "DNB", "TDNB", "sub"], np.nan)
                    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
                    preds[col] = train_and_predict(df[col].dropna().values.astype(float))
        if stats["Bowling"] is not None:
            df = stats["Bowling"]
            for col in ["Wkts", "Econ"]:
                if col in df.columns:
                    df[col] = df[col].replace(["-", "DNB", "TDNB"], np.nan).astype(float).fillna(0)
                    preds[col] = train_and_predict(df[col].dropna().values)
        if stats["Fielding"] is not None:
            df = stats["Fielding"]
            for col in ["Ct", "St"]:
                if col in df.columns:
                    df[col] = df[col].replace(["-", "DNB", "TDNB"], np.nan).astype(float).fillna(0)
                    preds[col] = train_and_predict(df[col].dropna().values)
        all_predictions[pname] = preds

    pred_df = pd.DataFrame.from_dict(all_predictions, orient="index")
    dream11_scores = calculate_dream11_score(pred_df)
    df = main_df.merge(dream11_scores, left_on="Player Name", right_index=True)
    df = df.merge(pred_df, left_on="Player Name", right_index=True)
    df = df.sort_values(by="Dream11 Score", ascending=False)

    final_team = []
    selected_roles = {"BAT": 0, "BOWL": 0, "WK": 0, "ALL": 0}
    selected_teams = set()

    for role in ["BAT", "BOWL", "WK", "ALL"]:
        player = df[df["Player Type"] == role].iloc[0]
        final_team.append(player)
        selected_roles[role] += 1
        selected_teams.add(player["Team"])

    for team in df["Team"].unique():
        if team not in selected_teams:
            player = df[df["Team"] == team].iloc[0]
            final_team.append(player)
            selected_roles[player["Player Type"]] += 1
            selected_teams.add(team)

    remaining = df[~df["Player Name"].isin([p["Player Name"] for p in final_team])]
    for _, player in remaining.iterrows():
        if len(final_team) >= 11:
            break
        final_team.append(player)

    final_df = pd.DataFrame(final_team)
    final_df["C/VC"] = "NA"
    final_df.loc[final_df["Dream11 Score"].idxmax(), "C/VC"] = "C"
    vc_idx = final_df["Dream11 Score"].nlargest(2).index[-1]
    final_df.loc[vc_idx, "C/VC"] = "VC"
    final_df["C/VC"] = pd.Categorical(final_df["C/VC"], categories=["C", "VC", "NA"], ordered=True)
    final_df = final_df.sort_values(by="C/VC")[["Player Name", "Team", "C/VC", "Dream11 Score"]]

    st.success("Predictions complete! Here's your team:")
    st.dataframe(final_df)

    csv = final_df.to_csv(index=False).encode()
    st.download_button("Download Dream11 Team", data=csv, file_name="Dream11_Team.csv", mime="text/csv")
