import typing
from enum import Enum

from BaseClasses import MultiWorld, Region, Entrance, Location
from .Options import SonicManiaOptions
from .Locations import SonicManiaLocation, location_table


class NoZones(int, Enum):#scared to delete this
    SOMETHING = 1

class SonicManiaRegion(Region):
    subregions: typing.List[Region] = []


def create_regions(world: MultiWorld, options: SonicManiaOptions, player: int):
    regMM = Region("Menu", player, world, "Level Select")
    #create_default_locs(regMM, locSS_table)#TODO this might break something
    world.regions.append(regMM)


    regGH1 = create_region("Green Hill 1", player, world)
    create_locs(regGH1,"Green Hill (Act 1) Clear","Green Hill (Act 1) Giant Ring 1 - Knuckles Path",
    "Green Hill (Act 1) Giant Ring 2 - Lower Path Waterfall","Green Hill (Act 1) Giant Ring 3 - Main Path")
    regGH2 = create_region("Green Hill 2", player, world)
    create_locs(regGH2,"Green Hill (Act 2) Clear","Green Hill (Act 2) Giant Ring 1 - Near First Zipline Chain",
    "Green Hill (Act 2) Giant Ring 2 - Bottom Path Fake Wall Behind Monitor","Green Hill (Act 2) Giant Ring 3 - Waterfall Near Boss")

    regCP1 = create_region("Chemical Plant 1", player, world)
    create_locs(regCP1,"Chemical Plant (Act 1) Clear","Chemical Plant (Act 1) Giant Ring 1 - Bottom Path Underwater Wall",
    "Chemical Plant (Act 1) Giant Ring 2 - Upper Path Near Yellow Springs","Chemical Plant (Act 1) Giant Ring 3 - Upper Path After Large Ramp",
    "Chemical Plant (Act 1) Giant Ring 4 - Vertical Moving Blocks Bottom",)
    regCP2 = create_region("Chemical Plant 2", player, world)
    create_locs(regCP2,"Chemical Plant (Act 2) Clear",    "Chemical Plant (Act 2) Giant Ring 1 - Left After First Downwards Launch",
    "Chemical Plant (Act 2) Giant Ring 2 - Long Purple Pad Fake Wall","Chemical Plant (Act 2) Giant Ring 3 - Upper Path Moving Blocks")

    regSP1 = create_region("Studiopolis 1", player, world)
    create_locs(regSP1,"Studiopolis (Act 1) Clear","Studiopolis (Act 1) Giant Ring 1 - Backwards Ramp Near Start",
    "Studiopolis (Act 1) Giant Ring 2 - Top Path Fake Wall","Studiopolis (Act 1) Giant Ring 3 - Lower Path Window Break Into Ramp")
    regSP2 = create_region("Studiopolis 2", player, world)
    create_locs(regSP2,"Studiopolis (Act 2) Clear","Studiopolis (Act 2) Giant Ring 1 - Top Path Applause Sign",
    "Studiopolis (Act 2) Giant Ring 2 - Platforms After Wire Launch","Studiopolis (Act 2) Giant Ring 3 - Top Path Badnik Bounce Chain")

    regFB1 = create_region("Flying Battery 1", player, world)
    create_locs(regFB1,"Flying Battery (Act 1) Clear","Flying Battery (Act 1) Giant Ring 1 - Ceiling Magnets After 3rd Checkpoint",
    "Flying Battery (Act 1) Giant Ring 2 - Room Before Boss Left Wall")
    regFB2 = create_region("Flying Battery 2", player, world)
    create_locs(regFB2,"Flying Battery (Act 2) Clear","Flying Battery (Act 2) Giant Ring 1 - Bottom Path Near First Fans",
    "Flying Battery (Act 2) Giant Ring 2 - Outside Rising Chain Near Propellers","Flying Battery (Act 2) Giant Ring 3 - Outside Chain After Wind Tunnel",
    "Flying Battery (Act 2) Giant Ring 4 - Magnets Above Inside Switch")

    regPG1 = create_region("Press Garden 1", player, world)
    create_locs(regPG1,"Press Garden (Act 1) Clear","Press Garden (Act 1) Giant Ring 1 - Left After First Spinning Tube",
    "Press Garden (Act 1) Giant Ring 2 - Closed Gate Above Crusher")
    regPG2 = create_region("Press Garden 2", player, world)
    create_locs(regPG2,"Press Garden (Act 2) Clear","Press Garden (Act 2) Giant Ring 1 - Under 1st Checkpoint",
    "Press Garden (Act 2) Giant Ring 2 - Top Path Behind Half Pipe Ice","Press Garden (Act 2) Giant Ring 3 - Ice Slide Fake Wall After Loop")

    regSS1 = create_region("Stardust Speedway 1", player, world)
    create_locs(regSS1,"Stardust Speedway (Act 1) Clear",    "Stardust Speedway (Act 1) Giant Ring 1 - Alt Upper Path Between Pillars",
    "Stardust Speedway (Act 1) Giant Ring 2 - Bottom Spin Tunnels Spring Room","Stardust Speedway (Act 1) Giant Ring 3 - Upper Path Red Spring Near Vine")
    regSS2 = create_region("Stardust Speedway 2", player, world)
    create_locs(regSS2,"Stardust Speedway (Act 2) Clear",    "Stardust Speedway (Act 2) Giant Ring 1 - Bottom Path Inside Near Start",
    "Stardust Speedway (Act 2) Giant Ring 2 - Bottom Path Small Inside Space","Stardust Speedway (Act 2) Giant Ring 3 - Top Path Inside Ceiling Jump")

    regHC1 = create_region("Hydrocity 1", player, world)
    create_locs(regHC1,"Hydrocity (Act 1) Clear","Hydrocity (Act 1) Giant Ring 1 - Upper Path Launch Near 1st Checkpoint",
    "Hydrocity (Act 1) Giant Ring 2 - Middle Path Fall Into Water","Hydrocity (Act 1) Giant Ring 3 - Bottom Path Fake Wall Near Bubble Switch")
    regHC2 = create_region("Hydrocity 2", player, world)
    create_locs(regHC2,"Hydrocity (Act 2) Clear","Hydrocity (Act 2) Giant Ring 1 - 1st Water Slide Drop Underwater",
    "Hydrocity (Act 2) Giant Ring 2 - Launch After Tallest Water Slide")

    regMS1 = create_region("Mirage Saloon 1", player, world)
    create_locs(regMS1,"Mirage Saloon (Act 1 Normal) Clear","Mirage Saloon (Act 1 Knuckles) Clear","Mirage Saloon (Act 1 Normal) Giant Ring - Inside Train Car",
    "Mirage Saloon (Act 1 Knuckles) Giant Ring 1 - Left Path Near Start","Mirage Saloon (Act 1 Knuckles) Giant Ring 2 - Final Bumper Section Top Left",
    "Mirage Saloon (Act 1 Knuckles) Giant Ring 3 - Open Area Left Side")
    regMS2 = create_region("Mirage Saloon 2", player, world)
    create_locs(regMS2,"Mirage Saloon (Act 2) Clear",    "Mirage Saloon (Act 2) Giant Ring 2 - Left Top Path Breaking Sand Loop",
    "Mirage Saloon (Act 2) Giant Ring 3 - Top Path Half Pipe Near Sprayer","Mirage Saloon (Act 2) Giant Ring 1 - Push Barrel Into Water Sprayer")

    regOO1 = create_region("Oil Ocean 1", player, world)
    create_locs(regOO1,"Oil Ocean (Act 1) Clear","Oil Ocean (Act 1) Giant Ring 1 - First Flame Shield Fans",
    "Oil Ocean (Act 1) Giant Ring 2 - Top Path Pipes","Oil Ocean (Act 1) Giant Ring 3 - Middle Path Fake Wall Near Elevator")
    regOO2 = create_region("Oil Ocean 2", player, world)
    create_locs(regOO2,"Oil Ocean (Act 2) Clear","Oil Ocean (Act 2) Giant Ring 1 - Under 1st Checkpoint",
    "Oil Ocean (Act 2) Giant Ring 2 - Fake Wall Above 2nd Checkpoint Area")

    regLR1 = create_region("Lava Reef 1", player, world)
    create_locs(regLR1,"Lava Reef (Act 1) Clear","Lava Reef (Act 1) Giant Ring 1 - Behind First Spike Crusher",
    "Lava Reef (Act 1) Giant Ring 2 - Lower Path Spin Elevators")
    regLR2 = create_region("Lava Reef 2", player, world)
    create_locs(regLR2,"Lava Reef (Act 2) Clear","Lava Reef (Act 2) Giant Ring 2 - Lower Path Crumbling Platforms",
    "Lava Reef (Act 2) Giant Ring 3 - Fake Wall Near Moving Platforms","Lava Reef (Act 2) Giant Ring 4 - Bottom Path Iwamodoki Tunnel In Lava",
    "Lava Reef (Act 2) Giant Ring 5 - Fake Floor After Walker","Lava Reef (Act 2) Giant Ring 1 - Knuckles Path")

    regMM1 = create_region("Metallic Madness 1", player, world)
    create_locs(regMM1,"Metallic Madness (Act 1) Clear","Metallic Madness (Act 1) Giant Ring 1 - Bottom Path Above 1st Checkpoint",
    "Metallic Madness (Act 1) Giant Ring 2 - First Background Path End","Metallic Madness (Act 1) Giant Ring 3 - Top Path Slopes Near End")
    regMM2 = create_region("Metallic Madness 2", player, world)
    create_locs(regMM2,"Metallic Madness (Act 2) Clear","Metallic Madness (Act 2) Giant Ring 1 - Bottom Path Near 2nd Checkpoint",
    "Metallic Madness (Act 2) Giant Ring 2 - Hidden Spin Tunnel In Background")

    regTM1 = create_region("Titanic Monarch 1", player, world)
    create_locs(regTM1,"Titanic Monarch (Act 1) Clear","Titanic Monarch (Act 1) Giant Ring 1 - Above 2nd Checkpoint",
    "Titanic Monarch (Act 1) Giant Ring 2 - Lightning Shield Near Orbs")
    regTM2 = create_region("Titanic Monarch 2", player, world)
    create_locs(regTM2,"Titanic Monarch (Act 2) Clear","Titanic Monarch (Act 2) Giant Ring - Bottom Right Path Breakable Bumpers")

    regSPEC = create_region("Special Stages", player, world)
    create_locs(regSPEC, "Special Stage 1 Clear", "Special Stage 2 Clear","Special Stage 3 Clear","Special Stage 4 Clear","Special Stage 5 Clear","Special Stage 6 Clear","Special Stage 7 Clear")

    if options.blue_spheres >0:
        regBS1 = create_region("Blue Spheres 1", player, world)
        regBS2 = create_region("Blue Spheres 2", player, world)
        regBS3 = create_region("Blue Spheres 3", player, world)
        regBS4 = create_region("Blue Spheres 4", player, world)

        create_locs(regBS1,"Blue Sphere (Set 1) - Orange/Brown Clear","Blue Sphere (Set 1) - Aqua/Green Clear",
        "Blue Sphere (Set 1) - White/Orange Clear","Blue Sphere (Set 1) - Lime/Green Clear","Blue Sphere (Set 1) - Orange/Aqua Clear",
        "Blue Sphere (Set 1) - Purple/Tan Clear","Blue Sphere (Set 1) - White/Lime Clear","Blue Sphere (Set 1) - Gray/Light Gray Clear")
        create_locs(regBS2,"Blue Sphere (Set 2) - Magenta/Lime Clear","Blue Sphere (Set 2) - Dark Blue/Aqua Clear",
        "Blue Sphere (Set 2) - Red/White Clear","Blue Sphere (Set 2) - Purple/Orange Clear","Blue Sphere (Set 2) - Light Blue/White Clear",
        "Blue Sphere (Set 2) - Blue/White Clear","Blue Sphere (Set 2) - Blue/Orange Clear","Blue Sphere (Set 2) - Blue/Off-White Clear")
        create_locs(regBS3,"Blue Sphere (Set 3) - Aqua/Light Blue Clear","Blue Sphere (Set 3) - Yellow/Purple Clear",
        "Blue Sphere (Set 3) - Black/Dark Blue Clear","Blue Sphere (Set 3) - Lime/Purple Clear","Blue Sphere (Set 3) - Orange/Yellow (Dark Sky) Clear",
        "Blue Sphere (Set 3) - Pink/Aqua Clear","Blue Sphere (Set 3) - Light Brown/Off-White Clear","Blue Sphere (Set 3) - Brown/Off-White Clear")
        create_locs(regBS4,"Blue Sphere (Set 4) - Lime/White Clear","Blue Sphere (Set 4) - Light Blue/Aqua Clear",
        "Blue Sphere (Set 4) - Orange/Yellow (Light Sky) Clear","Blue Sphere (Set 4) - Purple/Off-White Clear","Blue Sphere (Set 4) - Blue/Light Blue Clear",
        "Blue Sphere (Set 4) - Yellow/Dark Yellow Clear","Blue Sphere (Set 4) - Blue/Green Clear","Blue Sphere (Set 4) - Blue/Dark Blue Clear")
        if options.blue_spheres > 1:
            create_locs(regBS1, "Blue Sphere (Set 1) - Orange/Brown Perfect", "Blue Sphere (Set 1) - Aqua/Green Perfect",
                        "Blue Sphere (Set 1) - White/Orange Perfect", "Blue Sphere (Set 1) - Lime/Green Perfect",
                        "Blue Sphere (Set 1) - Orange/Aqua Perfect",
                        "Blue Sphere (Set 1) - Purple/Tan Perfect", "Blue Sphere (Set 1) - White/Lime Perfect",
                        "Blue Sphere (Set 1) - Gray/Light Gray Perfect")
            create_locs(regBS2, "Blue Sphere (Set 2) - Magenta/Lime Perfect",
                        "Blue Sphere (Set 2) - Dark Blue/Aqua Perfect",
                        "Blue Sphere (Set 2) - Red/White Perfect", "Blue Sphere (Set 2) - Purple/Orange Perfect",
                        "Blue Sphere (Set 2) - Light Blue/White Perfect",
                        "Blue Sphere (Set 2) - Blue/White Perfect", "Blue Sphere (Set 2) - Blue/Orange Perfect",
                        "Blue Sphere (Set 2) - Blue/Off-White Perfect")
            create_locs(regBS3, "Blue Sphere (Set 3) - Aqua/Light Blue Perfect",
                        "Blue Sphere (Set 3) - Yellow/Purple Perfect",
                        "Blue Sphere (Set 3) - Black/Dark Blue Perfect", "Blue Sphere (Set 3) - Lime/Purple Perfect",
                        "Blue Sphere (Set 3) - Orange/Yellow (Dark Sky) Perfect",
                        "Blue Sphere (Set 3) - Pink/Aqua Perfect", "Blue Sphere (Set 3) - Light Brown/Off-White Perfect",
                        "Blue Sphere (Set 3) - Brown/Off-White Perfect")
            create_locs(regBS4, "Blue Sphere (Set 4) - Lime/White Perfect", "Blue Sphere (Set 4) - Light Blue/Aqua Perfect",
                        "Blue Sphere (Set 4) - Orange/Yellow (Light Sky) Perfect",
                        "Blue Sphere (Set 4) - Purple/Off-White Perfect", "Blue Sphere (Set 4) - Blue/Light Blue Perfect",
                        "Blue Sphere (Set 4) - Yellow/Dark Yellow Perfect", "Blue Sphere (Set 4) - Blue/Green Perfect",
                        "Blue Sphere (Set 4) - Blue/Dark Blue Perfect")
















