import typing
from dataclasses import dataclass
from Options import DefaultOnToggle, Range, Toggle, DeathLink, Choice, PerGameCommonOptions, OptionSet, OptionGroup, OptionCounter, OptionList



class BlueSpheres(Choice):
    """Toggle Blue Spheres
    Clear - Each stage has 1 check for clearing it
    Perfect - Each stage has 2 checks, 1 for clearing and another for clearing with a perfect"""
    option_off = 0
    option_clear = 1
    option_perfect = 2
    default = 0
    display_name = "Blue Sphere Toggle"

class EncoreDLC(DefaultOnToggle):
    """Enable encore DLC
    Turning this off will force any DLC related options/items off"""
    display_name = "Encore DLC Toggle"


class EncoreMode(Choice):
    """Include encore mode zones
    Combined - Encore zones unlock alongside mania zones
    Per Mode - Encore zones have separate items
    Exclusive - Only include encore zones, no normal stages
    PLACEHOLDER, NONFUNCTIONAL"""
    option_off = 0
    option_combined = 1
    option_per_mode = 2
    option_exclusive = 3
    display_name = "Encore Mode"

class Actsanity(Toggle):
    """Split zones unlocks into individual acts
    ie: Green Hill Zone -> Green Hill Zone (Act 1), Green Hill Zone (Act 2)"""
    display_name = "Actsanity"

class Achievementsanity(Toggle):
    """Toggle achievement checks"""
    display_name = "Achievementsanity"

class HiddenMonitors(Choice):
    """Set how hidden monitors revealed by the signpost should work
    Vanilla - Locations related to the hidden monitors are included
    Reveal - Monitors will be shown and re-hidden after collection
    Exclude - Related locations are excluded and won't send checks"""
    option_vanilla = 0
    option_reveal = 1
    option_exclude = 2
    display_name = "Hidden Monitors"

class CompletionType(Choice):
    """Set goal for Victory Condition
    Bad Ending - Beat Titanic Monarch Act 2
    Good Ending - Beat Egg Reverie Zone with all Chaos Emeralds
    True Ending - Achieve any ending with Knuckles & Knuckles"""
    display_name = "Completion Goal"
    option_Bad_Ending = 0
    option_Good_Ending = 1
    option_True_Ending = 2
    default = 1

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
        "Spike Bug": 8,
        "Size Laser": 8,
        "Ground Speed Cap":8,
        #"Max Blue Sphere Speed":8
        #ordinary trap
    }
    display_name = "Trap Weights"

class TrapPercentage(Range):
    """Percentage of filler items to replace with traps"""
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 30


class RingLink(Choice):
    """When someone else gains/loses rings, you do as well. The reverse is true as well."""
    option_off = 0
    option_on = 1
    display_name = "RingLink"



mania_options_groups = [
    OptionGroup("Location Toggles", [
        BlueSpheres,
        EncoreMode
    ]),
    OptionGroup("Meta Options", [
        EncoreDLC,
        Actsanity,
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
    achievementsanity: Achievementsanity
    dlc_toggle: EncoreDLC
    encore_mode: EncoreMode
    actsanity: Actsanity
    filler_weights: FillerWeights
    trap_weights: TrapWeights
    trap_percent: TrapPercentage
    completion_type: CompletionType
    ring_link: RingLink
    death_link: DeathLink

