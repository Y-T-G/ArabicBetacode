import os, re
import betaCode, betaCodeTables
import argparse
import sys

def translitArabic():
    textToConvert = sys.stdin.read()

    translitBetaCode = betaCode.arabicToBetaCode(textToConvert)
    newText = translitBetaCode
    sys.stdout.buffer.write(newText.encode('utf8'))


def translitOTO():
    textToConvert = sys.stdin.read()

    translitBetaCode = betaCode.arabicToBetaCode(textToConvert)

    translitOTO = betaCode.betacodeToTranslit(translitBetaCode)

    newText = translitOTO
    sys.stdout.buffer.write(newText.encode('utf8'))

def translitLOC():
    textToConvert = sys.stdin.read()

    translitBetaCode = betaCode.arabicToBetaCode(textToConvert)

    translitLOC = betaCode.betacodeToLOC(translitBetaCode)

    newText = translitLOC
    sys.stdout.buffer.write(newText.encode('utf8'))

def translitToSearch():
    textToConvert = sys.stdin.read()

    translitBetaCode = betaCode.arabicToBetaCode(textToConvert)

    translitSearch = betaCode.betacodeToSearch(translitBetaCode)

    newText = translitSearch
    sys.stdout.buffer.write(newText.encode('utf8'))



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