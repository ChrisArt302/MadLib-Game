# Madlib using adjectives, nouns, and verbs with f strings.

adj1 = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
verb1 = input("Enter a verb: ")
noun1 = input("Enter a noun: ")
verb2 = input("Enter another verb: ")
adj3 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")
verb3 = input("Enter a past tense verb: ")

madlib = f"There was a {adj1} man, who enjoyed walking through\n" \
         f"his neighborhood. One day he noticed a {adj2} dog who\n" \
         f"was {verb1} his owner. The owner who was a {noun1},\n" \
         f"was {verb2}. On his way back home the man felt {adj3}\n" \
         f"and stopped at a {noun2} and {verb3} there. The end."

print(madlib)