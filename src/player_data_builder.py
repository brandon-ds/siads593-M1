'''This script queries an api of FUT ratings and builds a csv file of every player in the db and their complete rankings'''

import requests 
import pandas as pd 

headers = {'X-AUTH-TOKEN': 'eb00df86-622b-4155-a102-02a1bbae6142'}

rows = [] #store player entries
for i in range(1, 954): #total of 953 pages
    print(i)
    params = {'page' : i}
    r = requests.get('https://futdb.app/api/players', headers = headers, params=params).json()
    
    df_rows = []
    for player in r['items']:

        #bio 
        id = player['id'] #api id 
        futbin_id = player['futBinId'] #incase we ever need it 
        name = player['name']
        height = player['height']
        weight = player['weight']
        age = player['age']
        club = player['club']
        league = player['league']
        nation = player['nation']
        rarity = player['rarity']
        position = player['position']
        foot = player['foot']

        #top level stats 
        attackWorkRate = player['attackWorkRate']
        defenseWorkRate = player['defenseWorkRate']
        cardColor = player['color']
        overallRating = player['rating']
        pace = player['pace']
        shooting = player['shooting']
        passing = player['passing']
        dribbling = player['dribbling']
        defending = player['defending']
        physicality = player['physicality']

        #pace breakdown: 
        pace_acceleration = player['paceAttributes']['acceleration']
        pace_sprintSpeed = player['paceAttributes']['sprintSpeed']



        #shooting breakdown 
        shooting_positioning = player['shootingAttributes']['positioning']
        shooting_finishing = player['shootingAttributes']['finishing']
        shooting_shotPower = player['shootingAttributes']['shotPower']
        shooting_longShots = player['shootingAttributes']['longShots']
        shooting_volleys = player['shootingAttributes']['volleys']
        shooting_penalties = player['shootingAttributes']['penalties']

        #passing breakdwon 
        passing_vision = player['passingAttributes']['vision']
        passing_crossing = player['passingAttributes']['crossing']
        passing_freeKickAccuracy = player['passingAttributes']['freeKickAccuracy']
        passing_shortPassing = player['passingAttributes']['shortPassing']
        passing_longPassing = player['passingAttributes']['longPassing']
        passing_curve = player['passingAttributes']['curve']

        #dribbling breakdown 
        dribbling_agility = player['dribblingAttributes']['agility']
        dribbling_balance = player['dribblingAttributes']['balance']
        dribbling_reactions = player['dribblingAttributes']['reactions']
        dribbling_ballControl = player['dribblingAttributes']['ballControl']
        dribbling_dribbling = player['dribblingAttributes']['dribbling']
        dribbling_composure = player['dribblingAttributes']['composure']

        #defending breakdown 
        defending_interceptions = player['defendingAttributes']['interceptions']
        defending_headingAccuracy = player['defendingAttributes']['headingAccuracy']
        defending_standingTackle = player['defendingAttributes']['standingTackle']
        defending_slidingTackle = player['defendingAttributes']['slidingTackle']
        defending_defenseAwareness = player['defendingAttributes']['defenseAwareness']

        #physicality breakdown 
        phsyicality_jumping = player['physicalityAttributes']['jumping']
        physicality_stamina = player['physicalityAttributes']['stamina']
        physicality_strength = player['physicalityAttributes']['strength']
        physicality_aggression = player['physicalityAttributes']['aggression']

        #goal keeper breakdown
        goalkeeper_diving = player['goalkeeperAttributes']['diving']
        goalkeeper_handling = player['goalkeeperAttributes']['handling']
        goalkeeper_kicking = player['goalkeeperAttributes']['kicking']
        goalkeeper_positioning = player['goalkeeperAttributes']['positioning']
        goalkeeper_reflexes = player['goalkeeperAttributes']['reflexes']
        goalkeeper_speed = player['goalkeeperAttributes']['speed']

        entry = [id, futbin_id, name, height, weight, age, club, league, nation, rarity, position, foot, attackWorkRate, defenseWorkRate, 
        cardColor, overallRating, pace, shooting, passing, dribbling, defending, physicality, pace_acceleration, pace_sprintSpeed, 
        shooting_positioning, shooting_finishing, shooting_shotPower, shooting_longShots, shooting_volleys, shooting_penalties, 
        passing_vision, passing_crossing, passing_freeKickAccuracy, passing_shortPassing, passing_longPassing, passing_curve, 
        dribbling_agility, dribbling_balance, dribbling_reactions, dribbling_ballControl, dribbling_dribbling, dribbling_composure, 
        defending_interceptions, defending_headingAccuracy, defending_standingTackle, defending_slidingTackle, defending_defenseAwareness,
        phsyicality_jumping, physicality_stamina, physicality_strength, physicality_aggression, goalkeeper_diving, goalkeeper_handling, 
        goalkeeper_kicking, goalkeeper_positioning, goalkeeper_reflexes, goalkeeper_speed]

        rows.append(entry)

cols = ['id', 'futbin_id', 'name', 'height', 'weight', 'age', 'club', 'league', 'nation', 'rarity', 'position', 'foot', 'attackWorkRate', 'defenseWorkRate', 
    'cardColor', 'overallRating', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physicality', 'pace_acceleration', 'pace_sprintSpeed', 
    'shooting_positioning', 'shooting_finishing', 'shooting_shotPower', 'shooting_longShots', 'shooting_volleys', 'shooting_penalties', 
    'passing_vision', 'passing_crossing', 'passing_freeKickAccuracy', 'passing_shortPassing', 'passing_longPassing', 'passing_curve', 
    'dribbling_agility', 'dribbling_balance', 'dribbling_reactions', 'dribbling_ballControl', 'dribbling_dribbling', 'dribbling_composure', 
    'defending_interceptions', 'defending_headingAccuracy', 'defending_standingTackle', 'defending_slidingTackle', 'defending_defenseAwareness',
    'phsyicality_jumping', 'physicality_stamina', 'physicality_strength', 'physicality_aggression', 'goalkeeper_diving', 'goalkeeper_handling', 
    'goalkeeper_kicking', 'goalkeeper_positioning', 'goalkeeper_reflexes', 'goalkeeper_speed']

df = pd.DataFrame(data = rows, columns = cols)
df.to_csv('FUT_player_data.csv', index = False)
