
def addition(*args):
    return sum([arg for arg in args])

def main():
    print(addition(2, 2))
    print(addition(1, 5, 7, 10))

    my_nums = [1, 5, 7, 10]
    print(addition(*my_nums))

if __name__ == '__main__':
    main()