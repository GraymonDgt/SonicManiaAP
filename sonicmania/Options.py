import typing
from dataclasses import dataclass
from Options import DefaultOnToggle, Range, Toggle, DeathLink, Choice, PerGameCommonOptions, OptionSet, OptionGroup, OptionCounter, OptionList



class BlueSpheres(Choice):
    """Toggle Blue Spheres
    CURRENTLY NONFUNCTIONAL
    Clear - Each stage has 1 check for clearing it
    Perfect - Each stage has 2 checks, 1 for clearing and another for clearing with a perfect"""
    option_off = 0
    option_clear = 1
    option_perfect = 2
    default = 0
    display_name = "Blue Sphere Toggle"

class EncoreMode(Toggle):
    """placeholder"""
    display_name = "Encore Mode"

class CompletionType(Choice):
    """Set goal for Victory Condition
    CURRENTLY NONFUNCTIONAL (only good ending works)
    Bad Ending - Beat Titanic Monarch Act 2
    Good Ending - Beat Titanic Monarch Act 2 with all Chaos Emeralds"""
    display_name = "Completion Goal"
    option_Bad_Ending = 0
    option_Good_Ending = 1

class FillerWeights(OptionCounter):
    """
    Determines the ratio of each filler item
    """
    default = {
        "1UP": 4,
        "10 Rings": 25,
        "Shield": 10,
        "Hyper Ring": 5,
        "1000 Points": 8,
        "Invincibility": 12,
        "Super Sneakers": 12,
    }
    display_name = "Filler Weights"

class TrapWeights(OptionCounter):
    """
    Determines the ratio of each trap
    """
    default = {
        "Placebo Trap": 4
    }
    display_name = "Trap Weights"

class TrapPercentage(Range):
    """Percentage of filler items to replace with traps"""
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 30


class RingLink(Choice):
    """Enable Ringlink (share rings with other games)"""
    option_off = 0
    option_on = 1
    display_name = "Ring Link"



mania_options_groups = [
    OptionGroup("Location Toggles", [
        BlueSpheres,
        EncoreMode
    ]),
    OptionGroup("Meta Options", [
        CompletionType,
        FillerWeights,
        TrapWeights,
        TrapPercentage,
        RingLink,
    ]),
]

@dataclass
class SonicManiaOptions(PerGameCommonOptions):

    blue_spheres: BlueSpheres
    encore_mode: EncoreMode
    filler_weights: FillerWeights
    trap_weights: TrapWeights
    trap_percent: TrapPercentage
    completion_type: CompletionType
    ring_link: RingLink
    death_link: DeathLink

