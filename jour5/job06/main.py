def toilette(nombre, taille):
    total = nombre * taille * 70 / 100
    metre = "%.2f" % round(total, 2)
    print(f"Pour {nombre} marche de {taille} cm, le gardien parcours {metre}m par semaines")

toilette(398, 12.31)

def toilette_2_jours_de_repos(nombre, taille):
    total = nombre * taille * 50 / 100
    metre = "%.2f" % round(total, 2)
    print(f"Pour {nombre} marche de {taille} cm, le gardien parcours {metre}m par semaines")

toilette_2_jours_de_repos(398, 12.31)

def toilettes_n_jours_de_repos(nombre, taille, repos=0):
    total = nombre * taille * (70 - 10 * repos) / 100
    metre = "%.2f" % round(total, 2)
    print(f"Pour {nombre} marche de {taille} cm, le gardien parcours {metre}m par semaines quand il a {repos} jours de repos")
    
toilettes_n_jours_de_repos(398, 12.31, 2)
toilettes_n_jours_de_repos(398, 12.31)
