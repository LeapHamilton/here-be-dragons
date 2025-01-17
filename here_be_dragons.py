class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return f"{self.name}\n{self.description}\nExits: {', '.join(self.exits.keys())}\nItems: {', '.join(self.items)}"


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.items = []

inventory = []

player = Player("Richard")

#rooms 
manor_house = Room("The lord of the manor's house.", "This imposing structure sits atop a hill which overlooks the surrounding countryside for miles. To the south, past the meadow you can see a village. Over in the west meanwhile stands a dark, brooding forest.")
inside_manor_house = Room("Inside the manor house.", "The walls are decorated with heads of deer.")
meadow = Room("A pleasant, green meadow.", "A gentle breeze wafts over the grass. To the north a large house stands on top of a hill." )
farmland = Room("Farmland", "Here the fields have been sown with wheat and barley, but the crops seem to have been damaged by fire.")
forest = Room("A menacing forest.", "A wall of dark oaks stand in your way.")
village_gate = Room("The main gates.", "Set in a thick wall of stone, the main gate stands open.")
village_square = Room("The village square", "A statue stands in the middle of this quaint village square.")
burned_cottage = Room("The remains of a cottage.", "The building looks to have been destroyed by fire.")
abandoned_house = Room("An abandoned house.", "A chipped sign says, 'Carpenter', but it looks like the place has been empty for weeks.")
well = Room("A stone well.", "A circular structure with a rope and bucket for bringing up water.")
cluster = Room("A cluster of small houses.", "Made of wattle and daub, the roofs of the cottages have been damaged by fire.")
inn = Room("The Welcome Inn.", "Smoke rising from the chimney suggests the inn is open for business, but the sound of voices raised in argument does not bode well." )
inside_inn = Room("The interior of the Welcome Inn.", "The air is heavy with the smell of beer and sweat. Groups of men were arguing but quieten their voices when they see you. Despite this, the atmosphere is not unfriendly.")
fishmonger = Room("The fishmonger's.", "Perch and carp are on display, as well as eels and even a couple of salmon.")
blacksmith = Room("The blacksmith's", "A sign says 'Freshly made swords for sale'")
inside_blacksmith = Room("The blacksmith's workshop.", "The fire of a furnace burns bright and hot. The air is clammy with heat and steam.")
priest_house = Room("A well-kept house.", "Given that there is a church to the east, this must be the priest's home.")
inside_priest = Room("Inside the priest's house.","The decoration is simple. Notably, there is no cross on the wall, nor any sign of religious iconography.")
church = Room("A stone church.", "The roof has been blackened, but holds firm.")
inside_church = Room("Church interior.", "Wooden benches line the inside of the building. The alter is bare. Unlit candles stand by the entrance.")
graveyard = Room("A graveyard.", "Two freshly-laid gravestones are prominent.")


#exits
manor_house.add_exit("south", meadow)
manor_house.add_exit("in", inside_manor_house)
inside_manor_house.add_exit("out", manor_house)
meadow.add_exit("north", manor_house)
meadow.add_exit("south", village_gate)
meadow.add_exit("west", forest)
meadow.add_exit("east", farmland)
farmland.add_exit("west", meadow)
forest.add_exit("east", meadow)
village_gate.add_exit("north", meadow)
village_gate.add_exit("south", village_square)
village_square.add_exit("south", blacksmith)
village_square.add_exit("north", village_gate)
village_square.add_exit("west", well)
village_square.add_exit("east", burned_cottage)
burned_cottage.add_exit("west", village_square)
burned_cottage.add_exit("south", burned_cottage)
burned_cottage.add_exit("east", priest_house)
priest_house.add_exit("west", burned_cottage)
priest_house.add_exit("east", church)
priest_house.add_exit("in", inside_priest)
inside_priest.add_exit("out", priest_house)
abandoned_house.add_exit("west", blacksmith)
abandoned_house.add_exit("north", burned_cottage)
well.add_exit("east", village_square)
well.add_exit("west", cluster)
well.add_exit("south", fishmonger)
cluster.add_exit("east", well)
cluster.add_exit("south", inn)
inn.add_exit("north", cluster)
inn.add_exit("in", inside_inn)
inn.add_exit("east", fishmonger)
inside_inn.add_exit("out", inn)
fishmonger.add_exit("west", inn)
fishmonger.add_exit("east", blacksmith)
fishmonger.add_exit("north", well)
blacksmith.add_exit("north", village_square)
blacksmith.add_exit("in", inside_blacksmith)
blacksmith.add_exit("west", fishmonger)
blacksmith.add_exit("east", abandoned_house)
inside_blacksmith.add_exit("out", blacksmith)
church.add_exit("west", priest_house)
church.add_exit("in", inside_church)
church.add_exit("north", graveyard)
inside_church.add_exit("out", church)
graveyard.add_exit("south", church)

meadow.add_item("necklace")
manor_house.add_item("coin")

current_room = meadow
gameRunning = True
while gameRunning:
    
    print(current_room)
    command = input("What do you want to do? ").strip().lower()

    if command in current_room.exits:
        current_room = current_room.exits[command]

    elif len(current_room.items) > 0 and command == "get " + current_room.items[0]:
        player.items.append(current_room.items.pop(0))
        print("You are holding " + player.items[0])


    elif command == "drop " + player.items[0]:

        current_room.items.append(player.items.pop(0))

        print("You drop the " + current_room.items[0])
        
    elif command == "quit":
        print("Thanks for playing!")
        break
    else:
        print("Invalid command. Try again.")