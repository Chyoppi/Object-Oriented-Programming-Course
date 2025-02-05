"""Each dictionary object contains values mapped to the following keys:
"name": The name of the contestant 
"result1": the first result of the contestant (an integer between 1 and 10)
"result2": the second result of the contestant (as above)
"result3": the third result of the contestant (as above)"""
from random import randint

def smallest_average(person1: dict, person2: dict, person3: dict):
    avg1 = (person1["result1"] + person1["result2"] + person1["result3"]) / 3
    avg2 = (person2["result1"] + person2["result2"] + person2["result3"]) / 3
    avg3 = (person3["result1"] + person3["result2"] + person3["result3"]) / 3

    if avg1 < avg2 and avg1 < avg3:
        return print(f"Smallest average result: {person1["name"]}, with values {person1["result1"]}, {person1["result2"]}, {person1["result3"]}")
    elif avg2 < avg1 and avg2 < avg3:
        return print(f"Smallest average result: {person2["name"]}, with values {person1["result1"]}, {person2["result2"]}, {person2["result3"]}") 
    else:
        return print(f"Smallest average result: {person3["name"]}, with values {person3["result1"]}, {person3["result2"]}, {person3["result3"]}")
    

#Testing the function

testperson1 = {"name": "Chris", "result1": randint(1,10), "result2": randint(1,10), "result3": randint(1,10)}
testperson2 = {"name": "Jaakko", "result1": randint(1,10), "result2": randint(1,10), "result3": randint(1,10)}
testperson3 = {"name": "Markku", "result1": randint(1,10), "result2": randint(1,10), "result3": randint(1,10)}

smallest_average(testperson1, testperson2, testperson3)