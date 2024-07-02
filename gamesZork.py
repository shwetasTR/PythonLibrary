# Zork Game

# Define the game's rooms
rooms = {
    'start': {
        'description': 'You are in a dark room. There is a door to your left and right.',
        'left': 'kitchen',
        'right': 'living room'
    },
    'kitchen': {
        'description': 'You are in a kitchen. There is a fridge and a table.',
        'left': 'pantry',
        'right': 'start'
    },
    'living room': {
        'description': 'You are in a living room. There is a TV and a couch.',
        'left': 'start',
        'right': 'bedroom'
    },
    'pantry': {
        'description': 'You are in a pantry. There are shelves full of food.',
        'left': 'bathroom',
        'right': 'kitchen'
    },
    'bedroom': {
        'description': 'You are in a bedroom. There is a bed and a wardrobe.',
        'left': 'living room',
        'right': 'bathroom'
    },
    'bathroom': {
        'description': 'You are in a bathroom. There is a sink and a toilet.',
        'left': 'bedroom',
        'right': 'pantry'
    }
}

# Define the player's starting room
current_room = 'start'

# Game loop
while True:
    # Print the current room's description
    print(rooms[current_room]['description'])
    
    # Prompt the player for input
    direction = input('Enter a direction (left/right): ')
    
    # Check if the input is valid
    if direction not in ['left', 'right']:
        print('Invalid direction. Please enter "left" or "right".')
        continue
    
    # Update the current room based on the player's input
    current_room = rooms[current_room][direction]