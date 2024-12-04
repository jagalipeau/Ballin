from requests import get
import pandas as pd


def player_stats(
    College="",
    Conference="",
    Country="",
    DateFrom="",
    DateTo="",
    Division="",
    DraftPick="",
    DraftYear="",
    GameScope="",
    GameSegment="",
    Height="",
    ISTRound="",
    LastNGames="0",
    LeagueID="00",
    Location="",
    MeasureType="Base",
    Month="0",
    OpponentTeamID="0",
    Outcome="",
    PORound="0",
    PaceAdjust="N",
    PerMode="PerGame",
    Period="0",
    PlayerExperience="",
    PlayerPosition="",
    PlusMinus="N",
    Rank="N",
    Season="2023-24",
    SeasonSegment="",
    SeasonType="Regular%20Season",
    ShotClockRange="",
    StartBench="",
    TeamID="0",
    VsConference="",
    VsDivision="",
    Weight="",
):
    url = f"https://stats.nba.com/stats/leaguedashplayerstats?College={College}&Conference={Conference}&Country={Country}&DateFrom={DateFrom}&DateTo={DateTo}&Division={Division}&DraftPick={DraftPick}&DraftYear={DraftYear}&GameScope={GameScope}&GameSegment={GameSegment}&Height={Height}&ISTRound={ISTRound}&LastNGames={LastNGames}&LeagueID={LeagueID}&Location={Location}&MeasureType={MeasureType}&Month={Month}&OpponentTeamID={OpponentTeamID}&Outcome={Outcome}&PORound={PORound}&PaceAdjust={PaceAdjust}&PerMode={PerMode}&Period={Period}&PlayerExperience={PlayerExperience}&PlayerPosition={PlayerPosition}&PlusMinus={PlusMinus}&Rank={Rank}&Season={Season}&SeasonSegment={SeasonSegment}&SeasonType={SeasonType}&ShotClockRange={ShotClockRange}&StarterBench={StartBench}&TeamID={TeamID}&VsConference={VsConference}&VsDivision={VsDivision}&Weight={Weight}"

    payload = {}
    cookie_value = get("https://www.nba.com").cookies["_abck"]
    headers = {
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-site",
        "Origin": "https://www.nba.com",
        "Referer": "https://www.nba.com/",
        "Connection": "keep-alive",
        "Host": "stats.nba.com",
        "Sec-Fetch-Mode": "cors",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Fetch-Dest": "empty",
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": f"_abck={cookie_value}",
    }

    # response = requests.request("GET", url, headers=headers, data=payload)
    response = get(url, headers=headers).json()

    # resturns headers as a list
    header = response["resultSets"][0]["headers"]

    # Returns data for each player
    rowSet = response["resultSets"][0]["rowSet"]

    df = pd.DataFrame.from_records(rowSet, columns=header)

    return df


def team_stats(
    Conference="",
    DateFrom="",
    DateTo="",
    Division="",
    GameScope="",
    GameSegment="",
    Height="",
    ISTRound="",
    LastNGames="0",
    LeagueID="00",
    Location="",
    MeasureType="Base",
    Month="0",
    OpponentTeamID="0",
    Outcome="",
    PORound="0",
    PaceAdjust="N",
    PerMode="PerGame",
    Period="0",
    PlayerExperience="",
    PlayerPosition="",
    PlusMinus="N",
    Rank="N",
    Season="2023-24",
    SeasonSegment="",
    SeasonType="Regular%20Season",
    ShotClockRange="",
    StarterBench="",
    TeamID="0",
    TwoWay="0",
    VsConference="",
    VsDivision="",
):
    url = f"https://stats.nba.com/stats/leaguedashteamstats?Conference={Conference}&DateFrom={DateFrom}&DateTo={DateTo}&Division={Division}&GameScope={GameScope}&GameSegment={GameSegment}&Height={Height}&ISTRound={ISTRound}&LastNGames={LastNGames}&LeagueID={LeagueID}&Location={Location}&MeasureType={MeasureType}&Month={Month}&OpponentTeamID={OpponentTeamID}&Outcome={Outcome}&PORound={PORound}&PaceAdjust={PaceAdjust}&PerMode={PerMode}&Period={Period}&PlayerExperience={PlayerExperience}&PlayerPosition={PlayerPosition}&PlusMinus={PlusMinus}&Rank={Rank}&Season={Season}&SeasonSegment={SeasonSegment}&SeasonType={SeasonType}&ShotClockRange={ShotClockRange}&StarterBench={StarterBench}&TeamID={TeamID}&TwoWay={TwoWay}&VsConference={VsConference}&VsDivision={VsDivision}"
    payload = {}
    cookie_value = get("https://www.nba.com").cookies["_abck"]
    headers = {
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-site",
        "Origin": "https://www.nba.com",
        "Referer": "https://www.nba.com/",
        "Connection": "keep-alive",
        "Host": "stats.nba.com",
        "Sec-Fetch-Mode": "cors",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Fetch-Dest": "empty",
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": f"_abck={cookie_value}",
    }
    # response = requests.request("GET", url, headers=headers, data=payload)
    response = get(url, headers=headers).json()

    # resturns headers as a list
    header = response["resultSets"][0]["headers"]

    # Returns data for each player
    rowSet = response["resultSets"][0]["rowSet"]

    df = pd.DataFrame.from_records(rowSet, columns=header)
    return df
