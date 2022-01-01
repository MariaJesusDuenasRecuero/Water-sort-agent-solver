#!/usr/bin/python3
#-*-coding: utf-8; mode:python-*-
from classes.Bottle import *
import copy

class State(): 
    def __init__(self, list_bottles = None):
        self.bottles = list_bottles

    def __len__(self):
        return len(self.bottles)

    def is_Possible_Action(self, originBottle, destBottle):
        if originBottle.current_amount == 0:
            return False
        if (destBottle.current_amount == 0) and destBottle.isPossible_to_add_quantity(originBottle) == True:
            return True
        if (destBottle.getColourLast() == originBottle.getColourLast()) and destBottle.isPossible_to_add_quantity(originBottle) == True:
            return True
        return False

    def action(self, OriginBottle, DestBottle):
        DestBottle.insert_liquid(OriginBottle.liquids[0])
        OriginBottle.remove_liquid()

    def createCopy(self, la):
        return copy.deepcopy(la)

    def successor_fn(self, initState):
        successors_list = []
        bottle_list = self.createCopy(initState.bottles)
        for origin in range(len(bottle_list)):
            for destination in range(len(bottle_list)):
                if (origin != destination) and self.is_Possible_Action(bottle_list[origin], bottle_list[destination]):
                    quantity = bottle_list[origin].getQuantityLast()
                    self.action(bottle_list[origin], bottle_list[destination])
                    successors_list.append([[origin, destination, quantity], State(bottle_list), 1])
                    bottle_list = self.createCopy(initState.bottles)
        return successors_list

    def isGoal(self):
        inside_colours = []
        for bottle in self.bottles:
            if len(bottle.colours) == 1:
                if bottle.getColourLast() in inside_colours:
                    return False
                else:
                    inside_colours.append(bottle.getColourLast())
            elif len(bottle.colours) == 0:
                continue
            else:
                return False
        return True       