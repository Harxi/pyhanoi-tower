import tower, random, os

tower = tower.Towers();
tower.generate();

# SLOVE

towers = [0, 1, 2]
need = tower.search(15)
del towers[need["tower"]]
other = random.choice(towers)
del towers[towers.index(other)]
main = towers[0]

[tower.move(main, other) for x in range(0, len(tower.towers[main]))]

def found(value):
	towers = [0, 1, 2]
	del towers[main]
	need = tower.search(value)
	del towers[towers.index(need["tower"])]
	other = towers[0]
	
	for x in range(0, need["index"]):
		tower.move(need["tower"], other)
		
	tower.move(need["tower"], main)

for x in range(15, 0, -1):
	found(x)

# SLOVE END

for towerI in range(3):
	for x in tower.towers[towerI]:
		print(f"{' '*((31-x*2)//2)}{'_'*(x*2)}{' '*((31-x*2)//2)}     {x}")
	print()

#while True:
#	for tower in range(3):
#		for x in a.towers[tower]:
#			print(f"{' '*((31-x*2)//2)}{'_'*(x*2)}{' '*((31-x*2)//2)}     {x}")
#		print()
#	
#	m = (int(input("F: ")), int(input("T: ")))
#	a.move(m[0], m[1])
#	os.system("clear")
