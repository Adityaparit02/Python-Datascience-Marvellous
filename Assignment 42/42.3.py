###############################################################################
#                                                                             #
#                         K N N   C L A S S I F I E R                         #
#                                                                             #
###############################################################################
# Project Name : K-Nearest Neighbors Classifier
# Algorithm    : KNN Classification
# Author       : Aditya
# Description  : Classifies a new point using Euclidean Distance
#                and Majority Voting.
###############################################################################


import math

###############################################################################
#                         EUCLIDEAN DISTANCE                                 #
###############################################################################
def EuclidianDistance(p1,p2):
    Ans = math.sqrt(((p1['Study Hours']) - (p2['Study Hours'])) ** 2  + ((p1['Attendance']) - (p2['Attendance'])) **2)

    return Ans



###############################################################################
#                           KNN CLASSIFIER                                    #
###############################################################################
def KNNClassifier(X_test,Y_test,k=3):

    border = "-"*70
    print()
    print("=" * 70)
    print("                    K N N   C L A S S I F I E R")
    print("=" * 70)
    print("Algorithm : K-Nearest Neighbors")
    print("K Value   :", k)
    print("=" * 70)


    ###########################################################################
    #                         TRAINING DATA                                   #
    ###########################################################################
    Data = [
        {'Student':'A' , 'Study Hours' : 2 , 'Attendance' : 60 , 'Result' : 'Fail',},
        {'Student':'B' , 'Study Hours' : 5 , 'Attendance' : 80 , 'Result' : 'Pass',},
        {'Student':'C' , 'Study Hours' : 6 , 'Attendance' : 85 , 'Result' : 'Pass',},
        {'Student':'D' , 'Study Hours' : 1 , 'Attendance' : 50 , 'Result' : 'Fail',},
    ]

    ###########################################################################
    #                         TEST POINT                                      #
    ###########################################################################

    new_point = {'Study Hours' : X_test , 'Attendance' :Y_test}


    ###########################################################################
    #                    DISTANCE CALCULATION                                 #
    ###########################################################################
    for d in Data:
        d['Distance'] = EuclidianDistance(d,new_point)



    ###########################################################################
    #                         SORT DISTANCES                                  #
    ###########################################################################
    sorted_data = sorted(Data,key=lambda item :item['Distance'])


    ###########################################################################
    #                      SELECT K NEAREST                                   #
    ###########################################################################
    nearest = sorted_data[:k]
    print(f"                   {k} NEAREST NEIGHBORS")
    print(border)

    print(
    f"{'Rank':<8}"
    f"{'Student':<10}"
    f"{'Result':<10}"
    f"{'Distance':<15}"
    )

    rank = 1

    for d in nearest:
        print(
            f"{rank:<8}"
            f"{d['Student']:<10}"
            f"{d['Result']:<10}"
            f"{d['Distance']:<15.3f}"
        )

        rank = rank + 1

    ###########################################################################
    #                            VOTING                                       #
    ###########################################################################
    votes = {}

    for neighbours in nearest:
        label = neighbours['Result']
        votes[label] = votes.get(label,0) +1


    ###########################################################################
    #                         VOTE COUNTING                                   #
    ###########################################################################

    iMax = 0
    Name = ""

    for d in votes:
        if (votes[d] > iMax):
            iMax = votes[d]
            Name = d


    ###########################################################################
    #                         FINAL RESULT                                    #
    ###########################################################################
    print()
    print("=" * 70)
    print("                       FINAL RESULT")
    print("=" * 70)

    print(f"Test Point       : ({X_test}, {Y_test})")
    print(f"K Value          : {k}")
    print(f"Winning Votes    : {iMax}")
    print(f"Predicted Result  : {Name}")


    print()
    print()
    print()
    print()


###############################################################################
#                              MAIN FUNCTION                                 #
###############################################################################
def main():
    border = "-"*70
    print()
    print(border)
    print("                       TEST POINT")
    print(border)
    X_test = int(input("Enter Study Hours : "))
    Y_test = int(input("Enter Attendance : "))

   
    KNNClassifier(X_test,Y_test)


###############################################################################
#                           PROGRAM START                                    #
###############################################################################
if __name__ == "__main__":
    main()