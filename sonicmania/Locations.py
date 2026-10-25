from BaseClasses import Location

class SonicManiaLocation(Location):
    game: str = "Sonic Mania"

#Bob-omb Battlefield
ghz_table = {
    "Green Hill (Act 1) Clear": 1,
    "Green Hill (Act 2) Clear": 2,

    "Green Hill (Act 1) Giant Ring 1 - Knuckles Path": 70,
    "Green Hill (Act 1) Giant Ring 2 - Lower Path Waterfall": 71,
    "Green Hill (Act 1) Giant Ring 3 - Main Path": 72,
    "Green Hill (Act 2) Giant Ring 1 - Near First Zipline Chain": 73,
    "Green Hill (Act 2) Giant Ring 2 - Bottom Path Fake Wall Behind Monitor": 74,
    "Green Hill (Act 2) Giant Ring 3 - Waterfall Near Boss": 75,

    "Green Hill (Encore Act 1) Clear": 40,
    "Green Hill (Encore Act 2) Clear": 41,

    "Green Hill (Encore Act 1) Giant Ring 1 - Suspended Underground Bridge": 138,
    "Green Hill (Encore Act 1) Giant Ring 2 - Top Path Pushable Rock": 139,
    "Green Hill (Encore Act 2) Giant Ring 1 - Under First Spike Bridge": 140,
    "Green Hill (Encore Act 2) Giant Ring 2 - Waterfall Near Boss": 141,


}
cpz_table = {
    "Chemical Plant (Act 1) Clear": 3,
    "Chemical Plant (Act 2) Clear": 4,

    "Chemical Plant (Act 1) Giant Ring 1 - Bottom Path Underwater Wall": 76,
    "Chemical Plant (Act 1) Giant Ring 2 - Upper Path Near Yellow Springs": 77,
    "Chemical Plant (Act 1) Giant Ring 3 - Upper Path After Large Ramp": 78,
    "Chemical Plant (Act 1) Giant Ring 4 - Vertical Moving Blocks Bottom": 79,
    "Chemical Plant (Act 2) Giant Ring 1 - Left After First Downwards Launch": 80,
    "Chemical Plant (Act 2) Giant Ring 2 - Long Purple Pad Fake Wall": 81,
    "Chemical Plant (Act 2) Giant Ring 3 - Upper Path Moving Blocks": 82,

    "Chemical Plant (Encore Act 1) Clear": 42,
    "Chemical Plant (Encore Act 2) Clear": 43,

    "Chemical Plant (Encore Act 1) Giant Ring 1 - Upper Path Near Yellow Springs": 142,#2
    "Chemical Plant (Encore Act 1) Giant Ring 2 - Middle Path Fenced Ceiling Hole": 143, #tails/knux/&tails#10
    "Chemical Plant (Encore Act 1) Giant Ring 3 - Top Path Loop Near End": 144,#11

    "Chemical Plant (Encore Act 2) Giant Ring 1 - Left After First Downwards Launch": 145,#1
    "Chemical Plant (Encore Act 2) Giant Ring 2 - Spiked Walls Near Spinning Platforms": 146,#10
    "Chemical Plant (Encore Act 2) Giant Ring 3 - Knuckles Path Fake Wall": 147,#11

}
spz_table = {
    "Studiopolis (Act 1) Clear": 5,
    "Studiopolis (Act 2) Clear": 6,

    "Studiopolis (Act 1) Giant Ring 1 - Backwards Ramp Near Start": 83,
    "Studiopolis (Act 1) Giant Ring 2 - Top Path Fake Wall": 84,
    "Studiopolis (Act 1) Giant Ring 3 - Lower Path Window Break Into Ramp": 85,
    "Studiopolis (Act 2) Giant Ring 1 - Top Path Applause Sign": 86,
    "Studiopolis (Act 2) Giant Ring 2 - Platforms After Wire Launch": 87,
    "Studiopolis (Act 2) Giant Ring 3 - Top Path Badnik Bounce Chain": 88,

    "Studiopolis (Encore Act 1) Clear": 44,
    "Studiopolis (Encore Act 2) Clear": 45,


    "Studiopolis (Encore Act 1) Giant Ring 2 - Top Path Behind Window": 148,#10
    "Studiopolis (Encore Act 1) Giant Ring 3 - Hornet Van Near Upper Projector": 149,#11
    "Studiopolis (Encore Act 1) Giant Ring 1 - Bottom Path Under First Clapperboard": 150,  # 12
    "Studiopolis (Encore Act 2) Giant Ring 1 - Middle Path Wire Near Red Springs": 151,#10
    "Studiopolis (Encore Act 2) Giant Ring 2 - Up Right Near Final Lotto Balls": 152,#11
}
fbz_table = {
    "Flying Battery (Act 1) Clear": 7,
    "Flying Battery (Act 2) Clear": 8,

    "Flying Battery (Act 1) Giant Ring 1 - Ceiling Magnets After 3rd Checkpoint": 89,
    "Flying Battery (Act 1) Giant Ring 2 - Room Before Boss Left Wall": 90,
    "Flying Battery (Act 2) Giant Ring 1 - Bottom Path Near First Fans": 91,
    "Flying Battery (Act 2) Giant Ring 2 - Outside Rising Chain Near Propellers": 92,
    "Flying Battery (Act 2) Giant Ring 3 - Outside Chain After Wind Tunnel": 93,
    "Flying Battery (Act 2) Giant Ring 4 - Magnets Above Inside Switch": 94,

    "Flying Battery (Encore Act 1) Clear": 46,
    "Flying Battery (Encore Act 2) Clear": 47,

    "Flying Battery (Encore Act 1) Giant Ring 1 - Above First Moving Platform": 153,#10
    "Flying Battery (Encore Act 1) Giant Ring 2 - Main Path Switch Near Gate": 154,#11
    "Flying Battery (Encore Act 1) Giant Ring 3 - Upper Path Breakable Ground": 155,#1
    "Flying Battery (Encore Act 2) Giant Ring 1 - Outside Rising Chain Near Propellers": 156,#2
    "Flying Battery (Encore Act 2) Giant Ring 2 - Second Outside Area Computer Room": 157,#10

}
pgz_table = {
    "Press Garden (Act 1) Clear": 9,
    "Press Garden (Act 2) Clear": 10,

    "Press Garden (Act 1) Giant Ring 1 - Left After First Spinning Tube": 95,
    "Press Garden (Act 1) Giant Ring 2 - Closed Gate Above Crusher": 96,
    "Press Garden (Act 2) Giant Ring 1 - Under 1st Checkpoint": 97,
    "Press Garden (Act 2) Giant Ring 2 - Top Path Behind Half Pipe Ice": 98,
    "Press Garden (Act 2) Giant Ring 3 - Ice Slide Fake Wall After Loop": 99,

    "Press Garden (Encore Act 1) Clear": 48,
    "Press Garden (Encore Act 2) Clear": 49,


    #2 Closed Gate Above Crusher #2
    #1 Crate Path Under First Spinning Tube #(bubble/mighty) 10
    #3 Crates Above Boss #11

    #1 Under 1st Checkpoint #1
    #3 Bottom Path Above Red Spring #10
    #2 High Path Above 1st Checkpoint #sonic+lightning/tails/knuckles/ray #11
}
ssz_table = {
    "Stardust Speedway (Act 1) Clear": 11,
    "Stardust Speedway (Act 2) Clear": 12,

    "Stardust Speedway (Act 1) Giant Ring 1 - Alt Upper Path Between Pillars": 100,
    "Stardust Speedway (Act 1) Giant Ring 2 - Bottom Spin Tunnels Spring Room": 101,
    "Stardust Speedway (Act 1) Giant Ring 3 - Upper Path Red Spring Near Vine": 102,
    "Stardust Speedway (Act 2) Giant Ring 1 - Bottom Path Inside Near Start": 103,
    "Stardust Speedway (Act 2) Giant Ring 2 - Bottom Path Inside Above Loops": 104,
    "Stardust Speedway (Act 2) Giant Ring 3 - Top Path Inside Ceiling Jump": 105,

    "Stardust Speedway (Encore Act 1) Clear": 50,
    "Stardust Speedway (Encore Act 2) Clear": 51,

    #High Ledge After First Upper Loop #Tails/Knux/&Tails
    #Bottom Spin Tunnels Spring Room
    #Above Middle Top Path Tube Loop

    #Bottom Path Inside Above Loops
    #Bottom Path Long Middle Spin Tunnel
    #Top Fences Near End


}
hcz_table = {
    "Hydrocity (Act 1) Clear": 13,
    "Hydrocity (Act 2) Clear": 14,

    "Hydrocity (Act 1) Giant Ring 1 - Upper Path Launch Near 1st Checkpoint": 106,
    "Hydrocity (Act 1) Giant Ring 2 - Middle Path Fall Into Water": 107,
    "Hydrocity (Act 1) Giant Ring 3 - Bottom Path Fake Wall Near Bubble Switch": 108,
    "Hydrocity (Act 2) Giant Ring 1 - 1st Water Slide Drop Underwater": 109,
    "Hydrocity (Act 2) Giant Ring 2 - Launch After Tallest Water Slide": 110,

    "Hydrocity (Encore Act 1) Clear": 52,
    "Hydrocity (Encore Act 2) Clear": 53,

    #Upper Path Platforms Above 1st Checkpoint
    #Upper Knuckles Path Under Falling Bridge #knuckles

    #Upper Path Above First Loop
    #Ceiling After First Water Slide Launch
    #Left After Last Water Slide Launch
}
msz_table = {
    "Mirage Saloon (Act 1 Normal) Clear": 15,
    "Mirage Saloon (Act 1 Knuckles) Clear": 16,
    "Mirage Saloon (Act 2) Clear": 17,

    "Mirage Saloon (Act 1 Normal) Giant Ring - Inside Train Car": 111,
    "Mirage Saloon (Act 1 Knuckles) Giant Ring 1 - Left Path Near Start": 112,
    "Mirage Saloon (Act 1 Knuckles) Giant Ring 2 - Final Bumper Section Top Left": 113,
    "Mirage Saloon (Act 1 Knuckles) Giant Ring 3 - Open Area Left Side": 114,
    "Mirage Saloon (Act 2) Giant Ring 2 - Left Top Path Breaking Sand Loop": 115,
    "Mirage Saloon (Act 2) Giant Ring 3 - Top Path Half Pipe Near Sprayer": 116,
    "Mirage Saloon (Act 2) Giant Ring 1 - Push Barrel Into Water Sprayer": 117,

    "Mirage Saloon (Encore Act 1) Clear": 54,
    "Mirage Saloon (Encore Act 2) Clear": 55,


    #1 Above Left Side Train Cars
    #2 Barrels Under Train Track
    #3 Lower Right Path Fake Wall
    #4 Inside Final Train

    # Original Knuckles Path Start
    # Bottom Owl Totem Knuckles Path #knux/7 ems
    # Top Path Under Sand Slope Near End
}

