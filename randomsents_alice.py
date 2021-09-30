import nltk
import random
import time


def tokenized_and_replace():
    start_time = time.time()
    while True:
        present_time = time.time()
        if present_time - start_time > 120:
            print("You're over the 2 minute time limit")
            break

        alice = nltk.corpus.gutenberg.raw('carroll-alice.txt')
        alice = alice \
            .replace("\n", " ") \
            .replace("\r", " ") \
            .replace("\'", " ")

        alice_tokenized_sentences = nltk.sent_tokenize(alice)

        # get random sentence from alice_tokenized_sentences list
        random_sentence = random.choice(alice_tokenized_sentences)

        print(f'this is the random sentence : {random_sentence}')

        # tokenize the chosen sentence
        word_tokens = nltk.word_tokenize(random_sentence)
        word_tokens_lowered = [x.lower() for x in word_tokens]

        # get random word index, if the 'word' is not
        # a type of punctuation it gets chosen
        random_word_index = -1
        while True:
            random_word_index = random.randint(0, len(word_tokens_lowered) - 1)
            if not word_tokens_lowered[random_word_index] in ".,!?':;":
                break

        solution = word_tokens_lowered[random_word_index]

        # get the pos tag for each word in the sentence
        pos_tag_list = nltk.pos_tag(word_tokens)
        pos_tag_of_word = f"{pos_tag_list[random_word_index][1]}"

        word_tokens[random_word_index] = f"<{pos_tag_of_word}>"
        output_sentence = " ".join(word_tokens) \
            .replace(" ,", ",") \
            .replace(" .", ".") \
            .replace(" :", ":") \
            .replace(" !", "!") \
            .replace(" ?", "?") \
            .replace(" ;", ";") \
            .replace(" \'", "\'")
        # print the sentence
        print(output_sentence)
        print('Can you guess the missing word?')
        print(f'The answer is "{solution}"')
        for sentence in range(0, 3):
            answer = input(">>> ").lower()
            # put the cheating rule in place
            if answer == '###':
                print("Okay, this time I'm gonna turn a blind eye.")
                print(f"If you're interested, the solution was '{solution}'.")
                break
            # if the right word was guessed you get won the riddle
            elif answer == solution:
                print(f"You're right! The word was '{solution}', here is your trainticket.")
                break
            else:
                print("I am sorry this was not the right word.")


if __name__ == "__main__":
    tokenized_and_replace()
