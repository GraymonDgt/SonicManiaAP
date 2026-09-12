from typing import NamedTuple

from BaseClasses import Item, ItemClassification


class SonicManiaItem(Item):
    game: str = "Sonic Mania"

class SonicManiaItemData(NamedTuple):
    code: int | None = None
    classification: ItemClassification = ItemClassification.progression


generic_item_data_table: dict[str, SonicManiaItemData] = {

"Chaos Emerald": SonicManiaItemData(99),


"Blue Sphere Medal": SonicManiaItemData(140, ItemClassification.progression_deprioritized_skip_balancing),
"Blue Sphere Set 1": SonicManiaItemData(141),
"Blue Sphere Set 2": SonicManiaItemData(142),
"Blue Sphere Set 3": SonicManiaItemData(143),
"Blue Sphere Set 4": SonicManiaItemData(144),

#mode / ability unlocks ie mean bean, da garden, etc
"Shield": SonicManiaItemData(100, ItemClassification.filler),
"10 Rings": SonicManiaItemData(101, ItemClassification.filler),
"Hyper Ring": SonicManiaItemData(102, ItemClassification.filler),
"Invincibility": SonicManiaItemData(103, ItemClassification.filler),
"Super Sneakers": SonicManiaItemData(104, ItemClassification.filler),
"1UP": SonicManiaItemData(105, ItemClassification.filler),
"1000 Points": SonicManiaItemData(106, ItemClassification.filler),
}
traps_item_data_table:dict[str, SonicManiaItemData] = {
"Placebo Trap": SonicManiaItemData(120, ItemClassification.trap),#apply a bunch of minor status effects
}

character_item_data_table: dict[str, SonicManiaItemData] = {
    "Sonic": SonicManiaItemData(1),
    "Tails": SonicManiaItemData(2),
    "Knuckles": SonicManiaItemData(3),
    "Mighty": SonicManiaItemData(4),
    "Ray": SonicManiaItemData(5),
}

shield_item_data_table: dict[str, SonicManiaItemData] = {

    #"Bubble Shield": SonicManiaItemData(31),
    #"Lighting Shield": SonicManiaItemData(32),
    #"Flame Shield": SonicManiaItemData(33),

}



zone_item_data_table: dict[str, SonicManiaItemData] = {

"Green Hill Zone (Act 1)": SonicManiaItemData(6),
"Green Hill Zone (Act 2)": SonicManiaItemData(7),
"Chemical Plant Zone (Act 1)": SonicManiaItemData(8),
"Chemical Plant Zone (Act 2)": SonicManiaItemData(9),
"Studiopolis Zone (Act 1)": SonicManiaItemData(10),
"Studiopolis Zone (Act 2)": SonicManiaItemData(11),
"Flying Battery Zone (Act 1)": SonicManiaItemData(12),
"Flying Battery Zone (Act 2)": SonicManiaItemData(13),
"Press Garden Zone (Act 1)": SonicManiaItemData(14),
"Press Garden Zone (Act 2)": SonicManiaItemData(15),
"Stardust Speedway Zone (Act 1)": SonicManiaItemData(16),
"Stardust Speedway Zone (Act 2)": SonicManiaItemData(17),
"Hydrocity Zone (Act 1)": SonicManiaItemData(18),
"Hydrocity Zone (Act 2)": SonicManiaItemData(19),
"Mirage Saloon Zone (Act 1)": SonicManiaItemData(20),
"Mirage Saloon Zone (Act 2)": SonicManiaItemData(21),
"Oil Ocean Zone (Act 1)": SonicManiaItemData(22),
"Oil Ocean Zone (Act 2)": SonicManiaItemData(23),
"Lava Reef Zone (Act 1)": SonicManiaItemData(24),
"Lava Reef Zone (Act 2)": SonicManiaItemData(25),
"Metallic Madness Zone (Act 1)": SonicManiaItemData(26),
"Metallic Madness Zone (Act 2)": SonicManiaItemData(27),
"Titanic Monarch Zone (Act 1)": SonicManiaItemData(28),
"Titanic Monarch Zone (Act 2)": SonicManiaItemData(29),

"Special Stage 1": SonicManiaItemData(30),
"Special Stage 2": SonicManiaItemData(31),
"Special Stage 3": SonicManiaItemData(32),
"Special Stage 4": SonicManiaItemData(33),
"Special Stage 5": SonicManiaItemData(34),
"Special Stage 6": SonicManiaItemData(35),
"Special Stage 7": SonicManiaItemData(36),


}


ability_item_data_table: dict[str, SonicManiaItemData] = {

"Super Peelout": SonicManiaItemData(98),
"Spindash": SonicManiaItemData(97),
"Insta-shield": SonicManiaItemData(96),
}

item_data_table = {
    **generic_item_data_table,
    **traps_item_data_table,
    **character_item_data_table,
    **shield_item_data_table,
    **zone_item_data_table,
    **ability_item_data_table}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
