from collections import Counter

def main():
    class_1 = [
        'Bob',
        'Becky',
        'Chad',
        'Darcy',
        'Frank',
        'Hannah',
        'Kevin',
        'James',
        'James',
        'Melanie',
        'Penny',
        'Steve'
    ]
    class_2 = [
        'Bill',
        'Barry',
        'Cindy',
        'Debbie',
        'Frank',
        'Gabby',
        'Kelly',
        'James',
        'Joe',
        'Sam',
        'Tara',
        'Ziggy'
    ]

    c1 = Counter(class_1)
    c2 = Counter(class_2)
    print('How many James in class 1? A: {}'.format(c1['James']))
    print('How many students in class 1? A: {}'.format(sum(c1.values())))
    
    c1.update(class_2)
    print('How many students in class 1 and class 2? A: {}'.format(sum(c1.values())))
    print('Most common names: ', c1.most_common(3))

    c1.subtract(class_2)
    print('Most common names: ', c1.most_common(3))

    print(c1 & c2)


if __name__ == "__main__":
    main()