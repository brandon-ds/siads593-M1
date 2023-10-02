import requests
import pandas as pd

HEADERS = {"X-AUTH-TOKEN": "eb00df86-622b-4155-a102-02a1bbae6142"}
URL = "https://futdb.app/api/players"
COLUMNS = [
    "id",
    "futbin_id",
    "name",
    "height",
    "weight",
    "age",
    "club",
    "league",
    "nation",
    "rarity",
    "position",
    "foot",
    "attackWorkRate",
    "defenseWorkRate",
    "cardColor",
    "overallRating",
    "pace",
    "shooting",
    "passing",
    "dribbling",
    "defending",
    "physicality",
    "pace_acceleration",
    "pace_sprintSpeed",
    "shooting_positioning",
    "shooting_finishing",
    "shooting_shotPower",
    "shooting_longShots",
    "shooting_volleys",
    "shooting_penalties",
    "passing_vision",
    "passing_crossing",
    "passing_freeKickAccuracy",
    "passing_shortPassing",
    "passing_longPassing",
    "passing_curve",
    "dribbling_agility",
    "dribbling_balance",
    "dribbling_reactions",
    "dribbling_ballControl",
    "dribbling_dribbling",
    "dribbling_composure",
    "defending_interceptions",
    "defending_headingAccuracy",
    "defending_standingTackle",
    "defending_slidingTackle",
    "defending_defenseAwareness",
    "phsyicality_jumping",
    "physicality_stamina",
    "physicality_strength",
    "physicality_aggression",
    "goalkeeper_diving",
    "goalkeeper_handling",
    "goalkeeper_kicking",
    "goalkeeper_positioning",
    "goalkeeper_reflexes",
    "goalkeeper_speed",
]


def fetch_players(page):
    params = {"page": page}
    response = requests.get(URL, headers=HEADERS, params=params, verify=False)
    response.raise_for_status()  # This will raise an exception for HTTP errors
    return response.json()["items"]


def player_data_generator(pages):
    for page in range(1, pages + 1):
        print(page)
        players = fetch_players(page)
        for player in players:
            yield [
                player.get(key)
                if "Attributes" not in key
                else player.get(key.split("_")[0] + "Attributes", {}).get(
                    key.split("_")[1]
                )
                for key in COLUMNS
            ]


def main():
    rows = list(player_data_generator(2))  # Update the number of pages as needed
    df = pd.DataFrame(data=rows, columns=COLUMNS)
    df.to_csv("FUT_player_data.csv", index=False)


if __name__ == "__main__":
    main()
