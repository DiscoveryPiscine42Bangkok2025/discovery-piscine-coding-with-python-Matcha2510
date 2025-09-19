#cell 7-0
def array_of_names(dic):
    return [f"{key.capitalize()} {value.capitalize()}" for key, value in dic.items()]
persons = {
 "jean": "valjean",
 "grace": "hopper",
 "xavier": "niel",
 "fifi": "brindacier"
}

print(array_of_names(persons))