class person:
    def __init__(self, fname, lname) -> None:
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
        
class candidate(person):
    def reverse(self):
        print(self.lastname, self.firstname)

student1 = person("ada", "Obi")
student2 = candidate("louis", "Okoro")

student1.printname()
student2