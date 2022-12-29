#!/bin/bash
#SBATCH --cpus-per-task=8
#SBATCH --mem=35G
| grep -w exon | tr '"' '\t' | cut -f1,4,5,10,16 | sed 's/\t/_/4' | sort -k4 > tmp.bed
