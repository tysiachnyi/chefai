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
    
    def analyze_text(self, text):
        doc = self.nlp(text.lower())
        return doc
    
    def classify_intent(self, doc):
        for token in doc:
            if token.text == "recipe":
                return "recipe"
            elif token.text == "ingredients":
                return "ingredients"
        return "default"
    
    def generate_response(self, user_input):
        doc = self.analyze_text(user_input)
        intent = self.classify_intent(doc)
        greeting = random.choice(self.greetings)
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
