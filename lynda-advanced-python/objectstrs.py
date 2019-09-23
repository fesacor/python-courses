
class Person():
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __repr__(self):
        return '<Person Class - fname: {}, lname: {}, age: {}>'.format(
            self.fname, self.lname, self.age
        )

    def __str__(self):
        return 'Person {} {} is {} years old.'.format(
            self.fname, self.lname, self.age
        )

    def __bytes__(self):
        val = 'Person:{}:{}:{}'.format(
            self.fname, self.lname, self.age
        )
        return bytes(val.encode('utf-8'))

def main():
    person_1 = Person('Felipe', 'Saenz', '?')
    print(repr(person_1))
    print(str(person_1))
    print('Formatted: {}'.format(person_1))
    print(bytes(person_1))

if __name__ == '__main__':
    main()