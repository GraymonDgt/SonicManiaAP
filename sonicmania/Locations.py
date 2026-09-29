from BaseClasses import Location

class SonicManiaLocation(Location):
    game: str = "Sonic Mania"

#Bob-omb Battlefield
ghz_table = {
    "Green Hill (Act 1) Clear": 1,
    "Green Hill (Act 2) Clear": 2,

    "Green Hill (Act 1) Giant Ring 1 - Knuckles Path": 80,
    "Green Hill (Act 1) Giant Ring 2 - Lower Path Waterfall": 81,
    "Green Hill (Act 1) Giant Ring 3 - Main Path": 82,
    "Green Hill (Act 2) Giant Ring 1 - Near First Zipline Chain": 83,
    "Green Hill (Act 2) Giant Ring 2 - Bottom Path Fake Wall Behind Monitor": 84,
    "Green Hill (Act 2) Giant Ring 3 - Waterfall Near Boss": 85,
}
cpz_table = {
    "Chemical Plant (Act 1) Clear": 3,
    "Chemical Plant (Act 2) Clear": 4,

    "Chemical Plant (Act 1) Giant Ring 1 - Bottom Path Underwater Wall": 86,
    "Chemical Plant (Act 1) Giant Ring 2 - Upper Path Near Yellow Springs": 87,
    "Chemical Plant (Act 1) Giant Ring 3 - Upper Path After Large Ramp": 88,
    "Chemical Plant (Act 1) Giant Ring 4 - Vertical Moving Blocks Bottom": 89,
    "Chemical Plant (Act 2) Giant Ring 1 - Left After First Downwards Launch": 90,
    "Chemical Plant (Act 2) Giant Ring 2 - Long Purple Pad Fake Wall": 91,
    "Chemical Plant (Act 2) Giant Ring 3 - Upper Path Moving Blocks": 92,
}
spz_table = {
    "Studiopolis (Act 1) Clear": 5,
    "Studiopolis (Act 2) Clear": 6,

    "Studiopolis (Act 1) Giant Ring 1 - Backwards Ramp Near Start": 93,
    "Studiopolis (Act 1) Giant Ring 2 - Top Path Fake Wall": 94,
    "Studiopolis (Act 1) Giant Ring 3 - Lower Path Window Break Into Ramp": 95,
    "Studiopolis (Act 2) Giant Ring 1 - Top Path Applause Sign": 96,
    "Studiopolis (Act 2) Giant Ring 2 - Platforms After Wire Launch": 97,
    "Studiopolis (Act 2) Giant Ring 3 - Top Path Badnik Bounce Chain": 98,
}
fbz_table = {
    "Flying Battery (Act 1) Clear": 7,
    "Flying Battery (Act 2) Clear": 8,

    "Flying Battery (Act 1) Giant Ring 1 - Ceiling Magnets After 3rd Checkpoint": 99,
    "Flying Battery (Act 1) Giant Ring 2 - Room Before Boss Left Wall": 100,
    "Flying Battery (Act 2) Giant Ring 1 - Bottom Path Near First Fans": 101,
    "Flying Battery (Act 2) Giant Ring 2 - Outside Rising Chain Near Propellers": 102,
    "Flying Battery (Act 2) Giant Ring 3 - Outside Chain After Wind Tunnel": 103,
    "Flying Battery (Act 2) Giant Ring 4 - Magnets Above Inside Switch": 104,
}
pgz_table = {
    "Press Garden (Act 1) Clear": 9,
    "Press Garden (Act 2) Clear": 10,

    "Press Garden (Act 1) Giant Ring 1 - Left After First Spinning Tube": 105,
    "Press Garden (Act 1) Giant Ring 2 - Closed Gate Above Crusher": 106,
    "Press Garden (Act 2) Giant Ring 1 - Under 1st Checkpoint": 107,
    "Press Garden (Act 2) Giant Ring 2 - Top Path Behind Half Pipe Ice": 108,
    "Press Garden (Act 2) Giant Ring 3 - Ice Slide Fake Wall After Loop": 109,
}
ssz_table = {
    "Stardust Speedway (Act 1) Clear": 11,
    "Stardust Speedway (Act 2) Clear": 12,

    "Stardust Speedway (Act 1) Giant Ring 1 - Alt Upper Path Between Pillars": 110,
    "Stardust Speedway (Act 1) Giant Ring 2 - Bottom Spin Tunnels Spring Room": 111,
    "Stardust Speedway (Act 1) Giant Ring 3 - Upper Path Red Spring Near Vine": 112,
    "Stardust Speedway (Act 2) Giant Ring 1 - Bottom Path Inside Near Start": 113,
    "Stardust Speedway (Act 2) Giant Ring 2 - Bottom Path Small Inside Space": 114,
    "Stardust Speedway (Act 2) Giant Ring 3 - Top Path Inside Ceiling Jump": 115,
}
hcz_table = {
    "Hydrocity (Act 1) Clear": 13,
    "Hydrocity (Act 2) Clear": 14,

    "Hydrocity (Act 1) Giant Ring 1 - Upper Path Launch Near 1st Checkpoint": 116,
    "Hydrocity (Act 1) Giant Ring 2 - Middle Path Fall Into Water": 117,
    "Hydrocity (Act 1) Giant Ring 3 - Bottom Path Fake Wall Near Bubble Switch": 118,
    "Hydrocity (Act 2) Giant Ring 1 - 1st Water Slide Drop Underwater": 119,
    "Hydrocity (Act 2) Giant Ring 2 - Launch After Tallest Water Slide": 120,
}
msz_table = {
    "Mirage Saloon (Act 1 Normal) Clear": 15,
    "Mirage Saloon (Act 1 Knuckles) Clear": 16,
    "Mirage Saloon (Act 2) Clear": 17,

    "Mirage Saloon (Act 1 Normal) Giant Ring - Inside Train Car": 121,
    "Mirage Saloon (Act 1 Knuckles) Giant Ring 1 - Left Path Near Start": 122,
    "Mirage Saloon (Act 1 Knuckles) Giant Ring 2 - Final Bumper Section Top Left": 123,
    "Mirage Saloon (Act 1 Knuckles) Giant Ring 3 - Open Area Left Side": 124,
    "Mirage Saloon (Act 2) Giant Ring 2 - Left Top Path Breaking Sand Loop": 125,
    "Mirage Saloon (Act 2) Giant Ring 3 - Top Path Half Pipe Near Sprayer": 126,
    "Mirage Saloon (Act 2) Giant Ring 1 - Push Barrel Into Water Sprayer": 127,
}

