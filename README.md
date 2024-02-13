# FlavorFinderALPHA

Welcome to the FlavorFinder(ALPHA) 
-
Description: FlavorFinder is a program that is designed to predict what food the user is hungry for based on a series of (Y)es / (N)o questions

How does it work?
-
  1. The user is asked for their zipcode
  2. The user is asked how many results (images) they would like to be shown (the more images the greater the accuracy)
  3. Images are ran thought huggingface image classification model trained on various pictures of food (https://api-inference.huggingface.co/models/nateraw/food)
  4. Summary of detected food is returned from wikipedia API (https://pypi.org/project/Wikipedia-API/)
  5. Summary of food is assigned a value based on Cosine Similarity (Ex. image 1 - image 2, image 1 - image 3, etc.)
  6. Mean value of compared food is returned and graphed on a bar graph, the highest value data point is the food recommended to the user
-------------------------------------------------------------------------------------------------------
Setup
- 
FlavorFinderALPHA requires Python 3.11 to run. you can download this version of Python here (https://www.python.org/downloads/)

Run the following commands in cmd:

(clone repository)

git clone https://github.com/austinjames95/FlavorFinderALPHA.git

cd FlavorFinderALPHA

(install libraries)

pip install -r requrements.txt

-------------------------------------------------------------------------------------------------------

API Key Setup
-
Get API keys from the following and insert them into the file APIKEYS.py
  1. Image classification model - https://huggingface.co/nateraw/food
  2. Yelp Fusion - https://docs.developer.yelp.com/docs/fusion-intro
-------------------------------------------------------------------------------------------------------
Known Issues
-
TypeError: string indices must be integers
Sometimes when getting the first label, an error will be thrown on ~line 99, if this happens, just run it again until it passes. 

WIP
-

(FlavorFinder is Patent Pending)
