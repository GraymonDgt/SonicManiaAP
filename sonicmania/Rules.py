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


    connect_regions(world, player, "Menu", "Green Hill 1", lambda state: state.has("Green Hill Zone (Act 1)", player) or state.has("Green Hill Zone", player))
    connect_regions(world, player, "Menu", "Green Hill 2", lambda state: state.has("Green Hill Zone (Act 2)", player)or state.has("Green Hill Zone", player))

    connect_regions(world, player, "Menu", "Chemical Plant 1", lambda state: state.has("Chemical Plant Zone (Act 1)", player) or state.has("Chemical Plant Zone", player))
    connect_regions(world, player, "Menu", "Chemical Plant 2", lambda state: state.has("Chemical Plant Zone (Act 2)", player) or state.has("Chemical Plant Zone", player))

    connect_regions(world, player, "Menu", "Studiopolis 1", lambda state: state.has("Studiopolis Zone (Act 1)", player) or state.has("Studiopolis Zone", player))
    connect_regions(world, player, "Menu", "Studiopolis 2", lambda state: state.has("Studiopolis Zone (Act 2)", player) or state.has("Studiopolis Zone", player))

    connect_regions(world, player, "Menu", "Flying Battery 1", lambda state: state.has("Flying Battery Zone (Act 1)", player) or state.has("Flying Battery Zone", player))
    connect_regions(world, player, "Menu", "Flying Battery 2", lambda state: state.has("Flying Battery Zone (Act 2)", player) or state.has("Flying Battery Zone", player))

    connect_regions(world, player, "Menu", "Press Garden 1", lambda state: state.has("Press Garden Zone (Act 1)", player) or state.has("Press Garden Zone", player))
    connect_regions(world, player, "Menu", "Press Garden 2", lambda state: state.has("Press Garden Zone (Act 2)", player) or state.has("Press Garden Zone", player))

    connect_regions(world, player, "Menu", "Stardust Speedway 1", lambda state: state.has("Stardust Speedway Zone (Act 1)", player) or state.has("Stardust Speedway Zone", player))
    connect_regions(world, player, "Menu", "Stardust Speedway 2", lambda state: state.has("Stardust Speedway Zone (Act 2)", player) or state.has("Stardust Speedway Zone", player))

    connect_regions(world, player, "Menu", "Hydrocity 1", lambda state: state.has("Hydrocity Zone (Act 1)", player) or state.has("Hydrocity Zone", player))
    connect_regions(world, player, "Menu", "Hydrocity 2", lambda state: state.has("Hydrocity Zone (Act 2)", player) or state.has("Hydrocity Zone", player))

    connect_regions(world, player, "Menu", "Mirage Saloon 1", lambda state: state.has("Mirage Saloon Zone (Act 1)", player) or state.has("Mirage Saloon Zone", player))
    connect_regions(world, player, "Menu", "Mirage Saloon 2", lambda state: state.has("Mirage Saloon Zone (Act 2)", player) or state.has("Mirage Saloon Zone", player))

    connect_regions(world, player, "Menu", "Oil Ocean 1", lambda state: state.has("Oil Ocean Zone (Act 1)", player) or state.has("Oil Ocean Zone", player))
    connect_regions(world, player, "Menu", "Oil Ocean 2", lambda state: state.has("Oil Ocean Zone (Act 2)", player) or state.has("Oil Ocean Zone", player))

    connect_regions(world, player, "Menu", "Lava Reef 1", lambda state: (state.has("Lava Reef Zone (Act 1)", player) or state.has("Lava Reef Zone", player)) and state.has("Spindash", player))
    connect_regions(world, player, "Menu", "Lava Reef 2", lambda state: state.has("Lava Reef Zone (Act 2)", player) or state.has("Lava Reef Zone", player))

    connect_regions(world, player, "Menu", "Metallic Madness 1", lambda state: state.has("Metallic Madness Zone (Act 1)", player) or state.has("Metallic Madness Zone", player))
    connect_regions(world, player, "Menu", "Metallic Madness 2", lambda state: state.has("Metallic Madness Zone (Act 2)", player) or state.has("Metallic Madness Zone", player))

    connect_regions(world, player, "Menu", "Titanic Monarch 1", lambda state: state.has("Titanic Monarch Zone (Act 1)", player) or state.has("Titanic Monarch Zone", player))
    connect_regions(world, player, "Menu", "Titanic Monarch 2", lambda state: state.has("Titanic Monarch Zone (Act 2)", player) or state.has("Titanic Monarch Zone", player))

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


    add_rule(world.get_location("Green Hill (Act 1) Giant Ring 1 - Knuckles Path", player),
             lambda state: state.has("Knuckles", player))



    #MMZ1 NEEDS sonic/peelout/knuckles/spindash

    add_rule(world.get_location("Press Garden (Act 1) Giant Ring 2 - Closed Gate Above Crusher", player),
             lambda state: state.has("Sonic", player) or state.has("Tails", player) or
                           state.has("Knuckles",player) or state.has("Ray", player) or
                           state.has("Spindash", player) or state.has("Super Peelout", player))

    add_rule(world.get_location("Mirage Saloon (Act 1 Normal) Clear", player),
             lambda state: state.has("Sonic", player) or state.has("Tails", player) or state.has("Mighty", player) or state.has("Ray", player))
    add_rule(world.get_location("Mirage Saloon (Act 1 Normal) Giant Ring - Inside Train Car", player),
             lambda state: state.has("Sonic", player) or state.has("Tails", player) or state.has("Mighty", player) or state.has("Ray", player))
    add_rule(world.get_location("Mirage Saloon (Act 1 Knuckles) Clear", player),
             lambda state: state.has("Knuckles", player))
    add_rule(world.get_location("Mirage Saloon (Act 1 Knuckles) Giant Ring 1 - Left Path Near Start", player),
             lambda state: state.has("Knuckles", player))
    add_rule(world.get_location("Mirage Saloon (Act 1 Knuckles) Giant Ring 2 - Final Bumper Section Top Left", player),
             lambda state: state.has("Knuckles", player))
    add_rule(world.get_location("Mirage Saloon (Act 1 Knuckles) Giant Ring 3 - Open Area Left Side", player),
             lambda state: state.has("Knuckles", player))


    add_rule(world.get_location("Lava Reef (Act 2) Giant Ring 1 - Knuckles Path", player),
             lambda state: state.has("Knuckles", player))

    add_rule(world.get_location("Metallic Madness (Act 1) Clear", player),
             lambda state: state.has("Sonic", player) or state.has("Knuckles",player) or state.has("Spindash", player) or state.has("Super Peelout", player))


    add_rule(world.get_location("Titanic Monarch (Act 1) Giant Ring 2 - Lightning Shield Near Orbs", player),
             lambda state: state.has("Sonic", player) or state.has("Tails", player) or state.has("Knuckles", player) or state.has("Ray", player))


    #ghz1e suspended bridge mighty + flame





    if options.achievementsanity:
        connect_regions(world, player, "Menu", "Achievements", lambda state: True)

        add_rule(world.get_location("Achievement: That's a Two-fer", player),
                 lambda state: state.can_reach_region("Green Hill 1", player))
        #afaik at least chemical plant, oil ocean (and probably others) have hidden monitors but there is a total of 5 people
        #alive that know where they are, so those 5 people can do it out of logic because theres no way anyone else is finding
        #them
        add_rule(world.get_location("Achievement: Magnificent Seven", player),
                 lambda state: state.count("Chaos Emerald",player) > 6)

        add_rule(world.get_location("Achievement: See You Next Game", player),
                 lambda state: state.count("Chaos Emerald",player) > 6 or state.can_reach_location("Titanic Monarch (Act 2) Clear", player))

        add_rule(world.get_location("Achievement: Magnificent Seven", player),
                 lambda state: state.count("Chaos Emerald",player) > 6)

        add_rule(world.get_location("Achievement: Now It Can't Hurt You Anymore", player),
                 lambda state: state.can_reach_region("Green Hill 2", player))#(state.has("Mighty", player) and state.can_reach_region("Encore Green Hill 1", player)) or )#and fire shield

        add_rule(world.get_location("Achievement: Triple Trouble", player),
                 lambda state: state.can_reach_location("Chemical Plant (Act 2) Clear", player))

        add_rule(world.get_location("Achievement: The Most Famous Hedgehog in the World", player),
                 lambda state: state.can_reach_region("Studiopolis 1", player) or state.can_reach_region("Studiopolis 2", player))

        add_rule(world.get_location("Achievement: Window Shopping", player),
                 lambda state: state.can_reach_region("Flying Battery 2", player))

        add_rule(world.get_location("Achievement: Crate Expectations", player),
                 lambda state: state.can_reach_region("Press Garden 1", player) and state.has("Sonic", player))# & fire shield

        add_rule(world.get_location("Achievement: King of Speed", player),
                 lambda state: state.can_reach_region("Stardust Speedway 2", player))

        add_rule(world.get_location("Achievement: Boat Enthusiast", player),
                 lambda state: state.can_reach_region("Hydrocity 1", player))

        add_rule(world.get_location("Achievement: The Password is 'Special Stage'", player),
                 lambda state: state.can_reach_region("Mirage Saloon 2", player))

        add_rule(world.get_location("Achievement: Secret Sub", player),
                 lambda state: state.can_reach_region("Oil Ocean 2", player))

        add_rule(world.get_location("Achievement: Without a Trace", player),
                 lambda state: (state.can_reach_region("Lava Reef 1", player) and state.has("Spindash",player)) or state.can_reach_region("Lava Reef 2", player))

        add_rule(world.get_location("Achievement: Professional Hedgehog", player),
                 lambda state: state.can_reach_region("Titanic Monarch 1", player))

        add_rule(world.get_location("Achievement: Collect 'Em All", player),
                 lambda state: state.can_reach_region("Metallic Madness 2", player))

        if options.blue_spheres >0:
            add_rule(world.get_location("Achievement: Full Medal Jacket", player),
                     lambda state: state.has("Blue Sphere Set 1",player) and state.has("Blue Sphere Set 2",player) and
                                   state.has("Blue Sphere Set 3",player) and state.has("Blue Sphere Set 4",player))
            if options.blue_spheres >1:
                add_rule(world.get_location("Achievement: No Way? No Way!", player),
                         lambda state: state.has("Blue Sphere Set 1", player) and state.has("Blue Sphere Set 2",player) and
                                       state.has("Blue Sphere Set 3", player) and state.has("Blue Sphere Set 4",player))



    if options.completion_type == 0:
        world.completion_condition[player] = lambda state: state.can_reach_location("Titanic Monarch (Act 2) Clear", player)
    if options.completion_type == 1:
        world.completion_condition[player] = lambda state: state.count("Chaos Emerald",player) > 6
    if options.completion_type == 2:
        world.completion_condition[player] = lambda state: (state.count("Chaos Emerald", player) > 6 or state.can_reach_location("Titanic Monarch (Act 2) Clear", player)) and state.has("Knuckles", player) and state.has("& Knuckles", player)
