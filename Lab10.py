

def main():
    fileName = input("Enter the name of the file: ")
    censoredWordsFile = input("Enter the name of the censored words file: ")
    
    censorWords = open(censoredWordsFile , "r")
    file = open(fileName , "r")
    
    cenWords = censorWords.read().split()
    uncenFile = file.read().split()
    
    for cWord in cenWords:
        for i in range(0,len(uncenFile)):
            if cWord.lower() == uncenFile[i].lower():
                uncenFile[i] = "*" * len(cWord)
                
    
    cenFile = open("censoredFile.txt", 'w+')
    
    for words in uncenFile:
        cenFile.write(words + " ")   
        
    file.close()
    censorWords.close()
    cenFile.close()
main()