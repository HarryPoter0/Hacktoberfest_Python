# farm_animals = {"sheep", "hen",  "cow", "horse", "goat"}
# wild_animals =  {"lion", "tiger", "goat", "panther"}
#
# all = farm_animals.union(wild_animals)
# print(all)
#
# all2 = wild_animals.union(farm_animals)
# print(all2)
#
# all3 = wild_animals | farm_animals
# print(all3)

from prescription_data import adverse_interactions

meds_to_watch = set()
meds_to_watch2 = set()

for interaction in adverse_interactions:
    meds_to_watch1 = meds_to_watch.union(interaction)
    # meds_to_watch.update(interaction)
    meds_to_watch |= interaction

meds_to_watch2.update(*adverse_interactions)
print(sorted(meds_to_watch))
print(sorted(meds_to_watch1))
print(sorted(meds_to_watch2))
