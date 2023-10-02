import os
import pandas as pd

BASE_DIR = '../data/Transfer_fee_by_year/'
years = [str(year) for year in range(1992, 2022)]
data_by_league = {}

for year in years:
    year_path = os.path.join(BASE_DIR, year)
    print(f"Checking directory: {year_path}")

    if os.path.isdir(year_path):
        for file_name in os.listdir(year_path):
            if file_name.endswith('.csv'):
                league = file_name.split('.')[0]
                file_path = os.path.join(year_path, file_name)

                df = pd.read_csv(file_path)
                df['Year'] = year

                if league in data_by_league:
                    data_by_league[league] = pd.concat(
                        [data_by_league[league], df], ignore_index=True)
                else:
                    data_by_league[league] = df

for league, data in data_by_league.items():
    output_path = os.path.join(BASE_DIR, f'combined_{league}.csv')
    data.to_csv(output_path, index=False)
