h = ["H1", "H2", "H3"]

f = ["F1", "F2", "F3"]

preferencesH = {
    "H1" : ["F1", "F3", "F2"],
    "H2" : ["F2", "F1", "F3"],
    "H3" : ["F3", "F2", "F1"]
}

preferencesF = {
    "F1": ["H2", "H3", "H1"],
    "F2": ["H1", "H2", "H3"],
    "F3": ["H3", "H1", "H1"]
}
            


def prefers(prefer_list,x, y):
    return prefer_list.index(x) < prefer_list.index(y)

def is_stable(a,b, preferencesH, preferencesF, matchs):
    return 



print(prefers(preferencesH["H3"], "F2", "F3"))    