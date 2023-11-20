init_invest = 10000
annual_rendement_str = "10%"

annual_rendement_decimal = float(annual_rendement_str.strip('%')) / 100

rendement = init_invest * annual_rendement_decimal

print ("Le gain annuel sera " + str (rendement))

init_invest += rendement

print ("Après un an l'investissement inital passe à " + str (init_invest))

init_invest += 5000

annual_rendement_decimal += 0.02

annual_rendement_str = "{:.2%}".format(annual_rendement_decimal)

print ("Le nouveau pourcentage de rendement est " + str (annual_rendement_str))

rendement = init_invest * annual_rendement_decimal

print ("Le gain annuel sera " + str (rendement))

init_invest += rendement

print ("Après un an l'investissement inital passe à " + str (init_invest))

retrait = init_invest * 0.1

init_invest = init_invest - retrait

print ("Après le retrait il reste " + str (init_invest))

annual_rendement_decimal -= 0.01

annual_rendement_str = "{:.2%}".format(annual_rendement_decimal)

print ("Le nouveau pourcentage de rendement est " + str (annual_rendement_str))

rendement = init_invest * annual_rendement_decimal

init_invest += rendement

print ("Après un an l'investissement inital passe à " + str (init_invest))
