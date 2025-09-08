players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

players_2 = [
    i_keys + i_values
    for i_keys, i_values
    in players.items()
]

print(players_2)
