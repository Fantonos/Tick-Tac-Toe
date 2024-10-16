import random

playing_game = True

player_symbols = ["X", "0"]

tic_tac_dic = {
    "A1": " ", "A2": " ", "A3": " ",
    "B1": " ", "B2": " ", "B3": " ",
    "C1": " ", "C2": " ", "C3": " ",
}

pvp_gamemode_list = ["FRIENDS","FRIEND", "PVP", "1"]

help_codes_list = ["HELP", "H", "HE", "HEL"]

avail_tic_spots = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2","C3"]

wining_spots = {"Win 1": ["A1", "A2", "A3"], "Win 2": ["B1", "B2", "B3"], "Win 3": ["C1", "C2","C3"],
                "Win 4": ["A1", "B1", "C1"], "Win 5": ["A2", "B2", "C2"], "Win 6": ["A3", "B3", "C3"],
                "Win 8": ["A1", "B2", "C3"], "Win 9": ["A3", "B2", "C1"]}

spots_played_list = []

current_bot_move = "None"

def get_player_input(player_input, player):
    try:
        player_input = player_input.upper()
        if player_input not in spots_played_list and player_input in avail_tic_spots:
            tic_tac_dic[player_input] = player
            spots_played_list.append(player_input)
        elif player_input in help_codes_list:
            help_section(player_input)
            display_game_board()
            get_player_input(input(f'Current Player is {player}: '), player)
        else:
            display_game_board()
            print(f"It Aint Gonna Happen, Try again {player}!")
            get_player_input(input(f'Current Player is {player}: '), player)
    except exception as e:
        print(e)


def display_game_board():
    print(f'    (1) (2) (3) \nA) | {tic_tac_dic["A1"]} | {tic_tac_dic["A2"]} | {tic_tac_dic["A3"]} |\nB) | {tic_tac_dic["B1"]} | {tic_tac_dic["B2"]} | {tic_tac_dic["B3"]} |\nC) | {tic_tac_dic["C1"]} | {tic_tac_dic["C2"]} | {tic_tac_dic["C3"]} |')


def bots_move():
    avail_bot_spot = avail_tic_spots
    for spot in spots_played_list:
        if spot in avail_bot_spot:
            avail_bot_spot.remove(spot)
    current_bot_move = avail_bot_spot[random.randint(0, len(avail_bot_spot)-1)]
    print(f"The bot played {current_bot_move}")
    return current_bot_move


def help_section(userinput):
    if userinput in help_codes_list:
        print("""
    Welcome to Tic Tac Toe!
    The game board is as follows:
    
        (1)  (2)  (3)
    A) | A1 | A2 | A3 |
    B) | B1 | B2 | B3 |
    C) | C1 | C2 | C3 |
            
    You can play by typing the spot you want to play in the form of A1, B2, C3 etc.
        """)
    else:
        pass

def check_if_won(player):
    current_player_spots = []
    correct_spot_counter = 0

    for sec in tic_tac_dic:
        if tic_tac_dic[sec] == player:
            current_player_spots.append(sec)

    if len(spots_played_list) == 9:
        return "No Winners"

    if len(current_player_spots) >= 3:
        for spot in wining_spots:
            for i in range(0, len(current_player_spots)):
                if current_player_spots[i] in wining_spots[spot]:
                    correct_spot_counter += 1
            if correct_spot_counter != 3:
                correct_spot_counter = 0
            else:
                return "Winner"


def main(game_mode):
    while playing_game:
        for current_player in player_symbols:
            if game_mode not in pvp_gamemode_list and current_player == "X":
                get_player_input(input(f'Current Player is {current_player}: '), current_player)
            elif game_mode not in pvp_gamemode_list and current_player == "0":
                get_player_input(bots_move(), current_player)
            else:
                get_player_input(input(f'Current Player is {current_player}: '), current_player)
            display_game_board()
            if check_if_won(current_player) == "Winner":
                if game_mode not in pvp_gamemode_list and current_player == "0":
                    print("You Lost To A Bot!")
                    break
                else:
                    print(f'________________ \n Player {current_player} Won!')
                break
            elif check_if_won(current_player) == "No Winners":
                print(f'It`s a tie!')
                break
        if check_if_won(current_player):
            break


def start():
    gamemode = (input("--- Choose game mode ---\n[1. Player vs Player]\n[2. Player vs Bot]\n\nFor help type: Help\nEnter 1 or 2: ")).upper()
    if gamemode in ["BOTS", "FRIENDS", "BOT", "FRIEND", "PVP", "1", "2"]:
        display_game_board()
        main(gamemode)

    elif gamemode in help_codes_list:
        help_section(gamemode)
        start()
    else:
        print(f"Game Mode: '{gamemode}', is not supported")
        start()

start()
