# mood_responses.py
def mood_response(mood):
    responses = {
        "happy": "That's great to hear! Keep smiling!",
        "sad": "I'm sorry to hear that. Hope things get better soon.",
        "excited": "Awesome! Excitement is contagious!",
        "angry": "Take a deep breath. It's going to be okay.",
        "bored": "Find something fun to do, like reading a book or going for a walk."
    }
    # Normalize the input to lowercase to handle case sensitivity
    mood = mood.lower()
    return responses.get(mood, "I'm not sure how to respond to that mood, but I hope you have a good day!")

if __name__ == "__main__":
    # Test the module directly
    test_moods = ["happy", "sad", "excited", "angry", "bored", "confused"]
    for mood in test_moods:
        print(f"Mood: {mood}, Response: {mood_response(mood)}")
