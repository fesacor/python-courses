
def my_fcn(a1, a2, *, kw_only=True):
    pass

def main():
    #my_fcn(1, 2, True)
    my_fcn(1, 2, kw_only=False)

if __name__ == '__main__':
    main()