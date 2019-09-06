#Day 2 lunch exercises

#exercise 1

# creates fastq file containing only first 10000 reads (40000 lines)
head -40000 ../rawdata/SRR072893.fastq > SRR072893.10k.fastq

#checks that the correct number of reads is in the file
grep "^@SRR072893" SRR072893.10k.fastq| wc -l 

#creates a fastqc of SRR072893
fastqc SRR072893.10k.fastqc

#opens the fastqc report
open SRR072893.10k_fastqc.html_

#maps the BDGP6 indexs to SRR072893.10k.fastq as a sam file
hisat2 -p 4 -x BDGP6 -U ../day2-lunch/SRR072893.10k.fastq -S ../day2-lunch/SRR072893.10k.sam

#converts the sam file to a sorted bam
samtools sort -@ 4 -O BAM SRR072893.10k.sam > SRR072893.10k.bam 

#creates a bam.bai index from the sorted bam
samtools index -@ 4 -b SRR072893.10k.bam

#creates a .gtf of the bam file with quantitation data in .ctab files
stringtie SRR072893.10k.bam -e -B -p 4 -G ../genomes/BDGP6.Ensembl.81.gtf -o SRR072893.10k.gtf

#exersise 3

#searches the file for the specified term, cuts out column three, sorts the file alphabetically, and filters out repeating lines while reporting the number of times that line is repeated
grep "SRR072893" SRR072893_map.sam_ cut -f 3 | sort | uniq -c

# same as  above except no use of grep to search for a specific term.
cut -f 3 SRR072893_map.sam | sort | uniq -c

#python script that counts the alignmnents in the designated file
import sys
f = open(sys.argv[1])
counter = 0
for i, line in enumerate(f):
   if line.startswith("@"):
       continue
   fields = line.split("\t")
   if fields[2] == "*":
       continue
   counter += 1
print (counter)

#exercise 4

the difference between each catagory is the number of flags such as NH and MD associated with them. Alignments that don't fall into a catagory due to some issue are labeled as YT or YF


