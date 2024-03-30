import spacy

def main():
    nlp = spacy.load("en_core_web_sm")

    user_input = input("You: ")
    
    doc = nlp(user_input)
    for token in doc:
        print(token.text, token.pos_)


main()