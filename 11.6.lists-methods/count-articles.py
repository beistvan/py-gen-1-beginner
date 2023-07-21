s = input().lower().split()
print('Number of articles: ' + str(s.count('a') + s.count('an') + s.count('the')))