ooz_table = {
    "Oil Ocean (Act 1) Clear": 18,
    "Oil Ocean (Act 2) Clear": 19,

    "Oil Ocean (Act 1) Giant Ring 1 - First Flame Shield Fans": 118,
    "Oil Ocean (Act 1) Giant Ring 2 - Top Path Pipes": 119,
    "Oil Ocean (Act 1) Giant Ring 3 - Middle Path Fake Wall Near Elevator": 120,
    "Oil Ocean (Act 2) Giant Ring 1 - Under 1st Checkpoint": 121,
    "Oil Ocean (Act 2) Giant Ring 2 - Fake Wall Above 2nd Checkpoint Area": 122,

    "Oil Ocean (Encore Act 1) Clear": 56,
    "Oil Ocean (Encore Act 2) Clear": 57,

    # Main Path Above Second Elevator
    # Fake Wall Above End

    # Above 1st Checkpoint
    # Secret Sub

}
lrz_table = {
    "Lava Reef (Act 1) Clear": 20,
    "Lava Reef (Act 2) Clear": 21,

    "Lava Reef (Act 1) Giant Ring 1 - Behind First Spike Crusher": 123,
    "Lava Reef (Act 1) Giant Ring 2 - Lower Path Spin Elevators": 124,
    "Lava Reef (Act 2) Giant Ring 2 - Lower Path Crumbling Platforms": 125,
    "Lava Reef (Act 2) Giant Ring 3 - Fake Wall Near Moving Platforms": 126,
    "Lava Reef (Act 2) Giant Ring 4 - Bottom Path Iwamodoki Tunnel In Lava": 127,
    "Lava Reef (Act 2) Giant Ring 5 - Fake Floor After Walker": 128,
    "Lava Reef (Act 2) Giant Ring 1 - Knuckles Path": 129,

    "Lava Reef (Encore Act 1) Clear": 58,
    "Lava Reef (Encore Act 2) Clear": 59,

    # Upper Path Red Spring Fake Wall
    # Upper Path Platform Near Wood Scaffolding

    # Knuckles Path
    # Top Path High Above Spike Tubes #Tails/knux/RAY/&tails (LIGHTNING SHIELD PROBABLY BUT FUCK THAT
    # Lava After U-Turn Ramp
    # Lower Path High Wall Near End  #fuck ass badnik bounce but i dont care

}
mmz_table = {
    "Metallic Madness (Act 1) Clear": 22,
    "Metallic Madness (Act 2) Clear": 23,

    "Metallic Madness (Act 1) Giant Ring 1 - Bottom Path Above 1st Checkpoint": 130,
    "Metallic Madness (Act 1) Giant Ring 2 - First Background Path End": 131,
    "Metallic Madness (Act 1) Giant Ring 3 - Top Path Slopes Near End": 132,
    "Metallic Madness (Act 2) Giant Ring 1 - Bottom Path Near 2nd Checkpoint": 133,
    "Metallic Madness (Act 2) Giant Ring 2 - Hidden Spin Tunnel In Background": 134,

    "Metallic Madness (Encore Act 1) Clear": 60,
    "Metallic Madness (Encore Act 2) Clear": 61,

    # Upper Path Fence Above 1st Checkpoint #spindash/peelout/tails/&tails
    # Top Path Above Collapsing Bridges

    # Some Knuckles Path
    # High Wall Before Final Tube

}


