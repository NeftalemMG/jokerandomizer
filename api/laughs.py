import json
import random

def handler(request):
    # List of jokes
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I'm reading a book on anti-gravity. It's impossible to put down.",
        "What do you call a fake noodle? An impasta!",
        "The other jokes here are chatgpt generated so if you see this you are lucky."
    ]
    
    joke = random.choice(jokes)
    

    return {
        "statusCode": 200, 
        "body": json.dumps({"theJoke": joke})
    }