ooz_table = {
    "Oil Ocean (Act 1) Clear": 18,
    "Oil Ocean (Act 2) Clear": 19,

    "Oil Ocean (Act 1) Giant Ring 1 - First Flame Shield Fans": 128,
    "Oil Ocean (Act 1) Giant Ring 2 - Top Path Pipes": 129,
    "Oil Ocean (Act 1) Giant Ring 3 - Middle Path Fake Wall Near Elevator": 130,
    "Oil Ocean (Act 2) Giant Ring 1 - Under 1st Checkpoint": 131,
    "Oil Ocean (Act 2) Giant Ring 2 - Fake Wall Above 2nd Checkpoint Area": 132,
}
lrz_table = {
    "Lava Reef (Act 1) Clear": 20,
    "Lava Reef (Act 2) Clear": 21,

    "Lava Reef (Act 1) Giant Ring 1 - Behind First Spike Crusher": 133,
    "Lava Reef (Act 1) Giant Ring 2 - Lower Path Spin Elevators": 134,
    "Lava Reef (Act 2) Giant Ring 2 - Lower Path Crumbling Platforms": 135,
    "Lava Reef (Act 2) Giant Ring 3 - Fake Wall Near Moving Platforms": 136,
    "Lava Reef (Act 2) Giant Ring 4 - Bottom Path Iwamodoki Tunnel In Lava": 137,
    "Lava Reef (Act 2) Giant Ring 5 - Fake Floor After Walker": 138,
    "Lava Reef (Act 2) Giant Ring 1 - Knuckles Path": 139,
}
mmz_table = {
    "Metallic Madness (Act 1) Clear": 22,
    "Metallic Madness (Act 2) Clear": 23,

    "Metallic Madness (Act 1) Giant Ring 1 - Bottom Path Above 1st Checkpoint": 140,
    "Metallic Madness (Act 1) Giant Ring 2 - First Background Path End": 141,
    "Metallic Madness (Act 1) Giant Ring 3 - Top Path Slopes Near End": 142,
    "Metallic Madness (Act 2) Giant Ring 1 - Bottom Path Near 2nd Checkpoint": 143,
    "Metallic Madness (Act 2) Giant Ring 2 - Hidden Spin Tunnel In Background": 144,
}
tmz_table = {
    "Titanic Monarch (Act 1) Clear": 24,
    "Titanic Monarch (Act 2) Clear": 25,

    "Titanic Monarch (Act 1) Giant Ring 1 - Above 2nd Checkpoint": 145,
    "Titanic Monarch (Act 1) Giant Ring 2 - Lightning Shield Near Orbs": 146,
    "Titanic Monarch (Act 2) Giant Ring - Bottom Right Path Breakable Bumpers": 147,
}
special_stage_table = {
    "Special Stage 1 Clear": 26,
    "Special Stage 2 Clear": 27,
    "Special Stage 3 Clear": 28,
    "Special Stage 4 Clear": 29,
    "Special Stage 5 Clear": 30,
    "Special Stage 6 Clear": 31,
    "Special Stage 7 Clear": 32,
}

