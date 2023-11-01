def pluralize(word):
    if word == "moose":
        return "moose"
    elif word == "automaton":
        return "automata"
    elif word == "mouse":
        return "mice"
    else:
        return word + "s"

def pluralize_word():
    user_input = input("Word please: ")
    pluralized_word = pluralize(user_input)
    print(pluralized_word)

pluralize_word()