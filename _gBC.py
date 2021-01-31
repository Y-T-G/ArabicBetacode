import os, re
import betaCode, betaCodeTables
import argparse
import sys

def translitArabic():
    text = sys.stdin.read()

    textToConvert = text

    translitBetaCode = betaCode.arabicToBetaCode(textToConvert)
    newText = translitBetaCode
    sys.stdout.write(newText)


def translitOTO():
    text = sys.stdin.read()
    textToConvert = text

    translitBetaCode = betaCode.arabicToBetaCode(textToConvert)

    translitOTO = betaCode.betacodeToTranslit(translitBetaCode)

    newText = translitOTO
    sys.stdout.write(newText)

def translitLOC():
    text = sys.stdin.read()
    textToConvert = text

    translitBetaCode = betaCode.arabicToBetaCode(textToConvert)

    translitLOC = betaCode.betacodeToLOC(translitBetaCode)

    newText = translitLOC
    sys.stdout.write(newText)

def translitToSearch():
    text = sys.stdin.read()
    textToConvert = text

    translitBetaCode = betaCode.arabicToBetaCode(textToConvert)

    translitSearch = betaCode.betacodeToSearch(translitBetaCode)

    newText = translitSearch
    sys.stdout.write(newText)



parser = argparse.ArgumentParser()

parser.add_argument('--translitArabic', action='store_const', const=translitArabic)
parser.add_argument('--translitOTO', action='store_const', const=translitOTO)
parser.add_argument('--translitLOC', action='store_const', const=translitLOC)
parser.add_argument('--translitToSearch', action='store_const', const=translitToSearch)

args = parser.parse_args()

translitArabic = getattr(args, 'translitArabic')
translitOTO = getattr(args, 'translitOTO')
translitLOC = getattr(args, 'translitLOC')
translitToSearch = getattr(args, 'translitToSearch')

if(translitArabic != None):
  args.translitArabic()
  
elif(translitOTO != None):
  args.translitOTO()

elif(translitLOC != None):
  args.translitLOC()

elif(translitToSearch != None):
  args.translitToSearch()