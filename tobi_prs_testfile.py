from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import random

def tokenized_and_replace():
    # replace non
    alice = nltk.corpus.gutenberg.raw('carroll-alice.txt')
    alice = alice.replace('\n', ' ')
    alice = alice.replace('\r', ' ')
    alice = alice.replace('\'', " ")

    alice_tokenized_sentences = sent_tokenize(alice)

    # get random sentence from alice_tokenized_sentences list
    random_sentence = random.choice(alice_tokenized_sentences)

    #print('this is the random sentence : ' + random_sentence)

    # tokenize the chosen sentence
    word_tokens = nltk.word_tokenize(random_sentence)
    word_tokens_lowered = [x.lower() for x in word_tokens]



    # get random word index, if the 'word' is not a type of punctuation it gets chosen
    while True:
        random_word_index = random.randint(0, len(word_tokens_lowered) - 1)
        if not word_tokens_lowered[random_word_index] in ".,!?':;":
            break



    random_word_for_exchange = word_tokens_lowered[random_word_index]
    #print(random_word_for_exchange)

    # get the pos tag for each word in the sentence
    pos_tag_list_for_word_tokens = nltk.pos_tag(word_tokens)
    pos_tag_of_word = f"{pos_tag_list_for_word_tokens[random_word_index][1]}"

    word_tokens[random_word_index] = f"<{pos_tag_of_word}>"
    output_sentence = ' '.join(word_tokens) \
                         .replace(" ,", ",") \
                         .replace(" .", ".") \
                         .replace(" :", ":") \
                         .replace(" !", "!") \
                         .replace(" ?", "?") \
                         .replace(" ;", ";")

    print(output_sentence)



if __name__ == '__main__':
    tokenized_and_replace()

