Hommes = ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"]

Femmes = ["F1", "F2", "F3", "F4",  "F5", "F6", "F7", "F8"]

preferencesHommes = {
    "H1": ["F3", "F1", "F5","F7", "F4", "F2", "F8", "F6"],
    "H2": ["F6", "F1", "F3", "F4", "F8", "F7", "F5", "F2"],
    "H3": ["F7", "F4", "F3", "F6", "F5", "F1", "F2", "F8"],
    "H4": ["F5", "F3", "F8", "F2", "F6", "F1", "F4", "F7"],
    "H5":["F4", "F1", "F2", "F8", "F7", "F3", "F6", "F5"],
    "H6":["F6", "F2", "F5", "F7", "F8", "F4", "F3", "F1"],
    "H7":["F7", "F8", "F1", "F6", "F2", "F3", "F4", "F5"],
    "H8":["F2", "F6", "F7",  "F1", "F8", "F3", "F4", "F5"]
}

preferencesFemmes = {
    "F1": ["H4", "H3", "H8", "H1", "H2", "H5", "H7", "H6"],
    "F2": ["H3", "H7", "H5", "H8", "H6", "H4", "H1", "H2"],
    "F3": ["H7", "H5", "H8", "H3", "H6", "H2", "H1", "H4"],
    "F4": ["H6", "H4", "H2", "H7", "H3", "H1", "H5", "H8"],
    "F5": ["H8", "H7", "H1", "H5", "H6", "H4", "H3", "H2"],
    "F6": ["H5", "H4", "H7", "H6", "H2", "H8", "H3", "H1"],
    "F7": ["H1", "H4", "H5", "H6", "H2", "H8", "H3", "H7"],
    "F8": ["H2", "H5", "H4", "H3", "H7", "H8", "H1", "H6"]
}

def  prefers(preferences_list,a, b):
    return preferences_list.index(a)<preferences_list.index(b)

def is_stable(matching, preferencesH, preferencesF):
    for h, f in matching.items():
        for h2, f2 in matching.items():
        
            if h2 == h:
                continue
        
            if prefers(preferencesH[h], f2, f) and prefers(preferencesF[f2], h,h2):
                return False
    return True

def backtrack(i,H, F, preferencesH, preferencesF, matching, married):
    
    if i == len(H):
        if is_stable(matching, preferencesH, preferencesF):
            return matching.copy()
        return None
    
    h = H[i]
    
    for f in preferencesH[h]:
        if f not in married:
            
            matching[h] = f
            married.add(f)
                
            result = backtrack(i + 1, H, F, preferencesH, preferencesF, matching, married)
            if result is not None:
                return result

            married.remove(f)
            del matching[h]
    return None


matchs = backtrack(0, Hommes, Femmes, preferencesHommes, preferencesFemmes,{}, set())
print(matchs)
