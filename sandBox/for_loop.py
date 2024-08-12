dic = {'Azamat': "father", "Nuzhamal": "Mother", "Tamchy": "doughter", "Altai": "Son"}

for name in dic:
    print(f"Name is {name}")

for name, relation in dic.items():
    print(f"Name is {name}, is {relation}")