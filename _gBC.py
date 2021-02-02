import os, re
import betaCode, betaCodeTables
import argparse
import sys


def translitArabic():
    text = sys.stdin.read()

    if(getattr(args, 'delimited') != None):
      text = re.sub(r"(?<!\\)%(.*?)(?<!\\)%", lambda match: betaCode.arabicToBetaCode(match.group(1)), text, flags=re.DOTALL)
    
    else:
      text = betaCode.arabicToBetaCode(text)

    sys.stdout.buffer.write(text.encode('utf8'))


def translitOTO():
    text = sys.stdin.read()

    if(getattr(args, 'delimited') != None):
      text = re.sub(r"(?<!\\)%(.*?)(?<!\\)%", lambda match: betaCode.betacodeToTranslit(match.group(1)), text, flags=re.DOTALL)

    else:
      text = betaCode.betacodeToTranslit(text)

    sys.stdout.buffer.write(text.encode('utf8'))

def translitLOC():
    text = sys.stdin.read()
	
    if(getattr(args, 'delimited') != None):
      text = re.sub(r"(?<!\\)%(.*?)(?<!\\)%", lambda match: betaCode.betacodeToLOC(match.group(1)), text, flags=re.DOTALL)

    else:
      text = betaCode.betacodeToLOC(text)

    sys.stdout.buffer.write(text.encode('utf8'))

def translitToSearch():
    text = sys.stdin.read()

    if(getattr(args, 'delimited') != None):
      text = re.sub(r"(?<!\\)%(.*?)(?<!\\)%", lambda match: betaCode.betacodeToSearch(match.group(1)), text, flags=re.DOTALL)

    else:
      text = betaCode.betacodeToSearch(text)

    sys.stdout.buffer.write(text.encode('utf8'))


parser = argparse.ArgumentParser()

parser.add_argument('--translitArabic', action='store_const', const=translitArabic)
parser.add_argument('--translitOTO', action='store_const', const=translitOTO)
parser.add_argument('--translitLOC', action='store_const', const=translitLOC)
parser.add_argument('--translitToSearch', action='store_const', const=translitToSearch)
parser.add_argument('--delimited', action='store_const', const='delimited')

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