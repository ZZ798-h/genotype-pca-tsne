import sys
print(sys.executable)

from pysam import VariantFile   # Read VCF files
import numpy as np   # Numerical computing
from sklearn import decomposition # PCA analysis
import pandas as pd  # Data/Table manipulation

print("Packages loaded successfully")