# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import sys
import csv


def sort_goals_in_csv(csv_file):
	with open(csv_file) as csvfile:
		reader = csv.DictReader(csvfile)
		points = []
		for row in reader:
			spread = abs(int(row['Goals']) - int(row['Goals Allowed']))
			team = row['Team']
			points.append((team, spread))
	return sorted(points, key=lambda tup: tup[1])

def main():
    arg = sys.argv[1]

    if not arg:
        print('ERROR: include csv file as argument')
        sys.exit(1)

    goal_spread_list = sort_goals_in_csv(arg)
    team = goal_spread_list[0][0]
    print(team)
  
if __name__ == '__main__':
  main()