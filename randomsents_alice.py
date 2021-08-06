from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import random
import time



def tokenized_and_replace():
    start_time = time.time()
    while True:
        present_time = time.time()
        if present_time - start_time > 120:
            pass # TODO
        
        alice = nltk.corpus.gutenberg.raw("carroll-alice.txt")
        alice = alice.replace("\n", " ")
        alice = alice.replace("\r", " ")
        alice = alice.replace("\'", " ")
    
        alice_tokenized_sentences = sent_tokenize(alice)
    
        # get random sentence from alice_tokenized_sentences list
        random_sentence = random.choice(alice_tokenized_sentences)
    
        # print('this is the random sentence : ' + random_sentence)
    
        # tokenize the chosen sentence
        word_tokens = nltk.word_tokenize(random_sentence)
        word_tokens_lowered = [x.lower() for x in word_tokens]
    
        # get random word index, if the 'word' is not a type of punctuation it gets chosen
        random_word_index = -1 # TODO: if necessary
        while True:
            random_word_index = random.randint(0, len(word_tokens_lowered) - 1)
            if not word_tokens_lowered[random_word_index] in ".,!?':;":
                break
    
        solution_for_the_riddle = word_tokens_lowered[random_word_index]
    
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
        #print the sentence
        print(output_sentence)
        print('Can you guess the missing word?')
        print('The answer is < ' + solution_for_the_riddle + ' >')
        answer = input(">>> ")
        for sentence in range(0, 3):
            # put the cheating rule in place
            if answer.lower() == '###':
                print(f"Okay, this time I'm gonna turn a blind eye. If you're interested, "
                      f"the solution was < {solution_for_the_riddle} >.")
                return get_trainticket == True
            # if the right word was guessed you get won the riddle
            if answer.lower() == solution_for_the_riddle:
                print(f"You're right! The word was {solution_for_the_riddle}, here is your trainticket.")
                return get_trainticket == True
            if answer.lower() != solution_for_the_riddle:
                print(f"I am sorry this was not the right word.")
                get_trainticket == False


if __name__ == "__main__":
    #print_riddle_one_intro()
    tokenized_and_replace()
    #if get_train():
    #    pass
    #else:
    #    pass
    