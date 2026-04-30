# Population Genotype Structure Analysis Using PCA and t-SNE

## Overview

This is a mini bioinformatics portfolio project using public genotype data from the 1000 Genomes Project. The goal of this project is to explore population genetic structure by parsing genotype information from a VCF file, converting genotype calls into a numeric matrix, and applying dimensionality reduction methods such as PCA and t-SNE.

This project was inspired by Maria Nattestad's bioinformatics walkthrough on PCA analysis of genotype data. I used this project to practice working with real genomics data, Python-based data processing, reproducible analysis workflows, and scientific result interpretation.

## Project Goals

The main goals of this project are to:

- Download and inspect public genotype data from the 1000 Genomes Project.
- Understand the structure of VCF files.
- Parse genotype calls using Python.
- Convert genotype data into a numeric sample-by-variant matrix.
- Merge genotype data with population metadata.
- Perform PCA and t-SNE to reduce high-dimensional genotype data.
- Visualize population genetic structure by population labels.
- Organize the analysis as a reproducible GitHub project.

## Data Source

The genotype data are from the 1000 Genomes Project.

The main input files used in this project are:

```bash
# Genotype VCF file
curl -O "https://42basepairs.com/download/s3/1000genomes/release/20110521/ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz"

# VCF index file
curl -O "https://42basepairs.com/download/s3/1000genomes/release/20110521/ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz.tbi"

# Population panel file
curl -O "https://42basepairs.com/download/s3/1000genomes/release/20110521/phase1_integrated_calls.20101123.ALL.panel"
