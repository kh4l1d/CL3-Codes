import string # string module is shipped with python by default

def apparentlyMaturePlagiarismChecker(text1 , text2) :
    sanskariCharacters = string.letters + string.digits + "- "   # removing all punctuations and stuff other than - and space and of course letters and alphabets

    sanskariString1 = filter(lambda c: c in sanskariCharacters, text1)
    sanskariString2 = filter(lambda c: c in sanskariCharacters, text2)

    bagOfSupposedlyPureWords1 = sanskariString1.split() # split() removes all kinds of white space (spaces,tabs,newlines and what not)
    bagOfSupposedlyPureWords2 = sanskariString2.split()

#====================================================
# OPTIONAL - remove these common words so that Plagiarism won't be detected because of high content of these common words
# this means that the Plagiarism checker will consider all other (uncommon) words
# Example - if you don't remove these common words,then the following texts ->
# "Apsara is a good eraser"
# "Apsara is not a rubber"
# will show plagiarism (because 'is' and 'a' are matching) although the statements are very very different indeed
    if "is" in bagOfSupposedlyPureWords1 : bagOfSupposedlyPureWords1.remove("is")
    if "the" in bagOfSupposedlyPureWords1 : bagOfSupposedlyPureWords1.remove("the")
    if "a" in bagOfSupposedlyPureWords1 : bagOfSupposedlyPureWords1.remove("a")
    if "in" in bagOfSupposedlyPureWords1 : bagOfSupposedlyPureWords1.remove("in")

    if "is" in bagOfSupposedlyPureWords2 : bagOfSupposedlyPureWords2.remove("is")   # bet you didn't know 'if' could be written like this
    if "the" in bagOfSupposedlyPureWords2 : bagOfSupposedlyPureWords2.remove("the")
    if "a" in bagOfSupposedlyPureWords2 : bagOfSupposedlyPureWords2.remove("a")
    if "in" in bagOfSupposedlyPureWords2 : bagOfSupposedlyPureWords2.remove("in")
# i've just added a few word, you can add more
#======================================================
    # so essentially we'll be comparing how many words in these 2 lists will match
    # this is called bag of words checking
    kitneWordsCopyKiye = len(set(bagOfSupposedlyPureWords1) & set(bagOfSupposedlyPureWords2)) # this gets us the length of the set that is the intersection of the two sets - effectively giving us the count of common words
    similarityFlag = False
    smallerLength = 0

    if len(bagOfSupposedlyPureWords1) <= len(bagOfSupposedlyPureWords2) :
        smallerLength = len(bagOfSupposedlyPureWords1)
    else :
        smallerLength = len(bagOfSupposedlyPureWords2)

    if kitneWordsCopyKiye >= int((0.5 * smallerLength)) :
        similarityFlag = True

    return similarityFlag


if __name__ == "__main__":
    print("")
