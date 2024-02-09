import wikipedia

def get_food_description(food_name):
    try:
        summary = wikipedia.summary(food_name)
        return summary
    except wikipedia.exceptions.PageError:
        return f"No information found for {food_name}"