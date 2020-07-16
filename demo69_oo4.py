class Team:
    member = 7

    def working_hour(self):
        return self.day

    def all_working_hour(self):
        self.day = 7
        return self.day * self.member

    @classmethod
    def get_member(cls):
        return cls.member

    @staticmethod
    def calculate(x, y):
        return x ** y


t1 = Team()
print(f"all working hour={t1.all_working_hour()}")
print(f"working hour={t1.working_hour()}")
print(t1.get_member(), Team.get_member(), Team.member)
print(Team.calculate(3, 5), t1.calculate(4, 6))
