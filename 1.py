class Child:
    def __init__(self, name: str, name2: str, clas: int):
        self.name = name
        self.name2 = name2
        self.clas = clas

    def get_full_name(self):
        return self.name.title() + ' ' + self.name2.title()

    def get_grate(self):
        return self.clas


chi = Child("Aleksander", "micronov", 5)
print(chi.get_full_name())
print(chi.get_grate())