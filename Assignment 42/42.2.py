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
    Ans = math.sqrt(((p1['X']) - (p2['X'])) ** 2  + ((p1['Y']) - (p2['Y'])) **2)

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
        {'Point':'A' , 'X' : 1 , 'Y' : 2 , 'label' : 'Red',},
        {'Point':'B' , 'X' : 2 , 'Y' : 3 , 'label' : 'Red',},
        {'Point':'C' , 'X' : 3 , 'Y' : 1 , 'label' : 'Blue',},
        {'Point':'D' , 'X' : 6 , 'Y' : 5 , 'label' : 'Blue',},
        {'Point':'E' , 'X' : 6 , 'Y' : 6 , 'label' : 'Blue',},
        {'Point':'F' , 'X' : 3 , 'Y' : 4 , 'label' : 'Red',},
        {'Point':'G' , 'X' : 3 , 'Y' : 2 , 'label' : 'Red',}]

    ###########################################################################
    #                         TEST POINT                                      #
    ###########################################################################

    new_point = {'X' : X_test , 'Y' :Y_test}


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
    f"{'Point':<10}"
    f"{'Label':<10}"
    f"{'Distance':<15}"
    )

    rank = 1

    for d in nearest:
        print(
            f"{rank:<8}"
            f"{d['Point']:<10}"
            f"{d['label']:<10}"
            f"{d['Distance']:<15.3f}"
        )

        rank = rank + 1

    ###########################################################################
    #                            VOTING                                       #
    ###########################################################################
    votes = {}

    for neighbours in nearest:
        label = neighbours['label']
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
    print(f"Predicted Class  : {Name}")


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
    X_test = int(input("Enter X Coordinate : "))
    Y_test = int(input("Enter Y Coordinate : "))

    for k in range(1,6,2):
        KNNClassifier(X_test,Y_test,k)


###############################################################################
#                           PROGRAM START                                    #
###############################################################################
if __name__ == "__main__":
    main()