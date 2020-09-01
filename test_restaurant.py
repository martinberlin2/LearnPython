

# 11:10 01.09 kata zwischendurch = restaurant.py
# 
# "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"

import NaTALi
evalTC = NaTALi.evalTC
execFuncWithExc = NaTALi.execFuncWithExc
execMethWithExc = NaTALi.execMethWithExc

import restaurant
restaurant = restaurant.restaurant
# änderung

import logging
	
def test_restaurant(): 
	logging.info(" ----- Start test_restaurant -----")
	evalTC(1, "KataOrder", execFuncWithExc(restaurant, ['milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza']), "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke")
	logging.info(" ----- End test_restaurant -----")