blue_sphere_table = {

"Blue Sphere (Set 1) - Orange/Brown Clear": 201,
"Blue Sphere (Set 1) - Aqua/Green Clear": 202,
"Blue Sphere (Set 1) - White/Orange Clear": 203,
"Blue Sphere (Set 1) - Lime/Green Clear": 204,
"Blue Sphere (Set 1) - Orange/Aqua Clear": 205,
"Blue Sphere (Set 1) - Purple/Tan Clear": 206,
"Blue Sphere (Set 1) - White/Lime Clear": 207,
"Blue Sphere (Set 1) - Gray/Light Gray Clear": 208,
"Blue Sphere (Set 2) - Magenta/Lime Clear": 209,
"Blue Sphere (Set 2) - Dark Blue/Aqua Clear": 210,
"Blue Sphere (Set 2) - Red/White Clear": 211,
"Blue Sphere (Set 2) - Purple/Orange Clear": 212,
"Blue Sphere (Set 2) - Light Blue/White Clear": 213,
"Blue Sphere (Set 2) - Blue/White Clear": 214,
"Blue Sphere (Set 2) - Blue/Orange Clear": 215,
"Blue Sphere (Set 2) - Blue/Off-White Clear": 216,
"Blue Sphere (Set 3) - Aqua/Light Blue Clear": 217,
"Blue Sphere (Set 3) - Yellow/Purple Clear": 218,
"Blue Sphere (Set 3) - Black/Dark Blue Clear": 219,
"Blue Sphere (Set 3) - Lime/Purple Clear": 220,
"Blue Sphere (Set 3) - Orange/Yellow (Dark Sky) Clear": 221,
"Blue Sphere (Set 3) - Pink/Aqua Clear": 222,
"Blue Sphere (Set 3) - Light Brown/Off-White Clear": 223,
"Blue Sphere (Set 3) - Brown/Off-White Clear": 224,
"Blue Sphere (Set 4) - Lime/White Clear": 225,
"Blue Sphere (Set 4) - Light Blue/Aqua Clear": 226,
"Blue Sphere (Set 4) - Orange/Yellow (Light Sky) Clear": 227,
"Blue Sphere (Set 4) - Purple/Off-White Clear": 228,
"Blue Sphere (Set 4) - Blue/Light Blue Clear": 229,
"Blue Sphere (Set 4) - Yellow/Dark Yellow Clear": 230,
"Blue Sphere (Set 4) - Blue/Green Clear": 231,
"Blue Sphere (Set 4) - Blue/Dark Blue Clear": 232,

"Blue Sphere (Set 1) - Orange/Brown Perfect": 241,
"Blue Sphere (Set 1) - Aqua/Green Perfect": 242,
"Blue Sphere (Set 1) - White/Orange Perfect": 243,
"Blue Sphere (Set 1) - Lime/Green Perfect": 244,
"Blue Sphere (Set 1) - Orange/Aqua Perfect": 245,
"Blue Sphere (Set 1) - Purple/Tan Perfect": 246,
"Blue Sphere (Set 1) - White/Lime Perfect": 247,
"Blue Sphere (Set 1) - Gray/Light Gray Perfect": 248,
"Blue Sphere (Set 2) - Magenta/Lime Perfect": 249,
"Blue Sphere (Set 2) - Dark Blue/Aqua Perfect": 240,
"Blue Sphere (Set 2) - Red/White Perfect": 241,
"Blue Sphere (Set 2) - Purple/Orange Perfect": 242,
"Blue Sphere (Set 2) - Light Blue/White Perfect": 243,
"Blue Sphere (Set 2) - Blue/White Perfect": 244,
"Blue Sphere (Set 2) - Blue/Orange Perfect": 245,
"Blue Sphere (Set 2) - Blue/Off-White Perfect": 246,
"Blue Sphere (Set 3) - Aqua/Light Blue Perfect": 247,
"Blue Sphere (Set 3) - Yellow/Purple Perfect": 248,
"Blue Sphere (Set 3) - Black/Dark Blue Perfect": 249,
"Blue Sphere (Set 3) - Lime/Purple Perfect": 240,
"Blue Sphere (Set 3) - Orange/Yellow (Dark Sky) Perfect": 241,
"Blue Sphere (Set 3) - Pink/Aqua Perfect": 242,
"Blue Sphere (Set 3) - Light Brown/Off-White Perfect": 243,
"Blue Sphere (Set 3) - Brown/Off-White Perfect": 244,
"Blue Sphere (Set 4) - Lime/White Perfect": 245,
"Blue Sphere (Set 4) - Light Blue/Aqua Perfect": 246,
"Blue Sphere (Set 4) - Orange/Yellow (Light Sky) Perfect": 247,
"Blue Sphere (Set 4) - Purple/Off-White Perfect": 248,
"Blue Sphere (Set 4) - Blue/Light Blue Perfect": 249,
"Blue Sphere (Set 4) - Yellow/Dark Yellow Perfect": 240,
"Blue Sphere (Set 4) - Blue/Green Perfect": 241,
"Blue Sphere (Set 4) - Blue/Dark Blue Perfect": 242,


}

achievement_table = {
    "Achievement: Superstar": 160,
    "Achievement: That's a Two-fer": 161,
    "Achievement: Magnificent Seven": 162,
    "Achievement: See You Next Game": 163,
    "Achievement: Full Medal Jacket": 164,
    "Achievement: No Way? No Way!": 165,
    "Achievement: Now It Can't Hurt You Anymore": 166,
    "Achievement: Triple Trouble": 167,
    "Achievement: The Most Famous Hedgehog in the World": 168,
    "Achievement: Window Shopping": 169,
    "Achievement: Crate Expectations": 170,
    "Achievement: King of Speed": 171,
    "Achievement: Boat Enthusiast": 172,
    "Achievement: The Password is 'Special Stage'": 173,
    "Achievement: Secret Sub": 174,
    "Achievement: Without a Trace": 175,
    "Achievement: Collect 'Em All": 176,
    "Achievement: Professional Hedgehog": 177,
}

location_table = {**ghz_table,**cpz_table,**spz_table,**fbz_table,**pgz_table,**ssz_table,**hcz_table,**msz_table,**ooz_table,**lrz_table,**mmz_table,**tmz_table,**special_stage_table,**blue_sphere_table, **achievement_table}
