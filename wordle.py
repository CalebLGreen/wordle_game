from random import randint


def initialise():
    with open("potential_words.txt", "r") as all_words:
        words = [x.strip() for x in all_words]
        idx_word = randint(0, len(words))
        word = str(words[idx_word])
    game_loop(word, guesses=6)


def game_loop(word, guesses):
    # print(word)
    while guesses > 0:
        print("=" * 50, f"Guesses remaining {guesses}", "=" * 50, sep="\n")
        guess = str(input("Guess a 5 Letter Word\n"))
        if len(guess) != 5:
            print("Guess must be 5 letters long")
        else:
            (
                correct,
                correct_place,
                correct_place_list,
                wrong_place,
                wrong_place_list,
            ) = compare(word, guess)
            if correct:
                print(f"You got the word correct!\nYou had {guesses} remaining")
                break
            else:
                print(
                    f"The following letters are in the right place: {correct_place_list}",
                    f"The following letters are in the wrong place but correct: {wrong_place_list}",
                    sep="\n",
                )
                guesses -= 1
    print(f"The word was {word}, good attempt")


def compare(word, guess):
    # print(word, guess)
    if word == guess:
        correct = True
        return correct, 0, 0, 0, 0
    else:
        correct = False
        correct_place = 0
        correct_place_list = []
        wrong_place = 0
        wrong_place_list = []
        for idx, letter in enumerate(guess):
            if letter in word and guess[idx] == word[idx]:
                correct_place = +1
                correct_place_list.append(letter)
            elif letter in word and guess[idx] != word[idx]:
                wrong_place = +1
                wrong_place_list.append(letter)
        return correct, correct_place, correct_place_list, wrong_place, wrong_place_list


if __name__ == "__main__":
    initialise()
