newList = open("search_terms.txt").readlines()
newList = [s.rstrip('\n') for s in newList]
print(newList)
