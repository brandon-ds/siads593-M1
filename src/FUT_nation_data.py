"""This script gets the leauge IDs the API uses in the player data"""

import requests
import pandas as pd

headers = {"X-AUTH-TOKEN": "eb00df86-622b-4155-a102-02a1bbae6142"}

rows = []
for i in range(1, 51):
    print(i)
    params = {"page": i}
    r = requests.get(
        "https://futdb.app/api/nations", headers=headers, params=params
    ).json()

    for league in r["items"]:
        id = league["id"]
        name = league["name"]
        rows.append([id, name])

df = pd.DataFrame(data=rows, columns=["id", "LeagueName"])
df.to_csv("league_ids.csv", index=False)
