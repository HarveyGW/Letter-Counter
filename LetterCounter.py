#Made By HarveyGW
#Take a list of letters and find how many of the picked letter there is the the array

def letterCount(lArr):
  pick = input("Enter the letter to count: ")
  pick.lower()
  count = lArr.count(pick)
  print("There are %i" % count + " " + pick + "'s")


letters = input("Enter the sentence: ")
lArr = letters
letterCount(lArr)
