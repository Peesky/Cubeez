fic = open("playerdata.txt", "r")
score=fic.read()
fic.close()
print(score)
fic = open("playerdata.txt", "w")
fic.close()
fic = open("playerdata.txt", "r")
score=fic.read()
fic.close()
print("score : ",score)