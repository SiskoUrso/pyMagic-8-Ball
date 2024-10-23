import random, os

answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
    "No",
    "Nope",
    "Definitely not",
]

def colored_text(text, color):
    return f"\033[{color}m{text}\033[0m"

art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠞⠛⠋⠉⠉⠉⠉⠙⠛⠳⠶⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡾⠋⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡾⠋⢠⣾⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀
⠀⠀⢠⡞⠀⣰⣿⣿⡟⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣶⣦⣄⠀⠀⠀⢳⡄⠀⠀
⠀⠀⣾⠁⣰⣿⣿⠏⠀⠀⠀⠀⠀⢀⣾⣿⣿⡟⢛⣛⠛⣿⣿⣧⡀⠀⠈⣷⠀⠀
⠀⢸⡏⠀⣿⣿⡏⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣇⠻⠿⠠⣿⣿⣿⣧⠀⠀⢹⡇⠀
⠀⢸⡇⠀⣿⡟⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⡟⢰⣿⣷⠈⣿⣿⡟⠀⠀⢸⡇⠀
⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣄⣉⣡⣼⣿⡿⠁⠀⠀⣸⡇⠀
⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⣿⣿⡿⠟⠋⠀⠀⠀⢀⡿⠀⠀
⠀⠀⠘⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠃⠀⠀
⠀⠀⠀⠈⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠶⢦⣤⣄⣀⣀⣀⣀⣠⣤⡴⠶⠋⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

game_on = True

while game_on:
    print(art)
    print("    The Magic 8-Ball says...")
    answer = random.choice(answers)
    index = answers.index(answer)
    if index < 10:
        print(colored_text(answer, 32))
    elif 10 <= index < 15:
        print(colored_text(answer, 94))
    else:
        print(colored_text(answer, 31))
    
    while True:
        user_choice = input("Would you like to shake again? (y/n) ").strip().lower()
        if user_choice == "n":
            game_on = False
            break
        elif user_choice == "y":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            game_on = True
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
