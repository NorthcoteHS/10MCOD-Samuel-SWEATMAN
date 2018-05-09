"""

Prog:   HockeyTriviaGame.py
name:   Sam Sweatman
Date:
desc:   Hockey trivia game
"""


#list of answers
hockeyquizanswer = ['Wayne Gretzky', '6 ounces', '31', 'Pittsburgh Penguins', '1917']
#loop through list of questions
hockeyquiz = ['who has the most points in NHL?', 'how much does a puck weigh?', 'how many teams are in the NHL?', 'which team won the stanley cup in 2017?', 'What year did the NHL games officially start?']


for i,question in enumerate(hockeyquiz):
    inp=input(question)
    if inp == (hockeyquiz[i]):
        print('Correct!')
    else:
        print('incorrect!')
