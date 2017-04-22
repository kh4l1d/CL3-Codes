import string # string module is shipped with python by default

def apparentlyMaturePlagiarismChecker(text1 , text2) :
    cleanCharacters = string.letters + string.digits + "- "   # removing all punctuations and stuff other than - and space and of course letters and alphabets

    cleanString1 = filter(lambda c: c in cleanCharacters, text1)
    cleanString2 = filter(lambda c: c in cleanCharacters, text2)

    bagOfSupposedlycleanWords1 = cleanString1.split() # split() removes all kinds of white space (spaces,tabs,newlines and what not)
    bagOfSupposedlycleanWords2 = cleanString2.split()

#====================================================
# OPTIONAL - remove these common words so that Plagiarism won't be detected because of high content of these common words
# this means that the Plagiarism checker will consider all other (uncommon) words
# Example - if you don't remove these common words,then the following texts ->
# "Apsara is a good eraser"
# "Apsara is not a rubber"
# will show plagiarism (because 'is' and 'a' are matching) although the statements are very very different indeed
    if "is" in bagOfSupposedlycleanWords1 : bagOfSupposedlycleanWords1.remove("is")
    if "the" in bagOfSupposedlycleanWords1 : bagOfSupposedlycleanWords1.remove("the")
    if "a" in bagOfSupposedlycleanWords1 : bagOfSupposedlycleanWords1.remove("a")
    if "in" in bagOfSupposedlycleanWords1 : bagOfSupposedlycleanWords1.remove("in")

    if "is" in bagOfSupposedlycleanWords2 : bagOfSupposedlycleanWords2.remove("is")   # bet you didn't know 'if' could be written like this
    if "the" in bagOfSupposedlycleanWords2 : bagOfSupposedlycleanWords2.remove("the")
    if "a" in bagOfSupposedlycleanWords2 : bagOfSupposedlycleanWords2.remove("a")
    if "in" in bagOfSupposedlycleanWords2 : bagOfSupposedlycleanWords2.remove("in")
# i've just added a few word, you can add more
#======================================================
    # so essentially we'll be comparing how many words in these 2 lists will match
    # this is called bag of words checking
    kitneWordsCopyKiye = len(set(bagOfSupposedlycleanWords1) & set(bagOfSupposedlycleanWords2)) # this gets us the length of the set that is the intersection of the two sets - effectively giving us the count of common words
    similarityFlag = False
    smallerLength = 0

    if len(bagOfSupposedlycleanWords1) <= len(bagOfSupposedlycleanWords2) :
        smallerLength = len(bagOfSupposedlycleanWords1)
    else :
        smallerLength = len(bagOfSupposedlycleanWords2)

    if kitneWordsCopyKiye >= (0.5 * smallerLength) :
        similarityFlag = True

    return similarityFlag


if __name__ == "__main__":
    print("")
