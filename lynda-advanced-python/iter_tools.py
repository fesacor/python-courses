import itertools

def is_less_than(x, value):
    return x < value

def is_less_than_20(x):
    return is_less_than(x, 20)

def main():
    seq_1 = ['Joe', 'John', 'Mike']

    cycle_1 = itertools.cycle(seq_1)
    print('Cycle:')
    for i in range(10):
        print('\t{}'.format(next(cycle_1)))

    count_1 = itertools.count(100, 10)
    print('Count in increments of 10, startin on 100:')
    for i in range(7):
        print('\t{}'.format(next(count_1)))

    cnt = itertools.count(5, 5)
    vals = [next(cnt) for i in range(6)]
    accumulator = itertools.accumulate(vals)
    print('Accumulator:')
    for i in zip(vals, accumulator):
        print('\t{} -> {}'.format(i[0], i[1]))

    # Use min function as a criteria to the accumulator.
    # The min value will be held until a new one is found.
    accumulator = itertools.accumulate(vals, min)
    print('Accumulator (min):')
    for i in zip(vals, accumulator):
        print('\t{} -> {}'.format(i[0], i[1]))

    chain = itertools.chain('abcd', '1234')
    print('Chain:')
    for i in chain:
        print('\t{}'.format(i))

    dropwhile = itertools.dropwhile(is_less_than_20, vals)
    print('Drop while it\'s less than 20:')
    for i in dropwhile:
        print('\t{}'.format(i))

    takewhile = itertools.takewhile(is_less_than_20, vals)
    print('Take while it\'s less than 20:')
    for i in takewhile:
        print('\t{}'.format(i))

if __name__ == '__main__':
    main()