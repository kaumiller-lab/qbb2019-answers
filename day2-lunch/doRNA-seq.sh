#!/bin/bash

GENOME=../day2-morning/BDGP6
ANNOTATION=../genomes/BDGP6.Ensembl.81.gtf
THREADS=4

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
  echo "*** Processing $SAMPLE"
  cp ../rawdata/$SAMPLE.fastq .
  fastqc -t $THREADS $SAMPLE.fastq
  hisat2 -p $THREADS -x $GENOME -U $SAMPLE.fastq -S $SAMPLE.sam
  samtools sort -@ $THREADS -O BAM $SAMPLE.sam -o $SAMPLE.bam
  samtools index -@ $THREADS -b $SAMPLE.bam
  stringtie $SAMPLE.bam -e -B -p $THREADS -G $ANNOTATION -o $SAMPLE.gtf
done