def connect_regions(world: MultiWorld, player: int, source: str, target: str, rule=None) -> Entrance:
    sourceRegion = world.get_region(source, player)
    targetRegion = world.get_region(target, player)
    return sourceRegion.connect(targetRegion, rule=rule)


def create_region(name: str, player: int, world: MultiWorld) -> SonicManiaRegion:
    region = SonicManiaRegion(name, player, world)
    world.regions.append(region)
    return region


def create_subregion(source_region: Region, name: str, *locs: str) -> SonicManiaRegion:
    region = SonicManiaRegion(name, source_region.player, source_region.multiworld)
    connection = Entrance(source_region.player, name, source_region)
    source_region.exits.append(connection)
    connection.connect(region)
    source_region.multiworld.regions.append(region)
    create_locs(region, *locs)
    return region


def set_subregion_access_rule(world, player, region_name: str, rule):
    world.get_entrance(world, player, region_name).access_rule = rule


def create_default_locs(reg: Region, default_locs: dict):
    create_locs(reg, *default_locs.keys())


def create_locs(reg: Region, *locs: str):
    reg.locations += [SonicManiaLocation(reg.player, loc_name, location_table[loc_name], reg) for loc_name in locs]
import typing
from enum import Enum

from BaseClasses import MultiWorld, Region, Entrance, Location
from .Options import SonicManiaOptions
from .Locations import SonicManiaLocation, location_table


