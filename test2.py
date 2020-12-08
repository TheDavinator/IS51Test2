

def convert_list() :
    path = "/Users/Dell/Documents/College Courses/IS-51/Test2/Final.txt"
    with open(path, "r") as filename:
        scores = [[int(i) for i in scores.strip().split(',')] for scores in filename]
        return [sum(i)/len(i) for i in scores]


def main() :
    scores = convert_list()
    avg = sum(scores) / len(scores)
    print("The class average is:", avg)
    print("The number of students is:", len(scores))
    print()



main()
