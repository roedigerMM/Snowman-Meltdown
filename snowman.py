from game_logic import play_game

def main():
    play_game()
    while True:
        replay = input("\nDo you want to play again? (y/n)").lower()
        if replay == "n":
            print("\nThank you for playing The Snowman Meltdown!")
            break
        elif replay == "y":
            play_game()

if __name__ == "__main__":
    main()