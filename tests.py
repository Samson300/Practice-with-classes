from character import Character

arya = Character("Arya Stark", "arya.png")
jon = Character("Jon Snow", "jon.png")

print(jon.name, jon.avatar)
print(arya.name, arya.avatar)

# After adding stuff two items to inventory
# length of inventory should be == 2

arya.inventory.append("sword")
arya.inventory.append("mask")

print(len(arya.inventory))