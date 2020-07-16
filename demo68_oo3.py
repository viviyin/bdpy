class Team:
    name = "Normal Team"
    pass


t1 = Team()
print(t1.name, Team.name)

t1.name = "R&D Team"
print(t1.name, Team.name)

del t1.name
print(t1.name, Team.name)

t1.size = 7
print(t1.size, t1.name)
#print(t1.color)

