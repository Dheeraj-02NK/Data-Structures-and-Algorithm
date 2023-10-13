class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.occupation == 'Developer':
            print(self.name, 'does coding')
        elif self.occupation == 'CEO':
            print(self.name, "leads Company")
        else:
            print(self.name, 'is an employee')

    def speaks(self):
        print(self.name, "says I can do it!!!")

name = input('Enter name: ')
occ = input('Enter occupation: ')
person = Human(name, occ)
person.do_work()
person.speaks()