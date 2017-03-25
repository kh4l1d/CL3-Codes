def extremelySimplePlagiarismChecker(text1 , text2) :
    matches = 0
    smallerLength = 0
    if (len(text1) <= len(text2)) :
        smallerLength = len(text1)
    else :
        smallerLength = len(text2)

    i = 0
    while i < smallerLength :
        if text1[i] == text2[i] :
            matches = matches + 1
        i = i + 1

    similarityPercent = (matches/smallerLength) * 100
    return similarityPercent


if __name__ == "__main__":
    print("")
