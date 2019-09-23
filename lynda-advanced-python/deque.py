import collections 
import string

def main():
    d = collections.deque(string.ascii_lowercase)
    print('Item count: {}'.format(len(d)))
    for e in d:
        # Stay in the same line by using end=' ' 
        print(e.upper(), end=' ') 

    d.pop()
    d.popleft()
    d.append(1)
    d.appendleft(0)
    print(d)

    d.rotate(10)
    print(d)
    d.rotate(-10)
    print(d)

if __name__ == "__main__":
    main()