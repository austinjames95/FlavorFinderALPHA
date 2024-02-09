import requests
import json
import ast
from IPython.display import Image, display
from imageGet import download_image
from imageDetect import test, get_first_label, correctFormat
from foodVec import calculate_similarity
from getWiki import get_food_description
import matplotlib.pyplot as plt

# Yelp Fusion API endpoint
url = 'https://api.yelp.com/v3/businesses/search'

#initalize list
global imageList
imageList = []

global foodName
foodName = []

global food_description
food_description = []

global cosine_sim_description
cosine_sim_description = []

global mean_cosine
mean_cosine = []

# API key
headers = {
    'Authorization': 'Bearer ' + 'B5oRp7Uwj0EDptml5VYLowGV7B9k1Iwy9qdBOrRjpTqaHMmgqSA4Eg7UjsafKftEDeve1mnntfjxLG2SEa7_bIGH2subqvoKXhrNUgmtvUsVbtEyFYCSqfd5jMemZXYx',
}

#model classification


zipCode = str(input("What is your zipcode? "))

class inputChecker:
    def __init__(self, code):
        self.code  = code

    def check(self):
        if self.code.isdigit():
            return True
        return False

userZip = inputChecker(zipCode)
if userZip.check():
    numOutput = int(input("How many results would you like to return? "))
    


if userZip.check() == False:
    print("Please enter valid zip code")


# parameters
params = {
    'location': zipCode,  
    'categories': 'restaurants',
    'limit': numOutput,  # maximum businesses to return
}


# Send GET request
response = requests.get(url, headers=headers, params=params)

# Check the status code
if response.status_code == 200:
    # Convert the response to JSON format
    data = json.loads(response.text)

    # Print each business in the response
    for business in data['businesses']:
        print(business['name'])
        display(Image(url=business['image_url']))
        imageList.append(business['image_url'])
        isRealFood = str(input("Does this look appealing? Y/N "))
        if isRealFood.lower() == "n":
            imageList.remove(business['image_url'])
        elif isRealFood.lower() == "y":
            continue
        else:
            break
else:
    print(f'Request failed with status code: {response.status_code}')

for i in range(len(imageList)):
    currentImage = imageList[i]
    print(currentImage)
    imageName = str(i + 1) + ".jpg"
    download_image(currentImage, imageName)
    variable = test(imageName)
    line = str(variable)
    json_data_line = get_first_label(json.dumps(ast.literal_eval(line)))
    foodName.append(correctFormat(json_data_line['label']))
    food_description.append(get_food_description(foodName[i]))
    print(food_description[i])


totalVal = 0
for i in range(len(food_description)):
    for x in range(len(food_description)):
        currentVal = calculate_similarity(food_description[x], food_description[i])
        print(str(foodName[i]) + ", " + str(foodName[x]) + " " + str(currentVal))
        totalVal = currentVal + totalVal
    print("---------------" + str(i + 1) + "---------------" + " " + str(totalVal))
    mean_cosine.append(totalVal)
    totalVal = 0


def plot_bar_graph(values, foodName):
    # Generate x-axis values (assuming each value corresponds to a category)
    categories = foodName
    
    # Create the bar plot
    plt.bar(categories, values, color='skyblue')
    
    # Find the index of the maximum value
    max_index = values.index(max(values))
    
    # Highlight the bar with the highest value
    plt.bar(max_index + 1, values[max_index], color='orange')
    
    # Add labels and title
    plt.xlabel('Foods')
    plt.ylabel('Values')
    plt.title('Bar Graph based on the highest mean value')
    
    # Show the plot
    plt.show()


plot_bar_graph(mean_cosine, foodName)


        

    







    








    



    


    



    
    
