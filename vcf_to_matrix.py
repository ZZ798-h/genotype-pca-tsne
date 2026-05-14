import sys
print(sys.executable)

from pysam import VariantFile   # Read VCF files
import numpy as np   # Numerical computing
from sklearn import decomposition # PCA analysis
import pandas as pd  # Data/Table manipulation

print("Packages loaded successfully")

vcf_filename = "data/ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz" # Path to the VCF file containing genotype data
panel_filename = "data/phase1_integrated_calls.20101123.ALL.panel"

import os # For checking file paths and existence, operating system interactions

print(os.getcwd()) # Print the current working directory to verify where the script is being run from

print("VCF exists:", os.path.exists(vcf_filename)) # Check if the VCF file exists at the specified path

print("Panel exists:", os.path.exists(panel_filename)) # Check if the panel file exists at the specified path

genotypes = [] # List to store genotype data for each sample
samples = [] # List to store sample names
variant_ids = [] # List to store variant identifiers
