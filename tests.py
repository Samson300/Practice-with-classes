from character import Character
from character import Hero
from character import Monster

arya = Character("Arya Stark", "arya.png")
jon = Character("Jon Snow", "jon.png")

print(jon.name, jon.avatar)
print(arya.name, arya.avatar)

# After adding stuff two items to inventory
# length of inventory should be == 2

arya.inventory.append("sword")
arya.inventory.append("mask")

print(len(arya.inventory))

# arya should have a greet method
# and when i call it, it should return
# "Hello, jon snow, i am Arya Stark. I am awesome"
print(arya.greet(jon))

print(arya.greet())
bronn = Hero("Bronn of the Blackwater", "bron.png")

jack = Monster()
# Hero should be able to greet Character
print(bronn.greet(arya))
print(jon.greet(bronn))

# Will Monster be able to greet Hero?
print(jack.greet())
print(jack.greet(jon))