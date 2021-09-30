import random
import time
import nltk


def first_riddle():
    start_time = time.time()
    while True:
        present_time = time.time()
        if present_time - start_time > 120:
            first_train = False

        alice = nltk.corpus.gutenberg.raw("alice.txt")
        alice = alice.replace("\n", " ")
        alice = alice.replace("\r", " ")
        alice = alice.replace("\'", " ")

        alice_tokenized_sentences = nltk.sent_tokenize(alice)

        # get random sentence from alice_tokenized_sentences list
        random_sentence = random.choice(alice_tokenized_sentences)

        # print('this is the random sentence : ' + random_sentence)

        # tokenize the chosen sentence
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        word_tokens = tokenizer(random_sentence)
        word_tokens_lowered = [x.lower() for x in word_tokens]

        # get random word index, if the 'word' is not a type of punctuation it gets chosen
        random_word_index = -1 # TODO: if necessary
        while True:
            random_word_index = random.randint(0, len(word_tokens_lowered) - 1)
            if not word_tokens_lowered[random_word_index] in ".,!?':;":
                break

        solution = word_tokens_lowered[random_word_index]

        # get the pos tag for each word in the sentence
        pos_tag_list_for_word_tokens = nltk.pos_tag(word_tokens)
        pos_tag_of_word = f"{pos_tag_list_for_word_tokens[random_word_index][1]}"

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
        print(f'The answer is < {solution} >')
        answer = input(">>> ").lower()
        for sentence in range(0, 3):
            print(sentence)
            # put the cheating rule in place
            if answer == '###':
                print("Okay, this time I'm gonna turn a blind eye."
                      f"If you're interested, the solution was '{solution}'.")
                return get_trainticket is True
            # if the right word was guessed you get won the riddle
            if answer == solution:
                print(f"You're right! The word was {solution}, here is your trainticket.")
                return get_trainticket is True
            if answer != solution:
                print("I am sorry this was not the right word.")
                has_ticket = False


if __name__ == "__main__":
    first_riddle()

