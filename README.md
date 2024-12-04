# NBA Data Analysis Tool

A Python-based tool for fetching and analyzing NBA statistics using the official NBA Stats API. This project provides functionality to retrieve both player and team statistics, with capabilities for data visualization and analysis.

## Features

- Fetch comprehensive NBA player statistics
- Retrieve team-level statistics
- Data visualization with correlation heatmaps
- Customizable query parameters (season, player position, team, etc.)
- Streamlit web interface for interactive data exploration

## Installation

1. Clone this repository:
```bash
git clone https://github.com/jagalipeau/Ballin
cd Ballin
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Player Statistics

```python
from stats_2 import player_stats

# Get current season's player stats
df = player_stats()

# Get stats for a specific season
df = player_stats(Season="2022-23")

# Filter by additional parameters
df = player_stats(
    Season="2023-24",
    PlayerPosition="G",  # Guards only
    Conference="East"    # Eastern Conference
)
```

### Team Statistics

```python
from stats_2 import team_stats

# Get current season's team stats
df = team_stats()

# Get stats for specific parameters
df = team_stats(
    Conference="West",
    SeasonType="Regular Season",
    DateFrom="2023-12-01"
)
```

### Data Visualization

The project includes a Streamlit-based visualization tool (`eda.py`) that creates correlation heatmaps for various statistics as an example use case:

```bash
streamlit run eda.py
```

## Available Parameters

### Player Stats Parameters
- `Season`: NBA season (e.g., "2023-24")
- `PlayerPosition`: Position filter (e.g., "G", "F", "C")
- `Conference`: Conference filter ("East" or "West")
- `Division`: Division filter
- `TeamID`: Specific team ID
- `Country`: Player's country
- `College`: Player's college
- And many more...

### Team Stats Parameters
- Similar parameters as player stats, focused on team-level data
- Additional filters for game segments, periods, and team-specific metrics

## Data Output

Both player and team statistics are returned as Pandas DataFrames, making it easy to perform further analysis or export the data.

## Documentation Files

### stats_2.md
Contains detailed documentation for the main module functions:
- Complete parameter documentation for `player_stats()` and `team_stats()`
- Valid input values for each parameter
- Special formatting requirements (e.g., college names format)
- Comprehensive list of supported colleges, conferences, and countries

### eda.md
Contains detailed documentation about the DataFrame structure:
- Complete list of all columns in the player statistics DataFrame
- Description of each statistic and metric
- Data types and formats for each field
- Explanation of statistical calculations and abbreviations

## Dependencies

- requests>=2.31.0
- pandas>=2.1.4
- streamlit>=1.29.0
- seaborn>=0.13.0
- matplotlib>=3.8.2
- numpy>=1.26.2

## Notes

- This tool uses the official NBA Stats API
- Some API endpoints may have rate limiting
- The tool automatically handles authentication cookies for API access

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.


