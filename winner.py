import pandas as pd
import numpy as np
import re
from writer import frais_new_writer, write_to_index_html_file
from fetch_todays_games import fetch_todays_game, fetch_todays_game_charlem
from read_drive_sheets import read_drive_sheets

# Important, faire (winner, loser) dans les scores
# TODO faire que ca ecrit dans un fichier... Pas automatique
WEEK1_DATA = [('niners', (41, 23)), ('jaguars', (31, 30)), ('bills', (34, 13)),
              ('giants (beurk)', (24, 31)), ('bengals', (24, 17)), ('cowboys', (31, 14))]
WEEK2_DATA = [("chiefs", (27, 20)), ("eagles", (38, 7)),
              ("bengals", (27, 10)), ("niners", (19, 12))]
WEEK3_DATA = fetch_todays_game_charlem()
WEEK3_DATA.reverse()
WEEK4_DATA = []

ALL_DATA_TEMP = WEEK1_DATA + WEEK2_DATA + WEEK3_DATA + WEEK4_DATA
ALL_DATA = []

# REMOVE GAMES IF THE SCORE IS 0-0, THEY ARE NOT TO BE CONSIDERED YET
for game in ALL_DATA_TEMP:
    if sum(game[1]) != 0:
        ALL_DATA.append(game)
print(ALL_DATA)


LEN_EACH_WEEK = [len(WEEK1_DATA), len(WEEK2_DATA), len(WEEK3_DATA), len(WEEK4_DATA)]

# WEEK 1 SCORING
POINTS_FOR_OVER_UNDER_WEEK_1 = 1
POINTS_FOR_CORRECT_SCORE_WEEK_1 = 2
POINTS_FOR_GOOD_TEAM_WEEK_1 = 3

# WEEK 2 SCORING
POINTS_FOR_OVER_UNDER_WEEK_2 = 1
POINTS_FOR_CORRECT_SCORE_WEEK_2 = 2
POINTS_FOR_GOOD_TEAM_WEEK_2 = 5

# WEEK 3 SCORING
POINTS_FOR_OVER_UNDER_WEEK_3 = 2
POINTS_FOR_CORRECT_SCORE_WEEK_3 = 3
POINTS_FOR_GOOD_TEAM_WEEK_3 = 8

# WEEK 4 SCORING
POINTS_FOR_OVER_UNDER_WEEK_4 = 2
POINTS_FOR_CORRECT_SCORE_WEEK_4 = 5
POINTS_FOR_GOOD_TEAM_WEEK_4 = 13

STARTING_INDEX = 3

POINTS = [[POINTS_FOR_GOOD_TEAM_WEEK_1, POINTS_FOR_CORRECT_SCORE_WEEK_1, POINTS_FOR_OVER_UNDER_WEEK_1],
          [POINTS_FOR_GOOD_TEAM_WEEK_2, POINTS_FOR_CORRECT_SCORE_WEEK_2,
              POINTS_FOR_OVER_UNDER_WEEK_2],
          [POINTS_FOR_GOOD_TEAM_WEEK_3, POINTS_FOR_CORRECT_SCORE_WEEK_3,
              POINTS_FOR_OVER_UNDER_WEEK_3],
          [POINTS_FOR_GOOD_TEAM_WEEK_4, POINTS_FOR_CORRECT_SCORE_WEEK_4, POINTS_FOR_OVER_UNDER_WEEK_4]]

OVER_UNDERS = [42, 47.5, 43.5, 48, 40.5, 45.5, 53, 48, 49, 46, 46, 48]
NUMBER_OF_PLAYERS = 9



