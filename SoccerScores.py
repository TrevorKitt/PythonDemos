"""
You are given a text file called Scores.txt that contains scores from a series of soccer games.
Each line in the file represents the score from 1 game.
In the line, it lists the names of players who scored goals in that game and how many goals that player scored.
Here is an example:

Bob:1,Minnie:2,Jeff:1
Amy:3,Bob:1,Minnie:1
Bob:2,Jeff:1

In this example, the team played 3 games.
In the first game, Bob scored 1 goal, Minnie scored 2 goals and Jeff scored 1 goal.
In the second game, Amy scored 3 goals, Bob scored 1 goal and Minnie scored 1 goal.
In the third game, Bob scored 2 goals and Jeff scored 1 goal.

Write a program that can read a text file like this and print out the names of all the players along with the total number of goals scored by that player.
The names should be printed starting with the player who scored the most goals and continuing in descending order of goals scored.
If two or more players are tied for the same total score, print their names in alphabetical order. For example, the above scores would be printed as follows:

Bob:4
Amy: 3
Minnie: 3
Jeff:2

"""

#Requirement 1 - List every player who shows up in the text file
#Requirement 2 - List total scores beside each player name
#Requirement 3 - List player names in order of descending total scores
#Requirement 4 - for players with tied scores, player names should be listed alphabetically

#Goal data structure
# playerdict = {
#     'Amy' : 3,
#     'Bob' : 4,
#     'Minnie' : 3,
#     'Jeff' : 2
# }

import csv

playerdict = {}

#Score looks like "Bob:2"
def process_score(score):
    name, goals = score.split(':')
    if name in playerdict:
        playerdict[name] += int(goals)
    else:
        playerdict[name] = int(goals)

def read_score_file(filename):
    with open(filename, 'r') as file:
        csvreader = csv.reader(file, delimiter=',')
        for row in csvreader:
            for score in row:
                try:
                    process_score(score)
                except:
                    print("Unable to process score {} in row {}.Continuing to process other scores".format(score, row))

def getScore(tuple):
    return tuple[1]

def getName(tuple):
    return tuple[0]

def sort_players(dict):
    player_list = []
    for player in dict.keys():
        player_list.append((player, dict[player]))
    player_list.sort(key=getName)
    player_list.sort(key=getScore, reverse=True)
    return player_list

def print_player_scores(filename):
    read_score_file(filename)
    player_list = sort_players(playerdict)
    for player_tuple in player_list:
        print(player_tuple[0] + ':' + str(player_tuple[1]))

print_player_scores('Scores.txt')


