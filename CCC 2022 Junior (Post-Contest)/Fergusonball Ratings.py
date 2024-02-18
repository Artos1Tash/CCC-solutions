arr_points = []
arr_fouls = []
players = int(input())

for i in range(players):
    points = int(input())
    fouls = int(input())
    arr_points.append(points)
    arr_fouls.append(fouls)

ratings = []

for point in range(players):
    rating = arr_points[point] * 5 - arr_fouls[point] * 3
    ratings.append(rating)

star_players = 0

for b in ratings:
    if b > 40:
        star_players += 1

if star_players == players:
    print(f'{star_players}+')
else:
    print(f'{star_players}')
