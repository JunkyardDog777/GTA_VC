from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x664558, Add, 7),# units:Graphics  index:96    from 200 To 207
        SetMemory(0x660650, Add, -32),# units:Unit Direction  index:96    from 32 To 0
        SetMemory(0x6624D0, Add, 48640),# units:Hit Points  index:96    from 15360 To 64000
        SetMemory(0x6631B0, Add, 68),# units:Elevation Level  index:96    from 4 To 72
        SetMemory(0x663E30, Add, 22),# units:Rank/Sublabel  index:96    from 0 To 22
        SetMemory(0x6622C8, Add, -164),# units:Human AI Idle  index:96    from 166 To 2
        SetMemory(0x6648F8, Add, -164),# units:Return to Idle  index:96    from 166 To 2
        SetMemory(0x663380, Add, -178),# units:Attack Unit  index:96    from 188 To 10
        SetMemory(0x663AB0, Add, -186),# units:Attack Move  index:96    from 188 To 2
        SetMemory(0x663718, Add, -1),# units:Ground Weapon  index:96    from 130 To 129
        SetMemory(0x664640, Add, 1),# units:Max Ground Hits  index:96    from 0 To 1
        SetMemory(0x664200, Add, 536870916),# units:Special Ability Flags  index:96    from 402718720 To 939589636
        SetMemory(0x662E18, Add, 6),# units:Target Acquisition Range  index:96    from 0 To 6
        SetMemory(0x663264, Add, 100663296),# units:Sight Range  index:47    from 5 To 11
        SetMemory(0x663298, Add, -7),# units:Sight Range  index:96    from 7 To 0
        SetMemory(0x65FF28, Add, 3),# units:Armor  index:96    from 0 To 3
        SetMemory(0x6620F8, Add, -1),# units:Right-click Action  index:96    from 2 To 1
        SetMemory(0x660070, Add, -738),# units:What Sound Start  index:96    from 968 To 230
        SetMemory(0x662CB0, Add, -737),# units:What Sound End  index:96    from 970 To 233
        SetMemory(0x663BF8, Add, 226),# units:Piss Sound Start  index:96    from 0 To 226
        SetMemory(0x661FA8, Add, 229),# units:Piss Sound End  index:96    from 0 To 229
        SetMemory(0x663CD0, Add, 234),# units:Yes Sound Start  index:96    from 0 To 234
        SetMemory(0x661500, Add, 237),# units:Yes Sound End  index:96    from 0 To 237
        SetMemory(0x6629E0, Add, -31),# units:StarEdit Placement Box Width  index:96    from 32 To 1
        SetMemory(0x6629E0, Add, -2031616),# units:StarEdit Placement Box Height  index:96    from 32 To 1
        SetMemory(0x661AC8, Add, -15),# units:Unit Size Left  index:96    from 16 To 1
        SetMemory(0x661AC8, Add, -983040),# units:Unit Size Up  index:96    from 16 To 1
        SetMemory(0x661ACC, Add, -15),# units:Unit Size Right  index:96    from 15 To 0
        SetMemory(0x661ACC, Add, -983040),# units:Unit Size Down  index:96    from 15 To 0
        SetMemory(0x663048, Add, -10),# units:Portrait  index:96    from 103 To 93
        SetMemory(0x663948, Add, -1),# units:Mineral Cost  index:96    from 1 To 0
        SetMemory(0x65FDC0, Add, -1),# units:Vespene Cost  index:96    from 1 To 0
        SetMemory(0x6604E8, Add, 1499),# units:Build Time  index:96    from 1 To 1500
        SetMemory(0x663800, Add, -126),# units:Staredit Group Flags  index:96    from 136 To 10
        SetMemory(0x664470, Add, -254),# units:Space Required  index:96    from 255 To 1
        SetMemory(0x663F78, Add, 690),# units:Destroy Score  index:96    from 10 To 700
        SetMemory(0x6615D8, Add, -503),# units:Staredit Availability Flags  index:96    from 966 To 463
        SetMemory(0x66D4D8, Add, -1),# images:Use Full Iscript  index:0    from 1 To 0
        SetMemory(0x66D5C0, Add, -256),# images:Use Full Iscript  index:233    from 1 To 0
        SetMemory(0x66D6D0, Add, -16777216),# images:Use Full Iscript  index:507    from 1 To 0
        SetMemory(0x667718, Add, -1),# images:Draw If Cloaked  index:0    from 1 To 0
        SetMemory(0x669E28, Add, 12),# images:Draw Function  index:0    from 0 To 12
        SetMemory(0x66EC48, Add, 223),# images:Iscript ID  index:0    from 0 To 223
        SetMemory(0x66F2A4, Add, 35),# images:Iscript ID  index:407    from 215 To 250
    ])

