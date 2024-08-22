def reverseStringWordWise(string):
    # write your code logic !!!


    lister = string.split(" ")

    string = ""

    for x in range(1,len(lister)+1):

        string+=lister[-x] + " "

    return string