def calculate_scoreboard(df, score_final_chaque_ti_gars, noms_des_ti_gars, number_of_games_to_consider):
    good_score_winners_for_each_game = [[] for i in range(number_of_games_to_consider)]
    lowest_score_in_absolute = np.inf * np.ones(len(OVER_UNDERS))
    for ti_gars_number, row in enumerate(df.T[1:number_of_games_to_consider*3 + 1].T):

        for index, cell in enumerate(row):

            cell = cell.lower()
            points_for_game = []

            game_number = index // 3 + 1

            # CHECK FOR THE GAME NUMBER, USED TO ADD THE CORRECT POINTS AFTER EACH ROUND (THEY INCREASE)
            if game_number <= len(WEEK1_DATA):
                points_for_game = POINTS[0]

            elif game_number <= len(WEEK2_DATA) + len(WEEK1_DATA):
                points_for_game = POINTS[1]

            elif game_number <= len(WEEK3_DATA) + len(WEEK2_DATA) + len(WEEK1_DATA):
                points_for_game = POINTS[2]

            elif game_number <= len(WEEK4_DATA) + len(WEEK3_DATA) + len(WEEK2_DATA) + len(WEEK1_DATA):
                points_for_game = POINTS[3]

            else:
                raise Exception("wat")

            if index % 3 == 0:  # good team
                if cell == ALL_DATA[index // 3][0]:
                    score_final_chaque_ti_gars[ti_gars_number] += points_for_game[0]

            if index % 3 == 1:  # good score
                previous_cell = row[index - 1].lower()
                good_team = previous_cell == ALL_DATA[index // 3][0]

                if good_team:
                    score_ti_gars = re.findall(r'\b\d+\b', cell)
                    score_team_gagnante = score_ti_gars[0]
                    score_team_perdante = score_ti_gars[1]
                    if score_team_perdante > score_team_gagnante:
                        temp = score_team_gagnante
                        score_team_gagnante = score_team_perdante
                        score_team_perdante = temp

                    abs_total_score_avec_real_life = abs(int(score_team_gagnante) - ALL_DATA[index // 3][1][0]) +  \
                        abs(int(score_team_perdante) - ALL_DATA[index // 3][1][1])

                    if abs_total_score_avec_real_life == lowest_score_in_absolute[index // 3]:
                        good_score_winners_for_each_game[index //
                                                        3] += [ti_gars_number]
                    elif abs_total_score_avec_real_life < lowest_score_in_absolute[index // 3]:
                        good_score_winners_for_each_game[index //
                                                        3] = [ti_gars_number]
                        lowest_score_in_absolute[index //
                                                3] = abs_total_score_avec_real_life

            if index % 3 == 2:  # over under
                if ALL_DATA[index // 3][1][0] + ALL_DATA[index // 3][1][1] > OVER_UNDERS[index//3] and cell == "over":
                    score_final_chaque_ti_gars[ti_gars_number] += points_for_game[2]
                elif ALL_DATA[index // 3][1][0] + ALL_DATA[index // 3][1][1] < OVER_UNDERS[index//3] and cell == "under":
                    score_final_chaque_ti_gars[ti_gars_number] += points_for_game[2]
                else:
                    pass  # no points


    # ADD POINTS FOR GOOD SCORE (HAS TO DO AFTER)
    for index, plusieurs_ti_gars in enumerate(good_score_winners_for_each_game):
        for ti_gars in plusieurs_ti_gars:
            game_number = index + 1

            # CHECK FOR THE GAME NUMBER
            if game_number <= len(WEEK1_DATA):
                points_for_game = POINTS[0][1]

            elif game_number <= len(WEEK2_DATA) + len(WEEK1_DATA):
                points_for_game = POINTS[1][1]

            elif game_number <= len(WEEK3_DATA) + len(WEEK2_DATA) + len(WEEK1_DATA):
                points_for_game = POINTS[2][1]

            elif game_number <= len(WEEK4_DATA) + len(WEEK3_DATA) + len(WEEK2_DATA) + len(WEEK1_DATA):
                points_for_game = POINTS[3][1]

            score_final_chaque_ti_gars[ti_gars] += points_for_game
    

    # print('======= WINNERS OF SCORE =======')
    # ti_gars_par_numero = {i: j for i, j in zip(
    #     [i for i in range(len(noms_des_ti_gars))], list(noms_des_ti_gars))}
    # for index, i in enumerate(good_score_winners_for_each_game):
    #     print("GAME " + str(index + 1))
    #     for j in i:
    #         print(ti_gars_par_numero[j])



def print_and_save_scoreboard(noms_des_ti_gars, score_final_chaque_ti_gars, fleches):
    scoreboard, games = print_scoreboard(noms_des_ti_gars, score_final_chaque_ti_gars)
    order_list=[x[0] for x in scoreboard]
    sorted_fleches = sorted(fleches, key=lambda x: order_list.index(x[0]))
    frais_new_writer(scoreboard, games, sorted_fleches)



def print_scoreboard(noms_des_ti_gars, score_final_chaque_ti_gars):

    print('======= SCOREBOARD =======')
    scoreboard = [i for i in zip(
        list(noms_des_ti_gars), score_final_chaque_ti_gars)]

    # SORT THE SCOREBOARD
    scoreboard = sorted(scoreboard, key=lambda x: x[1], reverse=True)

    # FORMAT THE SCOREBOARD FOR THE TERMINAL
    formatted_scoreboard = [f"{a}: {b}" for a, b in [i for i in scoreboard]]

    for row in formatted_scoreboard:
        print(row)
    
    games = fetch_todays_game()

    return scoreboard, games


def main():
    df = read_drive_sheets()

    # TODO get this shit automatically
    CURRENT_WEEK = 3

    NUMBER_OF_GAMES_TO_CONSIDER = len(ALL_DATA)
    NUMBER_OF_GAMES_TO_CONSIDER_PREVIOUS_WEEK = sum(LEN_EACH_WEEK[:(CURRENT_WEEK - 1)])
    
    score_final_chaque_ti_gars = np.zeros(NUMBER_OF_PLAYERS)
    score_final_chaque_ti_gars_semaine_davant = np.zeros(NUMBER_OF_PLAYERS)
    noms_des_ti_gars = df[:, 0]

    calculate_scoreboard(df, score_final_chaque_ti_gars, noms_des_ti_gars, NUMBER_OF_GAMES_TO_CONSIDER)
    calculate_scoreboard(df, score_final_chaque_ti_gars_semaine_davant, noms_des_ti_gars, NUMBER_OF_GAMES_TO_CONSIDER_PREVIOUS_WEEK)

    fleches = list(zip(noms_des_ti_gars, score_final_chaque_ti_gars - score_final_chaque_ti_gars_semaine_davant))

    print_and_save_scoreboard(noms_des_ti_gars, score_final_chaque_ti_gars, fleches)
    print_scoreboard(noms_des_ti_gars, score_final_chaque_ti_gars_semaine_davant)


if __name__ == "__main__":
    main()
