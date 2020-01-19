# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:34:28 2020

@author: Yihao Wu
"""
import Dominion
import testUtility

# Get player names
player_names = ["Annie", "*Ben"]

# number of curses and victory cards
nV, nC = testUtility.initnCnV(player_names, 0)

# Define box
box = testUtility.getBoxs(nV)
supply_order = testUtility.getSupplyOrder()
supply = testUtility.getSupply(box, player_names, nV, nC, num=0)

# initialize the trash
trash = []

# Costruct the Player objects
players = testUtility.getPlayers(player_names)

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
testUtility.displayFinalScore(players)