tmz_table = {
    "Titanic Monarch (Act 1) Clear": 24,
    "Titanic Monarch (Act 2) Clear": 25,

    "Titanic Monarch (Act 1) Giant Ring 1 - Above 2nd Checkpoint": 135,
    "Titanic Monarch (Act 1) Giant Ring 2 - Lightning Shield Near Orbs": 136,
    "Titanic Monarch (Act 2) Giant Ring - Bottom Right Path Breakable Bumpers": 137,

    "Titanic Monarch (Encore Act 1) Clear": 62,
    "Titanic Monarch (Encore Act 2) Clear": 63,

    # Path Above 2nd Checkpoint
    # Fall Off Right Side Crane Platform

    # Top Right Path Fall Into First Portal

}
special_stage_table = {
    "Special Stage 1 Clear": 26,
    "Special Stage 2 Clear": 27,
    "Special Stage 3 Clear": 28,
    "Special Stage 4 Clear": 29,
    "Special Stage 5 Clear": 30,
    "Special Stage 6 Clear": 31,
    "Special Stage 7 Clear": 32,
    "Special Stage 8 Clear": 33,
    "Special Stage 9 Clear": 34,
    "Special Stage 10 Clear": 35,
    "Special Stage 11 Clear": 36,
    "Special Stage 12 Clear": 37,
    "Special Stage 13 Clear": 38,
    "Special Stage 14 Clear": 39,
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

"Blue Sphere (Set 1) - Orange/Brown Perfect": 233,
"Blue Sphere (Set 1) - Aqua/Green Perfect": 234,
"Blue Sphere (Set 1) - White/Orange Perfect": 235,
"Blue Sphere (Set 1) - Lime/Green Perfect": 236,
"Blue Sphere (Set 1) - Orange/Aqua Perfect": 237,
"Blue Sphere (Set 1) - Purple/Tan Perfect": 238,
"Blue Sphere (Set 1) - White/Lime Perfect": 239,
"Blue Sphere (Set 1) - Gray/Light Gray Perfect": 240,
"Blue Sphere (Set 2) - Magenta/Lime Perfect": 241,
"Blue Sphere (Set 2) - Dark Blue/Aqua Perfect": 242,
"Blue Sphere (Set 2) - Red/White Perfect": 243,
"Blue Sphere (Set 2) - Purple/Orange Perfect": 244,
"Blue Sphere (Set 2) - Light Blue/White Perfect": 245,
"Blue Sphere (Set 2) - Blue/White Perfect": 246,
"Blue Sphere (Set 2) - Blue/Orange Perfect": 247,
"Blue Sphere (Set 2) - Blue/Off-White Perfect": 248,
"Blue Sphere (Set 3) - Aqua/Light Blue Perfect": 249,
"Blue Sphere (Set 3) - Yellow/Purple Perfect": 250,
"Blue Sphere (Set 3) - Black/Dark Blue Perfect": 251,
"Blue Sphere (Set 3) - Lime/Purple Perfect": 252,
"Blue Sphere (Set 3) - Orange/Yellow (Dark Sky) Perfect": 253,
"Blue Sphere (Set 3) - Pink/Aqua Perfect": 254,
"Blue Sphere (Set 3) - Light Brown/Off-White Perfect": 255,
"Blue Sphere (Set 3) - Brown/Off-White Perfect": 256,
"Blue Sphere (Set 4) - Lime/White Perfect": 257,
"Blue Sphere (Set 4) - Light Blue/Aqua Perfect": 258,
"Blue Sphere (Set 4) - Orange/Yellow (Light Sky) Perfect": 259,
"Blue Sphere (Set 4) - Purple/Off-White Perfect": 260,
"Blue Sphere (Set 4) - Blue/Light Blue Perfect": 261,
"Blue Sphere (Set 4) - Yellow/Dark Yellow Perfect": 262,
"Blue Sphere (Set 4) - Blue/Green Perfect": 263,
"Blue Sphere (Set 4) - Blue/Dark Blue Perfect": 264,


}

achievement_table = {
    "Achievement: Superstar": 265,
    "Achievement: That's a Two-fer": 266,
    "Achievement: Magnificent Seven": 267,
    "Achievement: See You Next Game": 268,
    "Achievement: Full Medal Jacket": 269,
    "Achievement: No Way? No Way!": 270,
    "Achievement: Now It Can't Hurt You Anymore": 271,
    "Achievement: Triple Trouble": 272,
    "Achievement: The Most Famous Hedgehog in the World": 273,
    "Achievement: Window Shopping": 274,
    "Achievement: Crate Expectations": 275,
    "Achievement: King of Speed": 276,
    "Achievement: Boat Enthusiast": 277,
    "Achievement: The Password is 'Special Stage'": 278,
    "Achievement: Secret Sub": 279,
    "Achievement: Without a Trace": 280,
    "Achievement: Collect 'Em All": 281,
    "Achievement: Professional Hedgehog": 282,
}

location_table = {**ghz_table,**cpz_table,**spz_table,**fbz_table,**pgz_table,**ssz_table,**hcz_table,**msz_table,**ooz_table,**lrz_table,**mmz_table,**tmz_table,**special_stage_table,**blue_sphere_table, **achievement_table}
