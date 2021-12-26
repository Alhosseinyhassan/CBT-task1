from urllib.request import urlretrieve
import pyopenms
from pyopenms import ElementDB, EmpiricalFormula, CoarseIsotopePatternGenerator, FineIsotopePatternGenerator, ResidueDB, \
    ModificationsDB, RibonucleotideDB, AASequence, Residue, FASTAEntry, FASTAFile  
seq = AASequence.fromString("VAKA")
seq_formula = seq.getFormula()
vakaTotalMZ=0
coarse_isotopes = seq_formula.getIsotopeDistribution( CoarseIsotopePatternGenerator(6) )
for iso in coarse_isotopes.getContainer():
    print ("Isotope", iso.getMZ(),)
    vakaTotalMZ+=iso.getMZ()
print(vakaTotalMZ)
################################                #####################################
v = ResidueDB().getResidue("V")
a = ResidueDB().getResidue("A")
k = ResidueDB().getResidue("K")
l=[v,a,k,a]
subVakaMZ=0;
for i in l:
    vf=EmpiricalFormula(v.getFormula().toString()).getIsotopeDistribution(CoarseIsotopePatternGenerator(5))
    for iso in vf.getContainer():
        subVakaMZ+=iso.getMZ()
print(subVakaMZ)
      ###########################        # constans #       #####################################################

from pyopenms.Constants import *
help(pyopenms.Constants)
print("Avogadro's number :", pyopenms.Constants.AVOGADRO)


###########################          # elements  #          #############################

DataBase = ElementDB()
DataBase.hasElement("H")
DataBase.hasElement("He")
hydrogen = DataBase.getElement("H")
print(hydrogen.getName())
print(hydrogen.getSymbol())
print(hydrogen.getMonoWeight())
print(hydrogen.getAverageWeight())
########################################################
heleim = DataBase.getElement("He")
print(heleim.getName())
print(heleim.getSymbol())
print(heleim.getMonoWeight())
print(heleim.getAverageWeight())
isotopes = heleim.getIsotopeDistribution()
print("One mole of hydrogen weighs equals =", 2 * hydrogen.getAverageWeight(), "grams")
print("One mole of 16O2 weighs equals=", 2 * hydrogen.getMonoWeight(), "grams")
