# Quete = "\x1b[35mX\x1b[0m"
# FG=


# # \xb1[42m
# print(Quete)




import os,sys
# Variables
Prefix = "\x1b["
Style_Suffix = "m"
Reset = "0"
RED = "1"
GREEN = "2"
BLUE = "4"
FG_Prefix = "3"
BG_Prefix = "4"
Position_Suffix = "H"



os.system("")


print (f"{Prefix}{FG_Prefix}{RED};{BG_Prefix}{GREEN}{Style_Suffix}Rouge sur vert{Prefix}{Reset}{Style_Suffix}")

print(f"\x1b[31;42mRouge sur vert\x1b[0m")