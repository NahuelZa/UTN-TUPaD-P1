original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {}

for i,j in original.items():
    invertido[j]=i
print(invertido)


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
players_data = [
    {"name": "Patrick Mahomes", "position": "Quarterback", "jersey_number": 15, "yards_gained": 400, "touchdowns": 3},
    {"name": "Tyreek Hill", "position": "Wide Receiver", "jersey_number": 10, "yards_gained": 150, "touchdowns": 2},
    # Add more players as needed
]
names = [player["name"] for player in players_data]
print("Players Names:", names)