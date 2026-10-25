from typing import NamedTuple

from BaseClasses import Item, ItemClassification


class SonicManiaItem(Item):
    game: str = "Sonic Mania"

class SonicManiaItemData(NamedTuple):
    code: int | None = None
    classification: ItemClassification = ItemClassification.progression


generic_item_data_table: dict[str, SonicManiaItemData] = {

"Chaos Emerald": SonicManiaItemData(99),


"Medal": SonicManiaItemData(140, ItemClassification.progression_deprioritized_skip_balancing),
"Blue Sphere Set 1": SonicManiaItemData(141),
"Blue Sphere Set 2": SonicManiaItemData(142),
"Blue Sphere Set 3": SonicManiaItemData(143),
"Blue Sphere Set 4": SonicManiaItemData(144),



#mode / ability unlocks ie mean bean, da garden, etc
#no time limit
#& knuckles

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
"Spike Bug": SonicManiaItemData(121, ItemClassification.trap),
"Size Laser": SonicManiaItemData(122, ItemClassification.trap),
"Ground Speed Cap": SonicManiaItemData(123, ItemClassification.trap),
"Sonic Origins Classic Mode": SonicManiaItemData(124, ItemClassification.trap),
"Max Blue Sphere Speed": SonicManiaItemData(125, ItemClassification.trap),
"Ordinary Trap": SonicManiaItemData(126, ItemClassification.trap),
"Babysit Partner": SonicManiaItemData(127, ItemClassification.trap),
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
full_zone_item_data_table: dict[str, SonicManiaItemData] = {

"Green Hill Zone": SonicManiaItemData(37),
"Chemical Plant Zone": SonicManiaItemData(38),
"Studiopolis Zone": SonicManiaItemData(39),
"Flying Battery Zone": SonicManiaItemData(40),
"Press Garden Zone": SonicManiaItemData(41),
"Stardust Speedway Zone": SonicManiaItemData(42),
"Hydrocity Zone": SonicManiaItemData(43),
"Mirage Saloon Zone": SonicManiaItemData(44),
"Oil Ocean Zone": SonicManiaItemData(45),
"Lava Reef Zone": SonicManiaItemData(46),
"Metallic Madness Zone": SonicManiaItemData(47),
"Titanic Monarch Zone": SonicManiaItemData(48),

"Special Stage 1": SonicManiaItemData(30),
"Special Stage 2": SonicManiaItemData(31),
"Special Stage 3": SonicManiaItemData(32),
"Special Stage 4": SonicManiaItemData(33),
"Special Stage 5": SonicManiaItemData(34),
"Special Stage 6": SonicManiaItemData(35),
"Special Stage 7": SonicManiaItemData(36),
}
encore_item_data_table: dict[str, SonicManiaItemData] = {

"Encore Green Hill Zone (Act 1)": SonicManiaItemData(49),
"Encore Green Hill Zone (Act 2)": SonicManiaItemData(50),
"Encore Chemical Plant Zone (Act 1)": SonicManiaItemData(51),
"Encore Chemical Plant Zone (Act 2)": SonicManiaItemData(52),
"Encore Studiopolis Zone (Act 1)": SonicManiaItemData(53),
"Encore Studiopolis Zone (Act 2)": SonicManiaItemData(54),
"Encore Flying Battery Zone (Act 1)": SonicManiaItemData(55),
"Encore Flying Battery Zone (Act 2)": SonicManiaItemData(56),
"Encore Press Garden Zone (Act 1)": SonicManiaItemData(57),
"Encore Press Garden Zone (Act 2)": SonicManiaItemData(58),
"Encore Stardust Speedway Zone (Act 1)": SonicManiaItemData(59),
"Encore Stardust Speedway Zone (Act 2)": SonicManiaItemData(60),
"Encore Hydrocity Zone (Act 1)": SonicManiaItemData(61),
"Encore Hydrocity Zone (Act 2)": SonicManiaItemData(62),
"Encore Mirage Saloon Zone (Act 1)": SonicManiaItemData(63),
"Encore Mirage Saloon Zone (Act 2)": SonicManiaItemData(64),
"Encore Oil Ocean Zone (Act 1)": SonicManiaItemData(65),
"Encore Oil Ocean Zone (Act 2)": SonicManiaItemData(66),
"Encore Lava Reef Zone (Act 1)": SonicManiaItemData(67),
"Encore Lava Reef Zone (Act 2)": SonicManiaItemData(68),
"Encore Metallic Madness Zone (Act 1)": SonicManiaItemData(69),
"Encore Metallic Madness Zone (Act 2)": SonicManiaItemData(70),
"Encore Titanic Monarch Zone (Act 1)": SonicManiaItemData(71),
"Encore Titanic Monarch Zone (Act 2)": SonicManiaItemData(72),

"Special Stage 8": SonicManiaItemData(73),
"Special Stage 9": SonicManiaItemData(74),
"Special Stage 10": SonicManiaItemData(75),
"Special Stage 11": SonicManiaItemData(76),
"Special Stage 12": SonicManiaItemData(77),
"Special Stage 13": SonicManiaItemData(78),
"Special Stage 14": SonicManiaItemData(79),


}
full_encore_item_data_table: dict[str, SonicManiaItemData] = {

"Encore Green Hill Zone": SonicManiaItemData(80),
"Encore Chemical Plant Zone": SonicManiaItemData(81),
"Encore Studiopolis Zone": SonicManiaItemData(82),
"Encore Flying Battery Zone": SonicManiaItemData(83),
"Encore Press Garden Zone": SonicManiaItemData(84),
"Encore Stardust Speedway Zone": SonicManiaItemData(85),
"Encore Hydrocity Zone": SonicManiaItemData(86),
"Encore Mirage Saloon Zone": SonicManiaItemData(87),
"Encore Oil Ocean Zone": SonicManiaItemData(88),
"Encore Lava Reef Zone": SonicManiaItemData(89),
"Encore Metallic Madness Zone": SonicManiaItemData(90),
"Encore Titanic Monarch Zone": SonicManiaItemData(91),

"Special Stage 8": SonicManiaItemData(73),
"Special Stage 9": SonicManiaItemData(74),
"Special Stage 10": SonicManiaItemData(75),
"Special Stage 11": SonicManiaItemData(76),
"Special Stage 12": SonicManiaItemData(77),
"Special Stage 13": SonicManiaItemData(78),
"Special Stage 14": SonicManiaItemData(79),
}



ability_item_data_table: dict[str, SonicManiaItemData] = {
"& Tails": SonicManiaItemData(145),
"& Knuckles": SonicManiaItemData(146),
"No Time Limit": SonicManiaItemData(147,ItemClassification.useful),
#"Starting Hyper Ring": SonicManiaItemData(148,ItemClassification.useful),
"Super Peelout": SonicManiaItemData(98),
"Spindash": SonicManiaItemData(97),
"Insta-shield": SonicManiaItemData(96,ItemClassification.useful),
}

item_data_table = {
    **generic_item_data_table,
    **traps_item_data_table,
    **character_item_data_table,
    **shield_item_data_table,
    **zone_item_data_table,
    **ability_item_data_table,
    **full_zone_item_data_table,
    **encore_item_data_table,
    **full_encore_item_data_table,
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
