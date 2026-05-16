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

with VariantFile(vcf_filename) as vcf_reader: # Open the VCF file for reading， using pysam's VariantFile which provides an interface to read VCF files
    counter = 0 # Initialize a counter to keep track of the number of records processed, useful for progress tracking and debugging
    for record in vcf_reader: # Iterate through each record (variant) in the VCF file, where 'record' is an object representing a single variant and its associated data
        counter += 1 # Increment the counter for each record processed
        if counter % 100 == 0: # Print progress every 100 records, useful for long-running processes to monitor progress
            alleles = [record.samples[x]["GT"] for x in record.samples] # Extract the genotype information (GT field) for each sample in the current record, creating a list of genotypes corresponding to each sample for this variant
            samples = [sample for sample in record.samples] # Update the list of sample names based on the current record, ensuring that we have the correct sample names corresponding to the genotype data being extracted
            genotypes.append(alleles) # Append the extracted genotype information to the 'genotypes' list, which will be used later for analysis and matrix construction
            variant_ids.append(record.id) # Append the identifier of the current variant to the 'variant_ids' list, which will be used for reference and analysis purposes
        if counter % 4943 == 0: # Print progress every 4943 records, which is approximately every 1% of the total records (494328), providing a more granular progress update for long-running processes
            print(counter) # Print the current count of records processed, useful for monitoring progress and debugging
            print(f'{round(100 * counter / 494328)}%') # Print the percentage of records processed, calculated as (counter / total_records) * 100, providing a clear indication of how much of the VCF file has been processed at this point in time
        # if counter > 1000: # Limit to first 1000 variants for testing
        #     break

with open(panel_filename) as panel_file: # Open the panel file for reading, which contains information about the samples and their population groups
    labels = {} # {sample_id: population_code} Dictionary to store the mapping of sample IDs to their corresponding population codes, which will be used for labeling and analysis
    for line in panel_file:
        line = line.strip().split('\t') # Split each line of the panel file by tab characters, which is the expected format of the panel file, to extract the relevant fields
        labels[line[0]] = line[1] # Map the sample ID (first field) to the population code (second field) in the 'labels' dictionary, creating a reference for labeling samples based on their population groups for later analysis and visualization

    