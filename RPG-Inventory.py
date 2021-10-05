# Coarse: CS 30
# Period:3
# Date created: 30/09/21
# Date last modified: 04/10/21
# Name: Rabi Jasteen Juancito
# Description: RPG Inventory

# list of the characters with their info
characters = [
  "Mako has the abilty to mimic anything" "\n"
  "Mako is a an former athlete",
  "\n"
  "Harit has the ability to control electricity" "\n"
  "Harit is former electrician",
  "\n"
  "Sorn has the ability to make items disappear" "\n"
  "Sorn is a 12th grade high school student",
  "\n"
  "Attaku has the abilty of mind control" "\n"
  "Attaku is an intellegent criminal investigator"
  ]
for c in characters:  # output all character's descriptions
    print(f" {c}")

print("\n")
# list of the locations with their description
Location = [
  "Neustra Island is a small province where Mako was born and raised.",
  "Isle Stadt is a where Harit worked and discovered his powers.",
  "Pohwhet High School is where Sorn attends.",
  "Hashusai is Attaku's hometown in Japan."
  ]
for L in Location:  # output all Location descriptions
    print(f" {L}")

# nested dictionary that contains 4 dictionairies
# inventories of the character's power
print("\n")
inventories = {
  "Mako's Power Inventory": {
      "description": "can mimic any moving, living potentiel by watching them",
      "max energy": 1.489,
      "ATK": 0,
      "damage": 0
  },
  "Harit's Power Inventory": {
      "description": "control any types of electrical wave using his hands",
      "max energy": 5978,
      "ATK": 0,
      "damage": 40
  },
  "Sorn's Power Inventory": {
      "description": "make items dissapear and bring them back by touch",
      "max energy": 875,
      "ATK": 0,
      "damage": 60
  },
  "Attaku's Power Inventory": {
      "description": "compel someone to do whatever through physical contact",
      "max energy": 3000,
      "ATK": 0,
      "damage": 20
  }
}
print(inventories)  # output all the dictionaries
