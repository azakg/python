motrocycles = ['yamaha', 'honda', 'suzuki', 'harley']
print(motrocycles)

del motrocycles[0] # deleting first element from list
print(motrocycles)

popped_motocycle = motrocycles.pop() # remove and assign it to variable
"""Also you can remove and assign it to varivale any element from list 
just need point element (popped_motorcycle = motorcycles.pop(0))"""
print(motrocycles)
print(popped_motocycle)

#remove element by name
motrocycles.remove('honda')
print(motrocycles)