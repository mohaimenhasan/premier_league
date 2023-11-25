"""
*******DISCLAIMER THIS IS A FUN TOOL TO USE. NOT MEANT TO BE TAKEN SERIOUSLY*****************
Based on Matchday week 13. It predicted 6/7 games correctly. 

This Python script defines a FastAPI web application that retrieves and compares football (soccer) statistics for Premier League clubs.
The application scrapes data from "https://fbref.com" using BeautifulSoup, providing endpoints to fetch club-specific data, compare statistics between two clubs, and predict a winner based on various performance metrics.
The script includes functions for data retrieval, club name standardization, and score calculation, ultimately offering JSON responses with relevant football statistics and match predictions.
The application uses the FastAPI framework for building the API and integrates external libraries such as requests and BeautifulSoup for web scraping.

Requirements: FASTAPI, beautifulsoup4, uvicorn
"""


import requests
from fastapi import FastAPI
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

def get_definition():
    url = "https://fbref.com/en/comps/9/stats/Premier-League-Stats"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', {'class': 'stats_table'})

        data = []

        for row in table.find_all('tr')[2:]:
            # Extract data from each cell in the row
            row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
            data.append(row_data)

        return {"table_data": data}
    else:
        return f"Failed to retrieve data. Status code: {response.status_code}"
def get_defence():
    url = "https://fbref.com/en/comps/9/keepers/Premier-League-Stats"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', {'class': 'stats_table'})

        data = []

        for row in table.find_all('tr')[2:]:
            # Extract data from each cell in the row
            row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
            data.append(row_data)

        return {"table_data": data}
    else:
        return f"Failed to retrieve data. Status code: {response.status_code}"  

def get_possesion():
    url = "https://fbref.com/en/comps/9/possession/Premier-League-Stats"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', {'class': 'stats_table'})

        data = []

        for row in table.find_all('tr')[2:]:
            # Extract data from each cell in the row
            row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
            data.append(row_data)

        return {"table_data": data}
    else:
        return f"Failed to retrieve data. Status code: {response.status_code}"  


@app.get("/fpl_club_data")
async def get_club_data(club = ""):
    club = club.title()
    if club == "ManCity" or club == "City" or club == "ManchesterCity" or club ==  "Manchestercity":
        club = "Manchester City"
    if club == "ManUnited" or club == "ManUTD" or club == "ManchesterUnited" or club == "Manchesterunited" or club == "ManchesterUTD" or club == "Manunited" or club == "Man utd" or club == "Manchester utd" or club == "Man United":
        club = "Manchester Utd"
    if club == "Villa" or club == "AstonVilla" or club == "Astonvilla" or club ==  "Aston":
        club = "Aston Villa"
    if club == "Crystal" or club == "CrystalPalace" or club == "Crystalpalace" or club == "Palace":
        club = "Crystal Palace"
    if club == "NewcastleUnited" or club == "Newcastle" or club == "NewcastleUtd" or club ==  "NewcastleUTD" or club == "Newcastle united":
        club = "Newcastle Utd"
    if club == "Nottingham Forest" or club == "Nottingham" or club == "Forest" or club == "Nottingham" or club == "NottinghamForest":
        club = "Nott'ham Forest"   
    if club == "LutonTown" or club == "Lutontown" or club == "Luton town" or club == "Luton" or club == "Town":
        club = "Luton Town"   
    if club == "SheffieldUnited" or club == "SheffieldUTD" or club == "Sheffield" or club == "Sheffieldunited" or club == "Sheffield United" or club == "Sheffield utd":
        club = "Sheffield Utd"
    if club == "WestHam" or club == "West ham" or club == "Ham" or club == "West":
        club = "West Ham"
        
    x = get_definition()
    y = get_defence()
    z = get_possesion()
    hold = []

    for i, j, z in zip(x["table_data"], y["table_data"], z["table_data"]):
        if club in i[0] and club in j[0] and club in z[0]:
            data_entry = {
                "Team": i[0],
                "Expected Goal": i[16],
                "Progressive Passing": i[21],
                "Goal per 90 minutes": i[22],
                "Expected Goal per 90 minutes": i[27],
                "Possesion percentage": z[2],
                "Possesion in the Attacking 3rd": z[8],
                "Number of take ons": z[11],
                "Successful Take-ons Percentage": z[13],
                "Goal Against": j[6],
                "Goal Against Per 90 minute": j[7],
                "Clean Sheet": j[14],
                "Shots Against": j[8]
            }
            hold.append(data_entry)
    if len(hold) == 0:
        return {
            "please_check_spelling": (
            "Please check the spelling or try a different spelling from the following list: "),
        "club_list": [
            "Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton",
            "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Liverpool",
            "Luton Town", "Manchester City", "Manchester Utd", "Newcastle Utd",
            "Nottingham Forest", "Sheffield Utd", "Tottenham", "West Ham", "Wolves"
            ]
        }

    return hold


