#Jonathan Kelly, Jonathan.kelly2@marist.edu
# takes 2 files, one with a sentence and one with words that need to be censored
#reprints sentence into a new file with censored words

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