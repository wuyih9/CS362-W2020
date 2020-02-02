from unittest import TestCase
import unittest
import Dominion

class TestAction_Card(TestCase):
    def setUp(self):
        self.ac = Dominion.Action_card("ac",cost = 10,actions = 1,buys = 3,coins = 30,cards = 7)
        self.player = Dominion.Player("Annie")

    def test_init(self):
        self.assertEqual(3,self.ac.buys)
        self.assertEqual(1,self.ac.actions)
        self.assertNotEqual(2,self.ac.coins)
        self.ac.actions += 2
        self.assertEqual(3,self.ac.actions)
        self.ac.cost = 100
        self.assertEqual(100,self.ac.cost)
        self.ac.buys -= 1
        self.assertEqual(2,self.ac.buys)
        self.assertEqual(7,self.ac.cards)

    def test_use(self):
        self.player.hand.append(self.ac)
        self.ac.use(self.player,[])
        self.assertEqual(1,len(self.player.played))
        self.assertNotEqual(0,len(self.player.hand))
        pass
    def test_augment(self):
        self.player.actions = 0
        self.player.buys = 0
        self.player.purse = 0
        self.ac.augment(self.player)
        self.assertEqual(1, self.player.actions)
        self.assertEqual(3, self.player.buys)
        self.assertEqual(30, self.player.purse)
        pass
    pass

class TestGameOver(TestCase):
    def test_game_over(self):
        supply = {}
        supply["Copper"] = [Dominion.Copper()] * 6
        supply["Silver"] = [Dominion.Silver()] * 40
        supply["Gold"] = [Dominion.Gold()] * 0
        supply["Estate"] = [Dominion.Estate()] * 7
        supply["Duchy"] = [Dominion.Duchy()] * 0
        supply["Province"] = [Dominion.Province()] * 6
        supply["Curse"] = [Dominion.Curse()] * 0
        self.assertEqual(True,Dominion.gameover(supply))
        supply["Curse"] = [Dominion.Curse()] * 5
        self.assertEqual(False, Dominion.gameover(supply))
        supply["Province"] = [Dominion.Province()] * 0
        self.assertEqual(True, Dominion.gameover(supply))

        pass


class TestPlayer(TestCase):
    def setUp(self):
        self.player = Dominion.Player("Annie")

    def test_action_balance(self):
        self.assertEqual(0.0,self.player.action_balance())
        pass
    def test_calcpoints(self):
        points = self.player.calcpoints()
        self.assertEqual(3,points)
        self.player.deck = [Dominion.Copper()] * 7
        self.player.calcpoints()
        self.player.deck = []
        self.player.calcpoints()

        pass
    def test_draw(self):
        self.player.draw()
        self.player.draw(dest = [Dominion.Copper()]*7)
        self.assertEqual(3,len(self.player.deck))
        self.player.deck = []
        self.player.draw(dest = [Dominion.Copper()]*7)
        pass
    def test_cardsummary(self):
        summary = self.player.cardsummary()
        self.assertEqual(3,len(summary))
        self.player.deck = [Dominion.Copper()] * 7
        self.player.cardsummary()
        pass
    pass


if __name__ == '__main__':
    unittest.main()
