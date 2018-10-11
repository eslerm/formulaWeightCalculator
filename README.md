# formulaWeightCalculator

A most-abundant isotope formula weight calulator.

## Implementation

Most-abundant isotope weight measurements from IUPAC (See IUPAC's **Atomic Weights of the Elements: Review 2000**).

Python Decimal objects are used to track and round significant figures properly. See [atomicWeightsDecimal](https://github.com/HegemanLab/atomicWeightsDecimal) for more info.

### Caution

formulaWeightCalculator expects properly named, case-sensitive, elements.
  - e.g., Copper should be labeled as `Cu`. `CU` will be calculated as a carbon (`C`) and some quantity of uranium (`U`).

## Useage

**Simple example:**
```
# formulaWeightCalculator takes tabular files (.tsv) as input
# generate example data
echo "formula\tmass\nCH4\t16\nC2H6\t30\nC2H4\t28" > example.tsv
cat example.tsv

# use the --input or -i parameter to specify the input tabular file
# use the --output or -o parameter to specify the output tabular file
python3 formulaWeightCalculator.py -i example.tsv -o results.tsv
cat results.tsv
```

**Extended, real data, example:**
```
# download test data
curl ftp://ftp.plantcyc.org/Pathways/Data_dumps/PMN13_July2018/aracyc_compounds.20180702 > aracyc.tsv

# specify column header for the formula column with the --formula or -f parameter
# if this parameter is not supplied, the first column will be assumed to contain formulas
# in the case of the header is named "Chemical_formula"
python3 formulaWeightCalculator.py -i aracyc.tsv -o results.tsv -f "Chemical_formula"
head results.tsv

# to remove duplicates use the --unique or -u flag
python3 formulaWeightCalculator.py -i aracyc.tsv -o results.tsv -f "Chemical_formula" -u
head results.tsv

# to sort formulas by their weight use the --sort or -s flag
python3 formulaWeightCalculator.py -i aracyc.tsv -o results.tsv -f "Chemical_formula" -u -s
head results.tsv
```
