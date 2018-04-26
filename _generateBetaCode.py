import os, re
import betaCode, betaCodeTables

div = "############################################################\n"

def translitArabic(mainFolder):
    print("Converting Arabic into Translit: %s" % mainFolder)
    testLine = "###KEEP#THIS#LINE#TEXT#WILL#BE#GENERATED#BELOW#\n"
    listOfFiles = os.listdir(mainFolder)
    for file in listOfFiles:
        print(file)
        if file.startswith("."):
            pass
        else:
            with open(mainFolder+file, "r", encoding="utf8") as f:
                text = f.read()
                test = re.search(testLine, text)
                if test:
                    print("Transliterating %s" % file)
                    text = re.split(testLine, text)
                    textToConvert = text[0]

                    translitBetaCode = betaCode.arabicToBetaCode(textToConvert)

                    translitBC = "###TRANSLIT#BETACODE###\n\n%s" % translitBetaCode
                    translitOTO = "###TRANSLIT#ONE#TO#ONE###\n\n%s" % betaCode.betacodeToTranslit(translitBetaCode)
                    translitLOC = "###TRANSLIT#LIBRARY#OF#CONGRESS###\n\n%s" % betaCode.betacodeToLOC(translitBetaCode)
                    translitSearch = "###TRANSLIT#SEARCHEABLE###\n\n%s" % betaCode.betacodeToSearch(translitBetaCode)

                    newText = text[0] + "\n" + testLine + translitBC + translitOTO + translitLOC + translitSearch
                    newText = re.sub("\n{2,}", "\n\n", newText)

                    with open(mainFolder+file, "w", encoding="utf8") as f:
                        f.write(newText)
                else:
                    print("""File %s does not have the trigger line.\nIf you want the contents of this file converted, add the following line at the end of the file:\n\n%s\n\n""" % (file, testLine))

def translitAllFiles(mainFolder):
    print("Transliterating: %s" % mainFolder)
    testLine = "###KEEP#THIS#LINE#TEXT#WILL#BE#GENERATED#BELOW#\n"
    listOfFiles = os.listdir(mainFolder)
    for file in listOfFiles:
        print(file)
        if file.startswith("."):
            pass
        else:
            with open(mainFolder+file, "r", encoding="utf8") as f:
                text = f.read()
                test = re.search(testLine, text)
                if test:
                    print("Transliterating %s" % file)
                    text = re.split(testLine, text)
                    topLine = re.search("###BETACODE#.*\n", text[0]).group()
                    nbLine = re.search("NB:.*\n", text[0]).group()
                    textToConvert = re.sub("###BETACODE#.*\n|NB:.*\n", "", text[0])

                    translitOTO = "###TRANSLIT#ONE#TO#ONE###\n\n%s" % betaCode.betacodeToTranslit(textToConvert)
                    translitLOC = "###TRANSLIT#LIBRARY#OF#CONGRESS###\n\n%s" % betaCode.betacodeToLOC(textToConvert)
                    translitSearch = "###TRANSLIT#SEARCHEABLE###\n\n%s" % betaCode.betacodeToSearch(textToConvert)

                    newText = text[0] + "\n" + testLine + translitOTO + translitLOC + translitSearch
                    newText = re.sub("\n{2,}", "\n\n", newText)

                    with open(mainFolder+file, "w", encoding="utf8") as f:
                        f.write(newText)
                else:
                    print("""File %s does not have the trigger line.\nIf you want the contents of this file converted, add the following line at the end of the file:\n\n%s\n\n""" % (file, testLine))
            
def arabicAllFiles(mainFolder):
    print("converting to Arabic: %s" % mainFolder)
    testLine = "###KEEP#THIS#LINE#TEXT#WILL#BE#GENERATED#BELOW#\n"
    listOfFiles = os.listdir(mainFolder)
    for file in listOfFiles:
        print(file)
        if file.startswith("."):
            pass
        else:
            with open(mainFolder+file, "r", encoding="utf8") as f:
                text = f.read()
                test = re.search(testLine, text)
                if test:
                    print("converting to Arabic %s" % file)
                    text = re.split(testLine, text)
                    topLine = re.search("###BETACODE#.*\n", text[0]).group()
                    nbLine = re.search("NB:.*\n", text[0]).group()
                    textToConvert = re.sub("###BETACODE#.*\n|NB:.*\n", "", text[0])

                    translitOTO = "###TRANSLIT#ONE#TO#ONE###\n\n%s" % betaCode.betacodeToTranslit(textToConvert)
                    translitLOC = "###TRANSLIT#ARABIC#SCRIPT###\n\n%s" % betaCode.betacodeToArabic(textToConvert)

                    newText = text[0] + "\n" + testLine + translitOTO + translitLOC
                    newText = re.sub("\n{2,}", "\n\n", newText)

                    with open(mainFolder+file, "w", encoding="utf8") as f:
                        f.write(newText)
                else:
                    print("""File %s does not have the trigger line.\nIf you want the contents of this file converted, add the following line at the end of the file:\n\n%s\n\n""" % (file, testLine))

arabicAllFiles("./_to_arabic/")
translitAllFiles("./_to_translit/")
translitArabic("./_from_arabic_to_translit/")
