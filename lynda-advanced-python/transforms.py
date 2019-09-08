
def filter_odds(x):
    return x % 2 == 0

def filter_lowers(x):
    return x.islower()

def square(x):
    return x**2

def to_letters(x):
    if(x >= 90):
        return 'A'
    if(x >= 80):
        return 'B'
    if(x >= 70):
        return 'C'
    if(x >= 60):
        return 'D'
    return 'E'

def main():
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = 'abcDeFGHiJklmnoP'
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    odds = list(filter(filter_odds, nums))
    print(odds)

    lowers = list(filter(filter_lowers, chars))
    print(lowers)

    squares = list(map(square, nums))
    print(squares)

    grades = sorted(grades)
    letters = list(map(to_letters, grades))
    for r in zip(grades, letters):
        print('{} -> {}'.format(r[0], r[1]))

if __name__ == '__main__':
    main()