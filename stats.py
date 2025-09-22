def word_counter(text):
    return len(text.split())


def character_counter(text):
    empty_count_dict = {}
    for character in text:
        character = character.lower()
        if not character.isalpha():
            pass
        elif character in empty_count_dict:
            empty_count_dict[character] += 1
        else:
            empty_count_dict[character] = 1
    
    return empty_count_dict


def sorted_dictionary(dictionary_of_characters):
    sorted_characters = sorted(
        dictionary_of_characters.items(), reverse=True, key=lambda pair: pair[1])
    return "\n".join(f"{k}: {v}" for k, v in sorted_characters)