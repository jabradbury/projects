import random

# dictionary of ghost names and descriptions
ghosts_desc = {"banshee": "Will only target one player at a time, and has a distinctive \'scream\' response with "
                          "the parabolic microphone.",
               "demon": "Can hunt at any sanity using it's ability and will hunt more often. "
                        "The crucifix has an increased effective range.",
               "deogen": "Always has LoS on all players, even when they are hiding, and will move quickly to their "
                         "location, "
                         "but is the slowest ghost in the game when close to players.",
               "goryo": "DOTS can only be seen through a camera, and will change favourite room less often.",
               "hantu": "Moves faster in cold rooms and slower in warm ones.",
               "jinn": "Moves quickly to close distance with the player, but only when the breaker is on.",
               "mare": "More likely to turn off or break lights, and will hunt at higher sanity in the dark.",
               "moroi": "Moves faster at lower player sanity and is blinded for longer by smudge sticks.",
               "myling": "Quieter during a hunt but more active on the parabolic microphone.",
               "obake": "Will sometimes hide its fingerprints or generate a six fingered handprint.",
               "oni": "Increased activity around players and is more visible during hunts. cannot do airball events.",
               "onryo": "Multiple candles in a room will act as crucifixes, an individual candle will trigger a hunt "
                        "when extinguished.",
               "phantom": "Less visible during hunts, and identified by clear ghost photos.",
               "poltergeist": "Can throw multiple objects at once, and will throw objects more often.",
               "raiju": "Moves faster near active electronics.",
               "revenant": "Moves faster with LoS of player and slowly without LoS.",
               "shade": "Less active than other ghosts, wont hunt or interact if player is in same room.",
               "spirit": "Smudge sticks prevent a hunt for 3 minutes instead of 2.",
               "thaye": "Very active at the start of a mission, becomes less active the more time it spends "
                        "near the player.",
               "the mimic": "Every 2 minutes will copy another ghosts traits, will always show ghost orbs.",
               "the twins": "Will often \'twinteract\' in two places at once. has a 50/50 chance to be slower/faster "
                            "than average with each hunt.",
               "wraith": "Does not generate footprints, can randomly teleport to players leaving EMF2",
               "yokai": "Talking near it can trigger a hunt. Yokai is a \'dumb\' hunter.",
               "yurei": "Can slam doors with a distinctive noise and drain sanity"}

# dictionary of ghost names and evidence
ghosts_ev = {"obake": "emf5, fingerprints, orbs",
             "demon": "freezing, book, fingerprints",
             "the mimic": "freezing, fingerprints, spirit box",
             "hantu": "freezing, orbs, fingerprints",
             "wraith": "dots, emf5, spirit box",
             "banshee": "orbs, fingerprints, dots",
             "deogen": "dots, spirit box, writing",
             "goryo": "dots, emf5, fingerprints",
             "jinn": "fingerprints, emf5, freezing",
             "mare": "orbs, spirit box, writing",
             "moroi": "spirit box, freezing, writing",
             "myling": "emf5, fingerprints, writing",
             "oni": "emf5, freezing, dots",
             "onryo": "orbs, spirit box, freezing",
             "phantom": "spirit box, fingerprints, dots",
             "poltergeist": "spirit box, fingerprints, writing",
             "raiju": "emf5, orbs, dots",
             "revenant": "orbs, freezing, writing",
             "shade": "emf5, freezing, writing",
             "spirit": "emf5, spirit box, writing",
             "thaye": "orbs, writing, dots",
             "the twins": "emf5, spirit box, freezing",
             "yokai": "orbs, spirit box, dots",
             "yurei": "orbs, freezing, dots"
             }

# Tarot Cards
tarot_cards = {"Wheel of Fortune: Red": "Lose 25 sanity", "Wheel of Fortune: Green": "Gain 25 sanity",
               "The Tower": "Trigger an interaction", "The Hermit": "Prevents the ghost from roaming for 1 minute",
               "Death": "Triggers a cursed hunt", "The Devil": "Triggers a ghost event",
               "The Hanged Man": "Instantly kills the player",
               "High Priestess": "Grants an extra life or revives a dead teammate",
               "The Fool": "Appears as another card first before revealing itself. Has no effect",
               "The Sun": "Fully restores sanity to 100", "The Moon": "Fully drains sanity to 0"}
# Ouija board locations
locations = ["living room", "garage", "kitchen", "boys bedroom", "girls bedroom",
             "master bedroom", "basement", "foyer", "hallway", "bathroom", "dining room"]

# main program
while True:
    # choose which part you want to use
    choice = input("Welcome to Jack's Phasmophobia Application! \n"
                   "1) Enter ghost name \n"
                   "2) Enter evidence \n"
                   "3) Tarot Cards \n"
                   "4) Ouija Board \n"
                   "Q) Quit \n"
                   "Which function would you like to use? ")

    print(choice)
    # search by name
    if choice == "1":
        while True:
            g_name = input("Please enter the name of a ghost, or Q to quit: ")
            print(g_name)
            if g_name == "q":
                break
            elif g_name.lower() in ghosts_desc:
                print(ghosts_desc[g_name.lower()])
                continue
            else:
                print("Name not recognised. Please try again.")
                continue
    # search by evidence
    elif choice == "2":
        print("Please input your evidence:")
        ev1 = input("1)")
        ev1 = ev1.lower()
        result1 = [key for key, value in ghosts_ev.items() if ev1 in value.lower()]

        ev2 = input("2)")
        ev2 = ev2.lower()
        result2 = [key for key, value in ghosts_ev.items() if ev2 in value.lower()]

        ev3 = input("3)")
        ev3 = ev3.lower()
        result3 = [key for key, value in ghosts_ev.items() if ev3 in value.lower()]

        final = set(result1) & set(result2) & set(result3)
        print("The ghost is: " + str(final))
        print(input("Press enter to continue "))

    elif choice == "3":
        print(input("You found the tarot cards! Press enter to start! "))
        total = 0
        while total < 10:
            card = random.choice(list(tarot_cards.items()))
            # random.choices(tarot_cards, weights=(10, 10, 20, 10, 10, 10, 1, 2, 17, 5, 5), k=1)
            print(card)
            if card == tarot_cards["The Hanged Man"]:
                print("Bad luck, you are dead!")
                break
            else:
                total += 1
                again = input("Pull another card? ")
                if again.lower() == "no":
                    print("You pulled all the tarot cards!")
                    break
                else:
                    continue

    elif choice == "4":
        print(input("You found the Ouija board! Press enter to start asking questions! "))
        sanity = 100
        while sanity > 0:
            question = input("Q: ")
            if question.lower() == "where are you":
                print(random.choice(list(locations)))
                sanity -= 40
                continue
            elif question.lower() == "where is the bone":
                print(random.choice(list(locations)))
                sanity -= 20
                continue
            elif question.lower() == "how old are you":
                print(random.randint(2, 90))
                sanity -= 5
                continue
            elif question.lower() == "goodbye":
                break
            else:
                print("The ouija board did not understand your question. Try again.")
                continue
        else:
            print(input("You don't have enough sanity to ask another question. Press enter to run and hide!"))

    # quit and invalid entries
    elif choice.lower() == "q":
        print("Thanks for using Jack's Phasmophobia app!")
        quit()
    else:
        print("Please enter a valid number.")
        continue