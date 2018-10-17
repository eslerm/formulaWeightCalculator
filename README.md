# exactMassCalculator

An exact mass calculator for molecular formulas which uses an elements most-abundant isotope for the molecules isotopic composition.

## Implementation

Isotope abundance and atomic mass measurements from [IUPAC-CIAWW](https://www.ciaaw.org)'s **Atomic Weights of the Elements: Review 2000**.

Python Decimal objects are used to track and round significant figures properly. See [atomicWeightsDecimal](https://github.com/HegemanLab/atomicWeightsDecimal) for more info.

### Caution

exactMassCalculator expects properly named, case-sensitive, elements.
  - e.g., Copper should be labeled as `Cu`. `CU` will be calculated as a carbon (`C`) and some quantity of uranium (`U`).

## Usage

**Simple example:**
```
# exactMassCalculator takes tabular files (.tsv) as input
# generate example data
printf "formula\tapproximate_mass\n" > example.tsv
printf "CH4\t16\n" >> example.tsv
printf "C2H6\t30\n" >> example.tsv
printf "C2H4\t28\n" >> example.tsv
printf "C8H10N4O2\t194\n" >> example.tsv
cat example.tsv

# use the --input or -i parameter to specify the input tabular file
# use the --output or -o parameter to specify the output tabular file
# by default, the first column is used for formulas
python3 exactMassCalculator.py -i example.tsv -o results.tsv
cat results.tsv
```

**Extended, real data, example:**
```
# download test data
curl ftp://ftp.plantcyc.org/Pathways/Data_dumps/PMN13_July2018/aracyc_compounds.20180702 > aracyc.tsv

# specify column header for the formula column with the --formula or -f parameter
# if this parameter is not supplied, the first column will be assumed to contain formulas
# in the case of the header is named "Chemical_formula"
python3 exactMassCalculator.py -i aracyc.tsv -o results.tsv -f "Chemical_formula"
head results.tsv

# to remove duplicates use the --unique or -u flag
python3 exactMassCalculator.py -i aracyc.tsv -o results.tsv -f "Chemical_formula" -u
head results.tsv

# to sort formulas by their weight use the --sort or -s flag
python3 exactMassCalculator.py -i aracyc.tsv -o results.tsv -f "Chemical_formula" -u -s
head results.tsv
```
