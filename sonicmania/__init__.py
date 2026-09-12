import typing
import os
import json
from .Items import (item_table, item_data_table, generic_item_data_table, zone_item_data_table, character_item_data_table, SonicManiaItem)

from .Locations import location_table, SonicManiaLocation
from .Options import mania_options_groups, SonicManiaOptions
from .Rules import set_rules
from .Regions import create_regions
from BaseClasses import Item, Tutorial, ItemClassification, Region
from ..AutoWorld import World, WebWorld
import random
from multiprocessing import Process
from worlds.LauncherComponents import Component, components, Type, launch_subprocess, icon_paths






#class SM64Web(WebWorld):
#    tutorials = [Tutorial(
#        "Multiworld Setup Guide",
#        "A guide to setting up SM64EX for MultiWorld.",
#        "English",
#        "setup_en.md",
#        "setup/en",
#        ["N00byKing"]
#    )]

option_groups = mania_options_groups

class SonicManiaWorld(World):
    """ 
    Sonic Superstars if it was good
    """
    game: str = "Sonic Mania"
    topology_present = False

    item_name_to_id = item_table
    location_name_to_id = location_table

    required_client_version = (0, 3, 5)

    area_connections: typing.Dict[int, int]

    options_dataclass = SonicManiaOptions

    number_of_locations: int
    filler_count: int


    def generate_early(self):

        max_locations = 100#TODO up this once i have enough locations
        if self.options.blue_spheres >0:
            max_locations += 32
            if self.options.blue_spheres > 1:
                max_locations += 32
        #if self.options.legally_distinct and not self.options.pirated:#im going insane
        #    max_locations +=1
        self.number_of_locations = max_locations
        self.move_rando_bitvec = 0



    def create_regions(self):
        create_regions(self.multiworld, self.options, self.player)

    def set_rules(self):
        self.area_connections = {}
        set_rules(self.multiworld, self.options, self.player, self.area_connections, self.move_rando_bitvec)


    def create_item(self, name: str) -> Item:
        data = item_data_table[name]
        item = SonicManiaItem(name, data.classification, data.code, self.player)

        return item

    def create_items(self):
        slots_to_fill = self.number_of_locations



        Valid_starts = ["Green Hill Zone (Act 1)","Green Hill Zone (Act 2)",
"Chemical Plant Zone (Act 1)","Chemical Plant Zone (Act 2)",
"Studiopolis Zone (Act 1)","Studiopolis Zone (Act 2)",
"Flying Battery Zone (Act 1)","Flying Battery Zone (Act 2)",
"Press Garden Zone (Act 1)","Press Garden Zone (Act 2)",
"Stardust Speedway Zone (Act 1)","Stardust Speedway Zone (Act 2)",
"Hydrocity Zone (Act 1)","Hydrocity Zone (Act 2)",
"Mirage Saloon Zone (Act 1)","Mirage Saloon Zone (Act 2)",
"Oil Ocean Zone (Act 1)","Oil Ocean Zone (Act 2)",
"Lava Reef Zone (Act 1)","Lava Reef Zone (Act 2)",
"Metallic Madness Zone (Act 1)","Metallic Madness Zone (Act 2)",
"Titanic Monarch Zone (Act 1)"]

        rand_idx = random.randrange(len(Valid_starts))

        Starting_zone = Valid_starts[rand_idx]


        for zone in zone_item_data_table.keys():
            if zone == Starting_zone:
                self.multiworld.push_precollected(self.create_item(zone))
                continue
            self.multiworld.itempool += [self.create_item(zone)]
            slots_to_fill-=1

        Valid_chars = ["Sonic","Tails","Knuckles","Mighty","Ray"]

        rand_idx = random.randrange(len(Valid_chars))

        Starting_char = Valid_chars[rand_idx]

        for char in character_item_data_table.keys():
            if char == Starting_char:
                self.multiworld.push_precollected(self.create_item(char))
                continue
            self.multiworld.itempool += [self.create_item(char)]
            slots_to_fill -= 1


        for i in range(7):
            self.multiworld.itempool += [self.create_item("Chaos Emerald")]
            slots_to_fill -=1

        self.multiworld.itempool += [self.create_item("Spindash")]
        self.multiworld.itempool += [self.create_item("Super Peelout")]
        self.multiworld.itempool += [self.create_item("Insta-shield")]
        slots_to_fill -= 3

        if self.options.blue_spheres >0:#WORK????
            self.multiworld.itempool += [self.create_item("Blue Sphere Set 1")]
            self.multiworld.itempool += [self.create_item("Blue Sphere Set 2")]
            self.multiworld.itempool += [self.create_item("Blue Sphere Set 3")]
            self.multiworld.itempool += [self.create_item("Blue Sphere Set 4")]
            slots_to_fill -= 4
        #self.multiworld.itempool += [self.create_item("Progressive Shop")]
        #self.multiworld.itempool += [self.create_item("Progressive Shop")]
        #self.multiworld.itempool += [self.create_item("Progressive Shop")]
        #slots_to_fill -= 3

        trap_slots = slots_to_fill*(self.options.trap_percent/100)
        for i in range(int(trap_slots)):
            self.multiworld.itempool += [self.create_item("Placebo Trap")]
            slots_to_fill -= 1

        if slots_to_fill > 0:
            filler_slots = slots_to_fill
            total_filler_weights = 0
            for filler_weight in self.options.filler_weights:
                total_filler_weights += self.options.filler_weights[filler_weight]
            ratio = filler_slots / total_filler_weights
            for filler in self.options.filler_weights:
                for i in range(int(ratio * self.options.filler_weights[filler])):
                    self.multiworld.itempool += [self.create_item(filler)]
                    slots_to_fill -= 1

        while slots_to_fill > 0:
            self.multiworld.itempool += [self.create_item("1UP")]
            slots_to_fill -= 1


    def generate_basic(self): #use to force items in a specific location
        #self.multiworld.get_location()
        return
           #self.multiworld.get_location("BoB: Bob-omb Buddy", self.player).place_locked_item(self.create_item("Cannon Unlock BoB"))


    def get_filler_item_name(self) -> str:
        return "1UP"

    def fill_slot_data(self):
        return {
            "RingLink": self.options.ring_link.value,
            "DeathLink": self.options.death_link.value,
            "CompletionType": self.options.completion_type.value,
        }

    def generate_output(self, output_directory: str):
        if self.multiworld.players != 1:
            return
        data = {
            "slot_data": self.fill_slot_data(),
            "location_to_item": {self.location_name_to_id[i.name] : item_table[i.item.name] for i in self.multiworld.get_locations()},
            "data_package": {
                "data": {
                    "games": {
                        self.game: {
                            "item_name_to_id": self.item_name_to_id,
                            "location_name_to_id": self.location_name_to_id
                        }
                    }
                }
            }
        }
        filename = f"{self.multiworld.get_out_file_name_base(self.player)}.apmania"
        with open(os.path.join(output_directory, filename), 'w') as f:
            json.dump(data, f)

    def extend_hint_information(self, hint_data: typing.Dict[int, typing.Dict[int, str]]):
        return

    def write_spoiler(self, spoiler_handle: typing.TextIO) -> None:
        # Write calculated star costs to spoiler.
        star_cost_spoiler_header = '\n\n' + self.player_name + ' line 159, TODO find out what this does:\n\n'
        spoiler_handle.write(self.player_name)
        # - Reformat star costs dictionary in spoiler to be a bit more readable.


