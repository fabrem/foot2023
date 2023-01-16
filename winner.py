import pandas as pd
import numpy as np
import re
from writer import write_to_index_html_file

POINTS_FOR_OVER_UNDER = 1
POINTS_FOR_CORRECT_SCORE = 2
POINTS_FOR_GOOD_TEAM = 3

# important, faire (winner, loser) dans les scores
REAL_LIFE_DATA = [('niners', (41, 23)), ('jaguars', (31, 30)), ('bills', (34,13)),
           ('giants (beurk)', (24,31)), ('bengals', (0,0)), ('buccs', (0,0))]
           
OVER_UNDERS = [42, 47.5, 43.5, 48, 40.5, 45.5]

excel = pd.read_excel("./excel/week1-temp.xlsx")

# changer les chiffres pour adapt au excel
df = excel.T[3:].T

score_final_chaque_ti_gars = np.zeros(9)
noms_des_ti_gars = excel.iloc[:,1]

good_score_winners_for_each_game = [[] for i in range(len(REAL_LIFE_DATA))]
lowest_score_in_absolute = np.inf * np.ones(len(OVER_UNDERS))

for ti_gars_number, row in df.iterrows():

    for index, cell in enumerate(row):
        cell = cell.lower()
        if index % 3 == 0: # good team
            if cell == REAL_LIFE_DATA[index // 3][0]:
                score_final_chaque_ti_gars[ti_gars_number] += POINTS_FOR_GOOD_TEAM

        if index % 3 == 1: # good score
            previous_cell = row[index - 1].lower()
            good_team = previous_cell == REAL_LIFE_DATA[index // 3][0]

            if good_team:
                score_ti_gars = re.findall(r'\b\d+\b', cell)
                abs_total_score_avec_real_life = abs(int(score_ti_gars[0]) - REAL_LIFE_DATA[index // 3][1][0]) +  \
                   abs(int(score_ti_gars[1]) - REAL_LIFE_DATA[index // 3][1][1])

                if abs_total_score_avec_real_life  == lowest_score_in_absolute[index // 3]:
                   good_score_winners_for_each_game[index // 3] += [ti_gars_number]
                elif abs_total_score_avec_real_life < lowest_score_in_absolute[index // 3]:
                    good_score_winners_for_each_game[index // 3] = [ti_gars_number]
                    lowest_score_in_absolute[index // 3] = abs_total_score_avec_real_life

        if index % 3 == 2: # over under
            if REAL_LIFE_DATA[index // 3][1][0] + REAL_LIFE_DATA[index // 3][1][1] > OVER_UNDERS[index//3] and cell == "over":
                score_final_chaque_ti_gars[ti_gars_number] += POINTS_FOR_OVER_UNDER
            elif REAL_LIFE_DATA[index // 3][1][0] + REAL_LIFE_DATA[index // 3][1][1] < OVER_UNDERS[index//3] and cell == "under":
                score_final_chaque_ti_gars[ti_gars_number] += POINTS_FOR_OVER_UNDER
            else:
                pass # no points
    

# add points for good score
for plusieurs_ti_gars in good_score_winners_for_each_game:
    for ti_gars in plusieurs_ti_gars:
        score_final_chaque_ti_gars[ti_gars] += POINTS_FOR_CORRECT_SCORE

# print('======= SCOREBOARD =======')
scoreboard = [i for i in zip(list(noms_des_ti_gars), score_final_chaque_ti_gars)]
formatted_scoreboard = [f"{a}: {b}" for a, b in [i for i in scoreboard]]

for row in formatted_scoreboard:
    print(row)

print('======= WINNERS OF SCORE =======')
ti_gars_par_numero = {i:j for i, j in zip([i for i in range(len(noms_des_ti_gars))], list(noms_des_ti_gars))}
for index ,i in enumerate(good_score_winners_for_each_game):
    print("GAME " + str(index + 1))
    for j in i:
        print(ti_gars_par_numero[j])

write_to_index_html_file(scoreboard)
