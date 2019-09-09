from collections import defaultdict

def main():
    fruits = [
        'apple',
        'pear',
        'orange',
        'banana',
        'apple',
        'grape',
        'banana',
        'banana'
    ]

    # Using a regular dictionary
    fruit_count = {}
    for f in fruits:
        if f in fruit_count:
            fruit_count[f] += 1
        else:
            fruit_count[f] = 1
    print(fruit_count)

    # Using defaultdict
    fruit_count = defaultdict(int)
    for f in fruits:
        fruit_count[f] += 1
    print(fruit_count)

    # Using defaultdict with lambda
    fruit_count = defaultdict(lambda: 100)
    for f in fruits:
        fruit_count[f] += 1
    print(fruit_count)
    
if __name__ == "__main__":
    main()