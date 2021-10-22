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
