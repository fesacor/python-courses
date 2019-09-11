from collections import OrderedDict

def main():
    sport_teams = [
        # Team, wins, looses     
        ('Royals', (18, 12)),
        ('Rockets', (22, 8)),
        ('Cardinals', (20, 10)),
        ('Dragons', (22, 8)),
        ('Kings', (15, 15)),
        ('Chargers', (20, 10)),
        ('Jets', (16, 14)),
        ('Warriors', (25, 5))
    ]

    sorted_teams = sorted(sport_teams, key=lambda t: t[1][0], reverse=True)
    teams = OrderedDict(sorted_teams)
    print(teams)

    tm, wl = teams.popitem(False)
    print('Top team: {}. Wins: {}, losses: {}.'.format(tm, wl[0], wl[1]))

    a = OrderedDict({'a': 1, 'b': 2, 'c': 3})
    b = OrderedDict({'a': 1, 'c': 3, 'b': 2})
    c = {'a': 1, 'c': 3, 'b': 2}
    print(a)
    print(b)
    print(a == b)
    print(a == c)

if __name__ == "__main__":
    main()