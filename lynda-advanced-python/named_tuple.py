import collections

def main():
    point = collections.namedtuple('Point', 'x y')
    p1 = point(10, 20)
    p2 = point(30, 40)
    print(p1, p2)
    print(p1.x, p2.y)

    p1 = p1._replace(x=100)
    print(p1)

if __name__ == '__main__':
    main() 