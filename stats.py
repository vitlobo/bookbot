def get_num_words(text):
    words = text.split()
    return len(words)

def get_times_used(text):
    character_used = {}
    for c in text:
        if c in character_used:
            character_used[c] += 1
        else:
            character_used[c] = 1
    return character_used

def sort_on(item):
    return item["num"]

def sort_dict(this_dict):
    list_of_dicts = []
    for k in this_dict:
        list_of_dicts.append({"char": k, "num": this_dict[k]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts