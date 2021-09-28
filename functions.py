def countWordsFromFile():
      fileName = int(input("Enter The File Name"))
      if(fileName == "text1.txt"):
          fileName == "text2.txt"

      if(fileName == "text2.txt"):
          fileName == "text1.txt"
      file = open(fileName, 'r')
      numberOfWords = 0
     
      for line in file:
            words = line.split()
            print(words)
            numberOfWords = numberOfWords + len(words)
      print("Number Of Words:")
      print(numberOfWords)

countWordsFromFile()