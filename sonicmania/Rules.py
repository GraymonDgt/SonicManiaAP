from typing import Callable, Union, Dict, Set

from BaseClasses import MultiWorld, CollectionState
from ..generic.Rules import add_rule, set_rule
from .Locations import location_table
from .Options import SonicManiaOptions
from .Regions import connect_regions, NoZones


def shuffle_dict_keys(world, dictionary: dict) -> dict:
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    world.random.shuffle(keys)
    return dict(zip(keys, values))

def fix_reg(entrance_map: Dict[NoZones, str], entrance: NoZones, invalid_regions: Set[str],#scared to remove this
            swapdict: Dict[NoZones, str], world):
    if entrance_map[entrance] in invalid_regions: # Unlucky :C
        replacement_regions = [(rand_entrance, rand_region) for rand_entrance, rand_region in swapdict.items()
                               if rand_region not in invalid_regions]
        rand_entrance, rand_region = world.random.choice(replacement_regions)
        old_dest = entrance_map[entrance]
        entrance_map[entrance], entrance_map[rand_entrance] = rand_region, old_dest
        swapdict[entrance], swapdict[rand_entrance] = rand_region, old_dest
    swapdict.pop(entrance)



def set_rules(world, options: SonicManiaOptions, player: int, area_connections: dict, move_rando_bitvec: int):


    connect_regions(world, player, "Menu", "Green Hill 1", lambda state: state.has("Green Hill Zone (Act 1)", player))
    connect_regions(world, player, "Menu", "Green Hill 2", lambda state: state.has("Green Hill Zone (Act 2)", player))

    connect_regions(world, player, "Menu", "Chemical Plant 1", lambda state: state.has("Chemical Plant Zone (Act 1)", player))
    connect_regions(world, player, "Menu", "Chemical Plant 2", lambda state: state.has("Chemical Plant Zone (Act 2)", player))

    connect_regions(world, player, "Menu", "Studiopolis 1", lambda state: state.has("Studiopolis Zone (Act 1)", player))
    connect_regions(world, player, "Menu", "Studiopolis 2", lambda state: state.has("Studiopolis Zone (Act 2)", player))

    connect_regions(world, player, "Menu", "Flying Battery 1", lambda state: state.has("Flying Battery Zone (Act 1)", player))
    connect_regions(world, player, "Menu", "Flying Battery 2", lambda state: state.has("Flying Battery Zone (Act 2)", player))

    connect_regions(world, player, "Menu", "Press Garden 1", lambda state: state.has("Press Garden Zone (Act 1)", player))
    connect_regions(world, player, "Menu", "Press Garden 2", lambda state: state.has("Press Garden Zone (Act 2)", player))

    connect_regions(world, player, "Menu", "Stardust Speedway 1", lambda state: state.has("Stardust Speedway Zone (Act 1)", player))
    connect_regions(world, player, "Menu", "Stardust Speedway 2", lambda state: state.has("Stardust Speedway Zone (Act 2)", player))

    connect_regions(world, player, "Menu", "Hydrocity 1", lambda state: state.has("Hydrocity Zone (Act 1)", player))
    connect_regions(world, player, "Menu", "Hydrocity 2", lambda state: state.has("Hydrocity Zone (Act 2)", player))

    connect_regions(world, player, "Menu", "Mirage Saloon 1", lambda state: state.has("Mirage Saloon Zone (Act 1)", player))
    connect_regions(world, player, "Menu", "Mirage Saloon 2", lambda state: state.has("Mirage Saloon Zone (Act 2)", player))

    connect_regions(world, player, "Menu", "Oil Ocean 1", lambda state: state.has("Oil Ocean Zone (Act 1)", player))
    connect_regions(world, player, "Menu", "Oil Ocean 2", lambda state: state.has("Oil Ocean Zone (Act 2)", player))

    connect_regions(world, player, "Menu", "Lava Reef 1", lambda state: state.has("Lava Reef Zone (Act 1)", player) and state.has("Spindash", player))
    connect_regions(world, player, "Menu", "Lava Reef 2", lambda state: state.has("Lava Reef Zone (Act 2)", player))

    connect_regions(world, player, "Menu", "Metallic Madness 1", lambda state: state.has("Metallic Madness Zone (Act 1)", player))
    connect_regions(world, player, "Menu", "Metallic Madness 2", lambda state: state.has("Metallic Madness Zone (Act 2)", player))

    connect_regions(world, player, "Menu", "Titanic Monarch 1", lambda state: state.has("Titanic Monarch Zone (Act 1)", player))
    connect_regions(world, player, "Menu", "Titanic Monarch 2", lambda state: state.has("Titanic Monarch Zone (Act 2)", player))

    connect_regions(world, player, "Menu", "Special Stages", lambda state: True)

    if options.blue_spheres >0:
        connect_regions(world, player, "Menu", "Blue Spheres 1", lambda state: state.has("Blue Sphere Set 1", player))
        connect_regions(world, player, "Menu", "Blue Spheres 2", lambda state: state.has("Blue Sphere Set 2", player))
        connect_regions(world, player, "Menu", "Blue Spheres 3", lambda state: state.has("Blue Sphere Set 3", player))
        connect_regions(world, player, "Menu", "Blue Spheres 4", lambda state: state.has("Blue Sphere Set 4", player))




    add_rule(world.get_location("Special Stage 1 Clear", player),
             lambda state: state.has("Special Stage 1", player))
    add_rule(world.get_location("Special Stage 2 Clear", player),
             lambda state: state.has("Special Stage 2", player))
    add_rule(world.get_location("Special Stage 3 Clear", player),
             lambda state: state.has("Special Stage 3", player))
    add_rule(world.get_location("Special Stage 4 Clear", player),
             lambda state: state.has("Special Stage 4", player))
    add_rule(world.get_location("Special Stage 5 Clear", player),
             lambda state: state.has("Special Stage 5", player))
    add_rule(world.get_location("Special Stage 6 Clear", player),
             lambda state: state.has("Special Stage 6", player))
    add_rule(world.get_location("Special Stage 7 Clear", player),
             lambda state: state.has("Special Stage 7", player))


    add_rule(world.get_location("Green Hill (Act 1) Giant Ring - Knuckles Path", player),
             lambda state: state.has("Knuckles", player))


    add_rule(world.get_location("Mirage Saloon (Act 1 Normal) Clear", player),
             lambda state: state.has("Sonic", player) or state.has("Tails", player) or state.has("Mighty", player) or state.has("Ray", player))
    add_rule(world.get_location("Mirage Saloon (Act 1 Normal) Giant Ring - Inside Train Car", player),
             lambda state: state.has("Sonic", player) or state.has("Tails", player) or state.has("Mighty", player) or state.has("Ray", player))
    add_rule(world.get_location("Mirage Saloon (Act 1 Knuckles) Clear", player),
             lambda state: state.has("Knuckles", player))
    add_rule(world.get_location("Mirage Saloon (Act 1 Knuckles) Giant Ring - 1", player),
             lambda state: state.has("Knuckles", player))
    add_rule(world.get_location("Mirage Saloon (Act 1 Knuckles) Giant Ring - 2", player),
             lambda state: state.has("Knuckles", player))
    add_rule(world.get_location("Mirage Saloon (Act 1 Knuckles) Giant Ring - 3", player),
             lambda state: state.has("Knuckles", player))


    add_rule(world.get_location("Lava Reef (Act 2) Giant Ring - 5", player),
             lambda state: state.has("Knuckles", player))









    #later levels need a 2nd combat turret for logic
    #most levels require 2 weak combat turrets (pistol shrimp is strong enough for most levels)
    #levels with a lot of clams should require a collection turret
    if options.completion_type == 0:
        world.completion_condition[player] = lambda state: state.can_reach_location("Titanic Monarch (Act 2) Clear", player)
    else:
        world.completion_condition[player] = lambda state: state.can_reach_location("Titanic Monarch (Act 2) Clear", player) and state.count("Chaos Emerald",player) >6

