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
