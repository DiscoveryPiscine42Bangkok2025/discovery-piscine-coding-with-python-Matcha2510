#cell 7-1
def find_the_redheads(dic):
    return list(dict((k, v) for k, v in dic.items() if v == "red"))
dupont_family = {
 "florian": "red",
 "marie": "blond",
 "virginie": "brunette",
 "david": "red",
 "franck": "red"
 }

print(find_the_redheads(dupont_family))