import spacy
import random

class CookingChatbot:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.greetings = ["Hello!", "Hi there!", "Hey!"]
        self.responses = {
            "recipe": "Sure! Here's a delicious lasagna recipe: [Recipe instructions]",
            "ingredients": "To make lasagna, you'll need: [List of ingredients]",
            "default": "I'm sorry, I'm not sure how to respond to that."
        }
    
    def generate_response(self, user_input):
        # Tokenize user input and analyze it using spaCy
        doc = self.nlp(user_input)
        
        # Determine the user's intent based on spaCy's analysis
        intent = None
        for token in doc:
            if token.text.lower() == "recipe":
                intent = "recipe"
                break
            elif token.text.lower() == "ingredients":
                intent = "ingredients"
                break
        
        # Generate a random greeting
        greeting = random.choice(self.greetings)
        
        # Generate a response based on the detected intent
        if intent in self.responses:
            return f"{greeting} {self.responses[intent]}"
        else:
            return f"{greeting} {self.responses['default']}"

# Example usage
if __name__ == "__main__":
    chatbot = CookingChatbot()
    user_input = input("You: ")
    response = chatbot.generate_response(user_input)
    print("Chatbot:", response)
