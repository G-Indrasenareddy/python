from random import choice,choices
enames=["Indra","Shiva","Vishnu","raja","bhushan","modi","Rg"]

luck_name=choice(enames)
print(luck_name)

luck_draw_list=choices(enames,k=3)
print(luck_draw_list)