@app.get("/fpl_club_compare")
async def compare_two_club(club1="", club2=""):
    a = await get_club_data(club1)
    b = await get_club_data(club2)
    return {"club1": a, "club2": b}



@app.get("/fpl_who_will_win")
async def who_will_win(club1="", club2=""):
    a = await compare_two_club(club1, club2)

    score_club1 = 0
    score_club2 = 0
    if "please_check_spelling" in (a["club1"]) or "please_check_spelling" in (a["club2"]):
        return {
            "please_check_spelling": (
            "Please check the spelling or try a different spelling from the following list: "),
        "club_list": [
            "Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton",
            "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Liverpool",
            "Luton Town", "Manchester City", "Manchester Utd", "Newcastle Utd",
            "Nottingham Forest", "Sheffield Utd", "Tottenham", "West Ham", "Wolves"
            ]
        }
    for i, j in zip(a["club1"], a["club2"]):

        clubA = i["Team"]
        clubB = j["Team"]



        if i["Expected Goal"] > j["Expected Goal"]:
            score_club1 += 1
        elif j["Expected Goal"] > i["Expected Goal"]:
            score_club2 += 1

        if i["Progressive Passing"] > j["Progressive Passing"]:
            score_club1 += 1
        elif j["Progressive Passing"] > i["Progressive Passing"]:
            score_club2 += 1

        if i["Goal per 90 minutes"] > j["Goal per 90 minutes"]:
            score_club1 += 1
        elif j["Goal per 90 minutes"] > i["Goal per 90 minutes"]:
            score_club2 += 1

        if i["Expected Goal per 90 minutes"] > j["Expected Goal per 90 minutes"]:
            score_club1 += 1
        elif j["Expected Goal per 90 minutes"] > i["Expected Goal per 90 minutes"]:
            score_club2 += 1

        if i["Possesion percentage"] > j["Possesion percentage"]:
            score_club1 += 1
        elif j["Possesion percentage"] > i["Possesion percentage"]:
            score_club2 += 1

        if i["Possesion in the Attacking 3rd"] > j["Possesion in the Attacking 3rd"]:
            score_club1 += 1
        elif j["Possesion in the Attacking 3rd"] > i["Possesion in the Attacking 3rd"]:
            score_club2 += 1

        if i["Number of take ons"] > j["Number of take ons"]:
            score_club1 += 1
        elif j["Number of take ons"] > i["Number of take ons"]:
            score_club2 += 1

        if i["Successful Take-ons Percentage"] > j["Successful Take-ons Percentage"]:
            score_club1 += 1
        elif j["Successful Take-ons Percentage"] > i["Successful Take-ons Percentage"]:
            score_club2 += 1

        if i["Goal Against Per 90 minute"] < j["Goal Against Per 90 minute"]:
            score_club1 += 1
        elif j["Goal Against Per 90 minute"] < i["Goal Against Per 90 minute"]:
            score_club2 += 1

        if i["Clean Sheet"] > j["Clean Sheet"]:
            score_club1 += 1
        elif j["Clean Sheet"] > i["Clean Sheet"]:
            score_club2 += 1

        if i["Shots Against"] < j["Shots Against"]:
            score_club1 += 1
        elif j["Shots Against"] < i["Shots Against"]:
            score_club2 += 1

        if score_club1 > score_club2:
            winner = clubA
        elif score_club2 > score_club1:
            winner = clubB
        else:
            return {"we can't determine a winner the scores are too close. It will be a tie"}
        
    result = {
        "club1": {"name": clubA, "score": score_club1},
        "club2": {"name": clubB, "score": score_club2}
    }

    if abs(score_club1 - score_club2) < 3:
        prediction = {
            "It will be a close game. We would not recommend choosing a team as a guaranteed winner."
        }
    elif 3 < abs(score_club1 - score_club2) < 6:
        prediction = {
            f"Based on our algorithm, the club that will win is: {winner}. However, it can still be a close game. Be careful about how much you are risking on the winner of the game."
        }
    else:
        prediction = {
            f"Based on our algorithm, the club that will win is: {winner}. This is a safer team to choose as the winner of the game."
        }
    return prediction, result
