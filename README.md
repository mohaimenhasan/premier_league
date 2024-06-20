
# Premier League Statistics Predictor

**DISCLAIMER: THIS IS A FUN TOOL TO USE. NOT MEANT TO BE TAKEN SERIOUSLY**

This Python project defines a FastAPI web application that retrieves and compares football (soccer) statistics for Premier League clubs. The application scrapes data from "https://fbref.com" using BeautifulSoup and provides endpoints to fetch club-specific data, compare statistics between two clubs, and predict a winner based on various performance metrics.

## Features

- **Fetch Club Data:** Retrieve detailed statistics for a specified Premier League club.
- **Compare Clubs:** Compare statistics between two Premier League clubs.
- **Predict Match Outcome:** Predict the winner between two Premier League clubs based on their performance metrics.

## Requirements

- Python 3.7+
- FastAPI
- BeautifulSoup4
- Uvicorn

## Installation

1. Clone the repository:

   \```sh
   git clone https://github.com/muhtasim7/premier_league.git
   cd premier_league
   \```

2. Install the dependencies:

   \```sh
   pip install fastapi beautifulsoup4 uvicorn
   \```

## Usage

1. Run the FastAPI application:

   \```sh
   uvicorn main:app --reload
   \```

2. Open your browser and navigate to `http://127.0.0.1:8000`.

## API Endpoints

### Root Endpoint

- **URL:** `/`
- **Method:** `GET`
- **Response:** `{"Hello": "World"}`

### Fetch Club Data

- **URL:** `/fpl_club_data`
- **Method:** `GET`
- **Parameters:** `club` (string) - The name of the Premier League club.
- **Response:** JSON with detailed statistics for the specified club.

### Compare Two Clubs

- **URL:** `/fpl_club_compare`
- **Method:** `GET`
- **Parameters:** `club1` (string), `club2` (string) - The names of the two Premier League clubs to compare.
- **Response:** JSON with comparison statistics between the two clubs.

### Predict Match Outcome

- **URL:** `/fpl_who_will_win`
- **Method:** `GET`
- **Parameters:** `club1` (string), `club2` (string) - The names of the two Premier League clubs.
- **Response:** JSON with the predicted winner and relevant match statistics.

## How It Works

The application scrapes data from [FBref](https://fbref.com) using BeautifulSoup. It retrieves various performance metrics such as expected goals, progressive passing, possession percentage, and defensive statistics. These metrics are then used to compare clubs and predict match outcomes.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