class NoZones(int, Enum):#scared to delete this
    SOMETHING = 1

class SonicManiaRegion(Region):
    subregions: typing.List[Region] = []


def create_regions(world: MultiWorld, options: SonicManiaOptions, player: int):
    regMM = Region("Menu", player, world, "Level Select")
    #create_default_locs(regMM, locSS_table)#TODO this might break something
    world.regions.append(regMM)


    regGH1 = create_region("Green Hill 1", player, world)
    create_locs(regGH1,"Green Hill (Act 1) Clear","Green Hill (Act 1) Giant Ring - Knuckles Path",
    "Green Hill (Act 1) Giant Ring - Main Path","Green Hill (Act 1) Giant Ring - Lower Path Waterfall")
    regGH2 = create_region("Green Hill 2", player, world)
    create_locs(regGH2,"Green Hill (Act 2) Clear","Green Hill (Act 2) Giant Ring - Near First Zipline Chain",
    "Green Hill (Act 2) Giant Ring - Bottom Path Wall Behind Monitor","Green Hill (Act 2) Giant Ring - Waterfall Near Boss")

    regCP1 = create_region("Chemical Plant 1", player, world)
    create_locs(regCP1,"Chemical Plant (Act 1) Clear","Chemical Plant (Act 1) Giant Ring - Upper Path Near Yellow Springs",
    "Chemical Plant (Act 1) Giant Ring - Bottom Path Underwater Wall","Chemical Plant (Act 1) Giant Ring - Upper Path After Large Ramp",
    "Chemical Plant (Act 1) Giant Ring - Vertical Moving Blocks Bottom")
    regCP2 = create_region("Chemical Plant 2", player, world)
    create_locs(regCP2,"Chemical Plant (Act 2) Clear","Chemical Plant (Act 2) Giant Ring - Left After First Downwards Launch",
    "Chemical Plant (Act 2) Giant Ring - Long Purple Pad Fake Wall","Chemical Plant (Act 2) Giant Ring - Upper Path Moving Blocks")

    regSP1 = create_region("Studiopolis 1", player, world)
    create_locs(regSP1,"Studiopolis (Act 1) Clear","Studiopolis (Act 1) Giant Ring - Backwards Ramp Near Start",
    "Studiopolis (Act 1) Giant Ring - Top Path Fake Wall","Studiopolis (Act 1) Giant Ring - Lower Path Window Break Into Ramp")
    regSP2 = create_region("Studiopolis 2", player, world)
    create_locs(regSP2,"Studiopolis (Act 2) Clear","Studiopolis (Act 2) Giant Ring - Top Path Applause Sign",
    "Studiopolis (Act 2) Giant Ring - Platforms After Wire Launch","Studiopolis (Act 2) Giant Ring - Top Path Badnik Bounce Chain")

    regFB1 = create_region("Flying Battery 1", player, world)
    create_locs(regFB1,"Flying Battery (Act 1) Clear","Flying Battery (Act 1) Giant Ring - 1",
    "Flying Battery (Act 1) Giant Ring - 2")
    regFB2 = create_region("Flying Battery 2", player, world)
    create_locs(regFB2,"Flying Battery (Act 2) Clear","Flying Battery (Act 2) Giant Ring - 1",
    "Flying Battery (Act 2) Giant Ring - 2","Flying Battery (Act 2) Giant Ring - 3","Flying Battery (Act 2) Giant Ring - 4")

    regPG1 = create_region("Press Garden 1", player, world)
    create_locs(regPG1,"Press Garden (Act 1) Clear","Press Garden (Act 1) Giant Ring - 1","Press Garden (Act 1) Giant Ring - 2")
    regPG2 = create_region("Press Garden 2", player, world)
    create_locs(regPG2,"Press Garden (Act 2) Clear","Press Garden (Act 2) Giant Ring - 1",
    "Press Garden (Act 2) Giant Ring - 2","Press Garden (Act 2) Giant Ring - 3")

    regSS1 = create_region("Stardust Speedway 1", player, world)
    create_locs(regSS1,"Stardust Speedway (Act 1) Clear","Stardust Speedway (Act 1) Giant Ring - 1","Stardust Speedway (Act 1) Giant Ring - 2",
    "Stardust Speedway (Act 1) Giant Ring - 3")
    regSS2 = create_region("Stardust Speedway 2", player, world)
    create_locs(regSS2,"Stardust Speedway (Act 2) Clear","Stardust Speedway (Act 2) Giant Ring - 1","Stardust Speedway (Act 2) Giant Ring - 2",
    "Stardust Speedway (Act 2) Giant Ring - 3")

    regHC1 = create_region("Hydrocity 1", player, world)
    create_locs(regHC1,"Hydrocity (Act 1) Clear","Hydrocity (Act 1) Giant Ring - 1","Hydrocity (Act 1) Giant Ring - 2",
    "Hydrocity (Act 1) Giant Ring - 3")
    regHC2 = create_region("Hydrocity 2", player, world)
    create_locs(regHC2,"Hydrocity (Act 2) Clear","Hydrocity (Act 2) Giant Ring - 1","Hydrocity (Act 2) Giant Ring - 2")

    regMS1 = create_region("Mirage Saloon 1", player, world)
    create_locs(regMS1,"Mirage Saloon (Act 1 Normal) Clear","Mirage Saloon (Act 1 Knuckles) Clear","Mirage Saloon (Act 1 Normal) Giant Ring - Inside Train Car",
    "Mirage Saloon (Act 1 Knuckles) Giant Ring - 1","Mirage Saloon (Act 1 Knuckles) Giant Ring - 2","Mirage Saloon (Act 1 Knuckles) Giant Ring - 3")
    regMS2 = create_region("Mirage Saloon 2", player, world)
    create_locs(regMS2,"Mirage Saloon (Act 2) Clear","Mirage Saloon (Act 2) Giant Ring - 1","Mirage Saloon (Act 2) Giant Ring - 2","Mirage Saloon (Act 2) Giant Ring - 3")

    regOO1 = create_region("Oil Ocean 1", player, world)
    create_locs(regOO1,"Oil Ocean (Act 1) Clear","Oil Ocean (Act 1) Giant Ring - 1",
    "Oil Ocean (Act 1) Giant Ring - 2","Oil Ocean (Act 1) Giant Ring - 3")
    regOO2 = create_region("Oil Ocean 2", player, world)
    create_locs(regOO2,"Oil Ocean (Act 2) Clear","Oil Ocean (Act 2) Giant Ring - 1","Oil Ocean (Act 2) Giant Ring - 2")

    regLR1 = create_region("Lava Reef 1", player, world)
    create_locs(regLR1,"Lava Reef (Act 1) Clear","Lava Reef (Act 1) Giant Ring - 1","Lava Reef (Act 1) Giant Ring - 2")
    regLR2 = create_region("Lava Reef 2", player, world)
    create_locs(regLR2,"Lava Reef (Act 2) Clear","Lava Reef (Act 2) Giant Ring - 1","Lava Reef (Act 2) Giant Ring - 2",
    "Lava Reef (Act 2) Giant Ring - 3","Lava Reef (Act 2) Giant Ring - 4","Lava Reef (Act 2) Giant Ring - 5")

    regMM1 = create_region("Metallic Madness 1", player, world)
    create_locs(regMM1,"Metallic Madness (Act 1) Clear","Metallic Madness (Act 1) Giant Ring - 1",
    "Metallic Madness (Act 1) Giant Ring - 2","Metallic Madness (Act 1) Giant Ring - 3")
    regMM2 = create_region("Metallic Madness 2", player, world)
    create_locs(regMM2,"Metallic Madness (Act 2) Clear","Metallic Madness (Act 2) Giant Ring - 1","Metallic Madness (Act 2) Giant Ring - 2")

    regTM1 = create_region("Titanic Monarch 1", player, world)
    create_locs(regTM1,"Titanic Monarch (Act 1) Clear","Titanic Monarch (Act 1) Giant Ring - 1",
    "Titanic Monarch (Act 1) Giant Ring - 2")
    regTM2 = create_region("Titanic Monarch 2", player, world)
    create_locs(regTM2,"Titanic Monarch (Act 2) Clear","Titanic Monarch (Act 2) Giant Ring - 1")

    regSPEC = create_region("Special Stages", player, world)
    create_locs(regSPEC, "Special Stage 1 Clear", "Special Stage 2 Clear","Special Stage 3 Clear","Special Stage 4 Clear","Special Stage 5 Clear","Special Stage 6 Clear","Special Stage 7 Clear")

    if options.blue_spheres >0:
        regBS1 = create_region("Blue Spheres 1", player, world)
        regBS2 = create_region("Blue Spheres 2", player, world)
        regBS3 = create_region("Blue Spheres 3", player, world)
        regBS4 = create_region("Blue Spheres 4", player, world)

        create_locs(regBS1,"Blue Sphere (Set 1) - Orange/Brown Clear","Blue Sphere (Set 1) - Aqua/Green Clear",
        "Blue Sphere (Set 1) - White/Orange Clear","Blue Sphere (Set 1) - Lime/Green Clear","Blue Sphere (Set 1) - Orange/Aqua Clear",
        "Blue Sphere (Set 1) - Purple/Tan Clear","Blue Sphere (Set 1) - White/Lime Clear","Blue Sphere (Set 1) - Gray/Light Gray Clear")
        create_locs(regBS2,"Blue Sphere (Set 2) - Magenta/Lime Clear","Blue Sphere (Set 2) - Dark Blue/Aqua Clear",
        "Blue Sphere (Set 2) - Red/White Clear","Blue Sphere (Set 2) - Purple/Orange Clear","Blue Sphere (Set 2) - Light Blue/White Clear",
        "Blue Sphere (Set 2) - Blue/White Clear","Blue Sphere (Set 2) - Blue/Orange Clear","Blue Sphere (Set 2) - Blue/Off-White Clear")
        create_locs(regBS3,"Blue Sphere (Set 3) - Aqua/Light Blue Clear","Blue Sphere (Set 3) - Yellow/Purple Clear",
        "Blue Sphere (Set 3) - Black/Dark Blue Clear","Blue Sphere (Set 3) - Lime/Purple Clear","Blue Sphere (Set 3) - Orange/Yellow (Dark Sky) Clear",
        "Blue Sphere (Set 3) - Pink/Aqua Clear","Blue Sphere (Set 3) - Light Brown/Off-White Clear","Blue Sphere (Set 3) - Brown/Off-White Clear")
        create_locs(regBS4,"Blue Sphere (Set 4) - Lime/White Clear","Blue Sphere (Set 4) - Light Blue/Aqua Clear",
        "Blue Sphere (Set 4) - Orange/Yellow (Light Sky) Clear","Blue Sphere (Set 4) - Purple/Off-White Clear","Blue Sphere (Set 4) - Blue/Light Blue Clear",
        "Blue Sphere (Set 4) - Yellow/Dark Yellow Clear","Blue Sphere (Set 4) - Blue/Green Clear","Blue Sphere (Set 4) - Blue/Dark Blue Clear")
        if options.blue_spheres > 1:
            create_locs(regBS1, "Blue Sphere (Set 1) - Orange/Brown Perfect", "Blue Sphere (Set 1) - Aqua/Green Perfect",
                        "Blue Sphere (Set 1) - White/Orange Perfect", "Blue Sphere (Set 1) - Lime/Green Perfect",
                        "Blue Sphere (Set 1) - Orange/Aqua Perfect",
                        "Blue Sphere (Set 1) - Purple/Tan Perfect", "Blue Sphere (Set 1) - White/Lime Perfect",
                        "Blue Sphere (Set 1) - Gray/Light Gray Perfect")
            create_locs(regBS2, "Blue Sphere (Set 2) - Magenta/Lime Perfect",
                        "Blue Sphere (Set 2) - Dark Blue/Aqua Perfect",
                        "Blue Sphere (Set 2) - Red/White Perfect", "Blue Sphere (Set 2) - Purple/Orange Perfect",
                        "Blue Sphere (Set 2) - Light Blue/White Perfect",
                        "Blue Sphere (Set 2) - Blue/White Perfect", "Blue Sphere (Set 2) - Blue/Orange Perfect",
                        "Blue Sphere (Set 2) - Blue/Off-White Perfect")
            create_locs(regBS3, "Blue Sphere (Set 3) - Aqua/Light Blue Perfect",
                        "Blue Sphere (Set 3) - Yellow/Purple Perfect",
                        "Blue Sphere (Set 3) - Black/Dark Blue Perfect", "Blue Sphere (Set 3) - Lime/Purple Perfect",
                        "Blue Sphere (Set 3) - Orange/Yellow (Dark Sky) Perfect",
                        "Blue Sphere (Set 3) - Pink/Aqua Perfect", "Blue Sphere (Set 3) - Light Brown/Off-White Perfect",
                        "Blue Sphere (Set 3) - Brown/Off-White Perfect")
            create_locs(regBS4, "Blue Sphere (Set 4) - Lime/White Perfect", "Blue Sphere (Set 4) - Light Blue/Aqua Perfect",
                        "Blue Sphere (Set 4) - Orange/Yellow (Light Sky) Perfect",
                        "Blue Sphere (Set 4) - Purple/Off-White Perfect", "Blue Sphere (Set 4) - Blue/Light Blue Perfect",
                        "Blue Sphere (Set 4) - Yellow/Dark Yellow Perfect", "Blue Sphere (Set 4) - Blue/Green Perfect",
                        "Blue Sphere (Set 4) - Blue/Dark Blue Perfect")
















def connect_regions(world: MultiWorld, player: int, source: str, target: str, rule=None) -> Entrance:
    sourceRegion = world.get_region(source, player)
    targetRegion = world.get_region(target, player)
    return sourceRegion.connect(targetRegion, rule=rule)


def create_region(name: str, player: int, world: MultiWorld) -> SonicManiaRegion:
    region = SonicManiaRegion(name, player, world)
    world.regions.append(region)
    return region


def create_subregion(source_region: Region, name: str, *locs: str) -> SonicManiaRegion:
    region = SonicManiaRegion(name, source_region.player, source_region.multiworld)
    connection = Entrance(source_region.player, name, source_region)
    source_region.exits.append(connection)
    connection.connect(region)
    source_region.multiworld.regions.append(region)
    create_locs(region, *locs)
    return region


def set_subregion_access_rule(world, player, region_name: str, rule):
    world.get_entrance(world, player, region_name).access_rule = rule


def create_default_locs(reg: Region, default_locs: dict):
    create_locs(reg, *default_locs.keys())


def create_locs(reg: Region, *locs: str):
    reg.locations += [SonicManiaLocation(reg.player, loc_name, location_table[loc_name], reg) for loc_name in locs]
