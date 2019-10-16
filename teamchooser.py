from random import choice

players = ['Henry','Bechkam','Zidane','Gerrard']

teamA = []
teamB = []

while len (players) > 0:

 playerA = choice(players)
 print(playerA)
 teamA.append(playerA)
 players.remove(playerA)
 print('Players Left:', players)

 playerB = choice(players)
 print(playerB)
 teamB.append(playerB)
 players.remove(playerB)
 print('Players Left:', players)

 print('Team A:', teamA)
 print('Team B:', teamB)