#Verify that Pac-Man can eat a ghost if he is empowered by a power pellet
def eat_ghost(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost

#Verify that Pac-Man has scored when a power pellet or dot has been eaten.
def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot   

#Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet
def lose(power_pellet_active, touching_ghost):
    return not power_pellet_active and touching_ghost

#Trigger the victory event when all dots have been eaten
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)