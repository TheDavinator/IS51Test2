"""
This program will read a find the number of grades, calculate the grade average, and return the percentage of students within or above the average
First we create a int for the file path of the text
next we open the text
from the text we strip the grades and add it to a list
we use the list to get the average by dividing the sum of the list by the lenght of the list
we use the average grade score to find all the student on or above the curve
once we get our number of grades, average grade, and percent grades above average we display it
to the user using print function
"""
"""
def convert_list
path = path of text file
with open(path ,"r") as filename
    scorces = all the scores in the text file
    return list of scores

def main
counter for later
scores = covert_list to call function
avg = sum(scores list) / len (scores list)
for i in scores:
    if float(i) > avg:
        counter add 1
        %avg = counter / len(scorces)
"""

def convert_list() :
    path = "/Users/Dell/Documents/College Courses/IS-51/Test2/Final.txt"
    with open(path, "r") as filename:
        scores = [[float(i) for i in scores.strip().split(',')] for scores in filename]
        return [sum(i)/len(i) for i in scores]


def main() :
    counter = 0
    scores = convert_list()
    avg = sum(scores) / len(scores)
    for i in scores:
        if float(i) > avg:
            counter += 1
            percent_avg = counter/len(scores)
    print("The class average is:", avg)
    print("The number of students is:", len(scores))
    print("The percentage of the class above the average is:", percent_avg, "%")



main()
