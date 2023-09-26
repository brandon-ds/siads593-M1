import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def players_valuations():
    df_players = pd.read_csv('G:\My Drive\Github\siads593-M1\data\players.csv')
    df_players = df_players[['player_id', 'name']]
    
    df_players_valuations = pd.read_csv('G:\My Drive\Github\siads593-M1\data\player_valuations.csv')
    df_players_valuations = pd.merge(df_players, df_players_valuations, on='player_id', how='left')
    df_players_valuations.drop(columns=['player_id', 'datetime', 'date', 'dateweek', 'n', 'player_club_domestic_competition_id'], inplace=True)

    # There are multiple valuations per person due to multiple records or multiple valuations after certain assesments, etc..
    # So, we will take the average per year.  
    pd.set_option('display.float_format', '{:.2f}'.format)
    df_value_averaged = df_players_valuations.groupby(['name', 'last_season']).agg(average_value=('market_value_in_eur', 'mean')).reset_index()

    return df_value_averaged

preprocessed_valuations = players_valuations()
preprocessed_valuations.to_csv('G:\My Drive\Github\siads593-M1\data\preprocessed_valuations.csv')

