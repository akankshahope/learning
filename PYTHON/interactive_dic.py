import json
from difflib import get_close_matches

dic_data = json.load(open("resources/data.json"))

def search_word(word):
    word = word.lower()
    if word in dic_data:
        return dic_data[word]
    elif len(get_close_matches(word, dic_data.keys())) > 0:
        answer = input("Did you mean %s instead? Enter Y for yes or N for No: " % get_close_matches(word, dic_data.keys())[0])
        if answer == "Y":
            return dic_data[get_close_matches(word,dic_data.keys())[0]]
        elif answer == "N":
            return "The word not found in dictionary."
        else:
            return "We didn't understand your quey, Please check again"
    else:
        return "The word doesn't exit in dictionary, Please check your word"

word = input("Enter your word you want to search : ")

result = search_word(word)

if type(result) == list:
    for item in result:
        print(item)
else:
    print(result)
