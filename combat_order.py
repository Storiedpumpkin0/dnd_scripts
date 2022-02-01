# Author:   Andrew Hitchcock
# Date:     2/1/22
# Purpose:  This script will record player count, initiative, and possibly any changes to HP allong the way
#
# -------------------------------------------------------------------------------------------------------------
from operator import itemgetter
import pandas as pd

#variables
x = 0
combatant_names_and_scores = {}
output_dir = "C:\\Users\\hitch\\Documents\\DND_Hitchcock_house\\combat\\"
player_count = int(input("How many players are there?"))
monster_count = int(input("how many monsters are there?"))
output_df = pd.DataFrame()

#get total combatants involved
total_combatants = player_count + monster_count

# add players and initiative scores to a dictionary
while x < total_combatants :
    print("\n")
    combatant_name = input("enter combatant name: ")
    combatant_initiative = int(input("enter initiative:"))
    combatant_names_and_scores[combatant_name] = combatant_initiative
    x = x + 1

# save the dictonary in decending order (highest first) to get the order of combat
for k,v in reversed(sorted(combatant_names_and_scores .items(), key=itemgetter(1))):
    output_df = output_df.append({'Name': str(k), 'Initiative': str(v), 'HP': ""}, ignore_index = True)

# write the output as a csv
output_df.to_csv(output_dir + "combat_order.csv", index=False)