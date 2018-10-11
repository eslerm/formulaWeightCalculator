#!/usr/bin/env python

import argparse
import csv
import re
from decimal import Decimal

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', required=True, help='Relative path to input file.')
parser.add_argument('--output','-o', nargs='?', type=str, required=True, help='Relative path to output file.')
parser.add_argument('--formula','-f', nargs='?', type=str, help='Formula column name.')
parser.add_argument('--unique','-u', action='store_true', help='Remove duplicates.')
parser.add_argument('--sort','-s', action='store_true', help='Sort by mass.')
args = parser.parse_args()

INPUT = getattr(args, "input")
OUTPUT = getattr(args, "output")
FORMULA_COLUMN = getattr(args, "formula")
UNIQUE = getattr(args, "unique")
SORT = getattr(args, "sort")

try:
  with open(INPUT, 'r') as f:
    database = []
    data = csv.reader(f, delimiter='\t')
    header = next(data) 
    formula_index = 0 if FORMULA_COLUMN == None else header.index(FORMULA_COLUMN)
    # Dictionary of IUPAC's monoisotopic atomic weight measurements
    # see https://github.com/HegemanLab/atomicWeightsDecimal
    elementDictionary = {"H":Decimal((0,(1,0,0,7,8,2,5,0,3,1,9),-10)),"He":Decimal((0,(4,0,0,2,6,0,3,2,4,9,7),-10)),"Li":Decimal((0,(7,0,1,6,0,0,4,1),-7)),"Be":Decimal((0,(9,0,1,2,1,8,2,2),-7)),"B":Decimal((0,(1,1,0,0,9,3,0,5,5),-7)),"C":int(12),"N":Decimal((0,(1,4,0,0,3,0,7,4,0,0,7,4),-10)),"O":Decimal((0,(1,5,9,9,4,9,1,4,6,2,2,3),-10)),"F":Decimal((0,(1,8,9,9,8,4,0,3,2,0),-8)),"Ne":Decimal((0,(1,9,9,9,2,4,4,0,1,7,6),-9)),"Na":Decimal((0,(2,2,9,8,9,7,6,9,6,6),-8)),"Mg":Decimal((0,(2,3,9,8,5,0,4,1,8,7),-8)),"Al":Decimal((0,(2,6,9,8,1,5,3,8,4,1),-8)),"Si":Decimal((0,(2,7,9,7,6,9,2,6,4,9),-8)),"P":Decimal((0,(3,0,9,7,3,7,6,1,4,9),-8)),"S":Decimal((0,(3,1,9,7,2,0,7,0,7,3),-8)),"Cl":Decimal((0,(3,4,9,6,8,8,5,2,7,1),-8)),"Ar":Decimal((0,(3,9,9,6,2,3,8,3,1,2,4),-9)),"K":Decimal((0,(3,8,9,6,3,7,0,6,9),-7)),"Ca":Decimal((0,(3,9,9,6,2,5,9,1,2),-7)),"Sc":Decimal((0,(4,4,9,5,5,9,1,0,2),-7)),"Ti":Decimal((0,(4,7,9,4,7,9,4,7,0),-7)),"V":Decimal((0,(5,0,9,4,3,9,6,3,5),-7)),"Cr":Decimal((0,(5,1,9,4,0,5,1,1,5),-7)),"Mn":Decimal((0,(5,4,9,3,8,0,4,9,3),-7)),"Fe":Decimal((0,(5,5,9,3,4,9,4,1,8),-7)),"Co":Decimal((0,(5,8,9,3,3,1,9,9,9),-7)),"Ni":Decimal((0,(5,7,9,3,5,3,4,7,7),-7)),"Cu":Decimal((0,(6,2,9,2,9,6,0,0,7),-7)),"Zn":Decimal((0,(6,3,9,2,9,1,4,6,1),-7)),"Ga":Decimal((0,(6,8,9,2,5,5,8,1),-6)),"Ge":Decimal((0,(7,3,9,2,1,1,7,8,4),-7)),"As":Decimal((0,(7,4,9,2,1,5,9,6,6),-7)),"Se":Decimal((0,(7,7,9,1,6,5,2,2,1),-7)),"Br":Decimal((0,(7,8,9,1,8,3,3,7,9),-7)),"Kr":Decimal((0,(8,3,9,1,1,5,0,8),-6)),"Rb":Decimal((0,(8,4,9,1,1,7,9,2,4),-7)),"Sr":Decimal((0,(8,7,9,0,5,6,1,6,7),-7)),"Y":Decimal((0,(8,8,9,0,5,8,4,8,5),-7)),"Zr":Decimal((0,(8,9,9,0,4,7,0,2,2),-7)),"Nb":Decimal((0,(9,2,9,0,6,3,7,6,2),-7)),"Mo":Decimal((0,(9,7,9,0,5,4,0,6,9),-7)),"Ru":Decimal((0,(1,0,1,9,0,4,3,4,8,8),-7)),"Rh":Decimal((0,(1,0,2,9,0,5,5,0,4),-6)),"Pd":Decimal((0,(1,0,5,9,0,3,4,8,4),-6)),"Ag":Decimal((0,(1,0,6,9,0,5,0,9,3),-6)),"Cd":Decimal((0,(1,1,3,9,0,3,3,5,8,6),-7)),"In":Decimal((0,(1,1,4,9,0,3,8,7,9),-6)),"Sn":Decimal((0,(1,1,9,9,0,2,1,9,8,5),-7)),"Sb":Decimal((0,(1,2,0,9,0,3,8,2,2,2),-7)),"Te":Decimal((0,(1,2,9,9,0,6,2,2,2,9),-7)),"I":Decimal((0,(1,2,6,9,0,4,4,6,8),-6)),"Xe":Decimal((0,(1,3,1,9,0,4,1,5,4,6),-7)),"Cs":Decimal((0,(1,3,2,9,0,5,4,4,7),-6)),"Ba":Decimal((0,(1,3,7,9,0,5,2,4,2),-6)),"La":Decimal((0,(1,3,8,9,0,6,3,4,9),-6)),"Ce":Decimal((0,(1,3,9,9,0,5,4,3,5),-6)),"Pr":Decimal((0,(1,4,0,9,0,7,6,4,8),-6)),"Nd":Decimal((0,(1,4,1,9,0,7,7,1,9),-6)),"Sm":Decimal((0,(1,5,1,9,1,9,7,2,9),-6)),"Eu":Decimal((0,(1,5,2,9,2,1,2,2,7),-6)),"Gd":Decimal((0,(1,5,7,9,2,4,1,0,1),-6)),"Tb":Decimal((0,(1,5,8,9,2,5,3,4,3),-6)),"Dy":Decimal((0,(1,6,3,9,2,9,1,7,1),-6)),"Ho":Decimal((0,(1,6,4,9,3,0,3,1,9),-6)),"Er":Decimal((0,(1,6,5,9,3,0,2,9,0),-6)),"Tm":Decimal((0,(1,6,8,9,3,4,2,1,1),-6)),"Yb":Decimal((0,(1,7,3,9,3,8,8,5,8),-6)),"Lu":Decimal((0,(1,7,4,9,4,0,7,6,8,2),-7)),"Hf":Decimal((0,(1,7,9,9,4,6,5,4,8,8),-7)),"Ta":Decimal((0,(1,8,0,9,4,7,9,9,6),-6)),"W":Decimal((0,(1,8,3,9,5,0,9,3,2,3),-7)),"Re":Decimal((0,(1,8,6,9,5,5,7,5,0,5),-7)),"Os":Decimal((0,(1,9,1,9,6,1,4,7,9),-6)),"Ir":Decimal((0,(1,9,2,9,6,2,9,2,3),-6)),"Pt":Decimal((0,(1,9,4,9,6,4,7,7,4),-6)),"Au":Decimal((0,(1,9,6,9,6,6,5,5,1),-6)),"Hg":Decimal((0,(2,0,1,9,7,0,6,2,5),-6)),"Tl":Decimal((0,(2,0,4,9,7,4,4,1,2),-6)),"Pb":Decimal((0,(2,0,7,9,7,6,6,3,6),-6)),"Bi":Decimal((0,(2,0,8,9,8,0,3,8,4),-6)),"Th":Decimal((0,(2,3,2,0,3,8,0,4,9,5),-7)),"Pa":Decimal((0,(2,3,1,0,3,5,8,8),-5)),"U":Decimal((0,(2,3,8,0,5,0,7,8,3,5),-7))}
    for row in data:
      # sanity check that formula index exist
      if len(row) > formula_index:
        formula = row[formula_index]
        # remove null and empty formulas
        if formula and not formula.isspace():
          # create list of atomic elements and counts
          # e.g., "CH4" becomes ["C","H","4"]
          formulaList = re.findall('[A-Z][a-z]?|[0-9]+', formula)
          # max precission in IUPAC's measurements
          significantExponent = -10
          formulaMass = Decimal((0,(0,0),significantExponent))
          i = 0;
          while i < len(formulaList):
            if formulaList[i] in elementDictionary:
              elementMass = elementDictionary[formulaList[i]]
              if formulaList[i] != "C":
                elementExponent = elementMass.as_tuple().exponent
                if elementExponent > significantExponent:
                  significantExponent = elementExponent
              # elementCount == 1
              if i+1 == len(formulaList) or formulaList[i+1].isalpha():
                formulaMass += elementMass
              else:
                elementCount = int(formulaList[i+1])
                formulaMass += elementMass * elementCount
                i+=1
            # fail softly
            else:
              print("A formula '%s' has an unknown element: '%s'. Removing formula from output." % (formula, formulaList[i]))
              formulaMass = "error"
              i = len(formulaList)
            i+=1
          if formulaMass != "error":
            # round non-significant figures
            formulaMass = formulaMass.quantize(Decimal((0,(1,0),significantExponent)))
            # store tuple
            database.append((formulaMass, formula.strip().replace(" ","")))
  if UNIQUE : database = set(database)
  if SORT : database = sorted(database)
  try:
    with open(OUTPUT, 'w') as out: 
      out.write("formula\tmass\n")
      for pair in database:
        out.write(pair[1]+'\t'+str(pair[0])+'\n')
  except ValueError:
    print('Error while writing the %s database file.' % out)
except ValueError:
  print('Error while reading the %s tabular database file.' % INPUT)
