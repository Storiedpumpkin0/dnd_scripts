# Author:   Andrew Hitchcock
# Date:     2/1/22
# Purpose:  This script will record player count, initiative, and possibly any changes to HP allong the way
#
# -------------------------------------------------------------------------------------------------------------
from operator import itemgetter
#variables

x = 0
combatant_names_and_scores = {}
player_count = int(input("How many players are there?"))
monster_count = int(input("how many monsters are there?"))

#get total combatants involved
total_combatants = player_count + monster_count

# get the relevant info from the players
print("enter combatants names, initiative scores")

while x < total_combatants :
    print("\n")
    combatant_name = input("enter combatant name: ")
    combatant_initiative = int(input("enter initiative:"))
    combatant_names_and_scores[combatant_name] = combatant_initiative
    x = x + 1

# print the order of combat
for k,v in reversed(sorted(combat_order.items(), key=itemgetter(1))):
    print (k,v)
    order_by_name.extend(k)
