import json
import requests
from datetime import datetime

def fetch_todays_game():
    res = requests.get('http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard')
    response = json.loads(res.text)
    path_to_games = "events"
    first_team_score_path = ['competitions', 0, 'competitors', 0]
    second_team_score_path = ['competitions', 0, 'competitors', 1]
    events = response[path_to_games]
    game_name = []
    game_scores = []

    for index in range(len(events)):
        game_name.append(events[index]['name'])

    for single_game in events:
        first_team_score = single_game
        second_team_score = single_game

        for subpath in first_team_score_path:
            first_team_score = first_team_score[subpath]
        for subpath in second_team_score_path:
            second_team_score = second_team_score[subpath]

        game_scores.append(((first_team_score['team']['displayName'], first_team_score['score']), (second_team_score['team']['displayName'], second_team_score['score'])))

    formatted_scores = []
    for i in range(len(game_scores)):
        formatted_scores.append(game_scores[i][0][0] + " " + game_scores[i][0][1] + " - " + game_scores[i][1][1] + " " + game_scores[i][1][0])

    return formatted_scores

def fetch_todays_game_charlem():
    res = requests.get('http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard')
    response = json.loads(res.text)
    path_to_games = "events"
    first_team_score_path = ['competitions', 0, 'competitors', 0]
    second_team_score_path = ['competitions', 0, 'competitors', 1]
    events = response[path_to_games]
    game_time = []
    game_scores = []

    # for index in range(len(events)):

    for index, single_game in enumerate(events):
        first_team_score = single_game
        second_team_score = single_game
        game_time = events[index]['date']

        for subpath in first_team_score_path:
            first_team_score = first_team_score[subpath]
        for subpath in second_team_score_path:
            second_team_score = second_team_score[subpath]

        game_scores.append(((first_team_score['team']['displayName'], first_team_score['score']), (second_team_score['team']['displayName'], second_team_score['score']), game_time))

    formatted_matches = []
    for match in game_scores:
        team1, team2, game_time = match
        if int(team1[1]) > int(team2[1]):
            formatted_matches.append((team1[0].split(" ")[-1].lower(), (int(team1[1]), int(team2[1])), match[-1]))
        else:
            formatted_matches.append((team2[0].split(" ")[-1].lower(), (int(team2[1]), int(team1[1])), match[-1]))
        
    # sort by key here, match time
    return sorted(formatted_matches, key=lambda x: datetime.strptime(x[-1],"%Y-%m-%dT%H:%MZ"))

# print(fetch_todays_game_charlem())
