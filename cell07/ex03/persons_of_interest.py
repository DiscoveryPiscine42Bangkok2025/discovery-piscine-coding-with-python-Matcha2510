#cell 7-3
def famous_births(dic):
    for key, value in dic.items():
        print(f"{value['name']} is a great scientist born in {value['date_of_birth']}.")
women_scientists = {
 "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
 "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
 "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
 "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
 }

famous_births(women_scientists)