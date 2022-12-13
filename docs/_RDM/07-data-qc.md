---
title: Data Quality Control
category: RDM
layout: docs_home
docs_css: markdown
---

Qualtiy Control Expert Q&A

Legend:
* FP = false positive result
* END = no solution, this problem is unsolvable


# RNA-seq
1. high peak at low bp in the electropherogram (intensity mV per Size bp)
- **source**: documentation (PDF)
- **possible reason(s)**: contamination e.g. adapter dimers (adapter+adapter, no DNA)
- **solution/measure**: increase starting material / trim /exclude by size
2. combine replicates from multiple batches without any replicates within each batch
- **source**: conceptional
- **possible reason(s)**: it is not possible to distinguish between the biological and the technical variance -> bad design
- **solution/measure**: END
3. enrichment of wrong population (e.g. polyA-enrichment to compare to rRNAs)
- **source**: conceptional
- **possible reason(s)**: it is not possible to distinguish between the biological and the technical variance -> bad design
- **solution/measure**: exclude rRNAs

### QC
1. low base call quality at 3'-end
- **source**: fastqc, fastq input (sam/bam are missing Phred)
- **possible reason(s)**: general effect esp. for older data, could be hint for 3'-adapters
- **solution/measure**: check trim again
2. overall low base call quality
- **source**: fastqc, fastq input (sam/bam are missing Phred)
- **possible reason(s)**: universally very good reads + wrong phred-type detection (FP)
- **solution/measure**: check encoding detected by fastqc, could be a FP
3. red spots in per tile sequence quality
- **source**: fastqc, Illumina input
- **possible reason(s)**: damaged flow cell
- **solution/measure**: exclude reads from these cells, buy new flow cell
4. high per base sequence content
- **source**: fastqc, Illumina input
- **possible reason(s)**: adapter sequence still present
- **solution/measure**: trim adapters
5. at the 5' end high per base sequence content
- **source**: fastqc, Illumina input
- **possible reason(s)**: TSS reads -> start of read = start of gene = bias distr. (FP)
- **solution/measure**: -
6. C is missing in high per base sequence content
- **source**: fastqc, Illumina input
- **possible reason(s)**: sodium bisulphite treated = C->T  (FP)
7. overall high high per base sequence content
- **source**: fastqc, Illumina input
- **possible reason(s)**: contamination e.g. adapter dimers
8. 2/more peaks in per sequence GC content
- **source**: fastqc, Illumina input
- **possible reason(s)**: multiple unrelated species present
- **solution/measure**: remove contaminated species
9. 2/more peaks in per sequence GC content
- **source**: fastqc, Illumina input
- **possible reason(s)**: other contamination, e.g. adapter dimers
- **solution/measure**: adapter dimers => trim
10. high percentage of overrepresented sequences
- **source**: fastqc, Illumina input
- **possible reason(s)**: contamination present in reads
- **solution/measure**: blast most abudant reads, can be adapter sequences too
11. high percentage of overrepresented sequences
- **source**: fastqc, Illumina input
- **possible reason(s)**: overrepresented sequence present in data e.g. rRNAs (FP)
12. high percentage of duplicated sequences
- **source**: fastqc, Illumina input
- **possible reason(s)**: low complexity
- **solution/measure**: little starting material / heavy PCR
13. high percentage of duplicated sequences
- **source**: fastqc, Illumina input
- **possible reason(s)**: constrained library (only reads starting at TSS) (FP)
- **solution/measure**: You can use random barcoding to distigush between biol. and tech. replicates if needed

### Trimming
1. no reads are trimmed although adapters are present
- **source**: trim-galore, Illumina input
- **possible reason(s)**: hard coded adapter sequences, ...
- **solution/measure**: adjust parameters
2. trimmed reads although no adapters are present
- **source**: trim-galore, Illumina input
- **possible reason(s)**: false positive result of TG
- **solution/measure**: skip trim-galore

### Mapping
1. high number of unmapped reads
- **source**: Mapping tool / output, Illumina input
- **possible reason(s)**: wrong target genome/transcriptome
- **solution/measure**: -
2. high number of unmapped reads
- **source**: Mapping tool / output, Illumina input
- **possible reason(s)**: adapter sequence still present
- **solution/measure**: go back to trimming

### Post-Mapping
1. different conditions correlate very good
- **source**: correlation matrix, Illumina input
- **possible reason(s)**: low potential for DEGs present
- **solution/measure**: END
2. within replicate correlation is bad
- **source**: correlation matrix, Illumina input
- **possible reason(s)**: e.g. contamination with HVG like rRNAs
- **solution/measure**: if only a small sub-population is confounding -> remove
3. replicates do not cluster
- **source**: PCA, Illumina input
- **possible reason(s)**: e.g. biol. and tech. replicates are mixed up
- **solution/measure**: END-RESTART
4. replicates do not cluster
- **source**: PCA, negative control study
- **possible reason(s)**: negative control study (FP)
5. two experiment of 2 conditions (ctrl, KO) cluster in the wrong area
- **source**: PCA, negative control study
- **possible reason(s)**: misslabeling
- **solution/measure**: check design matrix, documentation, ...
6. no clear separation between conditions (ctrl, KO) 
- **source**: PCA, negative control study
- **possible reason(s)**: e.g. biol. and tech. replicates are mixed up
- **solution/measure**: END-RESTART

### DEA
1. dispersion-plot: gene estimation does not follow red fit
- **source**: DESeq2, negative control study
- **possible reason(s)**: model does not represent data
- **solution/measure**: Deseq is not applicable
2. dispersion-plot: high fit dispersion for high mean count
- **source**: DESeq2, negative control study
- **possible reason(s)**: low number of replication + high variability
- **solution/measure**: careful with reported DEGs
3. almost all genes are DE
- **source**: DESeq2, negative control study
- **possible reason(s)**: e.g. biol. and tech. replicates are mixed up
- **solution/measure**: END-RESTART
4. almost no gene is DE
- **source**: DESeq2, negative control study
- **possible reason(s)**: negative control study (FP)

### Visualize
1. using CPM to visualize DEGs
- **source**: Plot, negative control study
- **possible reason(s)**: mixed up within- and between-sample normalization
- **solution/measure**: use correct normalization
2. use raw Ratios to visualize DEGs effect size
- **source**: Plot, negative control study
- **possible reason(s)**: humans are bad with ratios (0.01 = almost 0 and 100 is just large but not the largest bar ever)
- **solution/measure**: use any log transformation (e.g. log10: 0.01 => -2, 100 => +2)

# Single cell

### Quality check
1. peak at left/right side in gene or reads per cell histogram or log10-cummulative-number of reads per cell id
- **source**: BD rhapsody pipeline, negative control study
- **possible reason(s)**: left=cell fragments, right=multiplets present
- **solution/measure**: remove with cut-offs
2. inflated UMI counts
- **source**: BD rhapsody pipeline, negative control study
- **possible reason(s)**: using raw UMI counts
- **solution/measure**: use DBEC/RSEC UMI counts

### Dim. reduction
1. poor PCA/UMAP/tSNE embedding
- **source**: Dim. reduction embedding, negative control study
- **possible reason(s)**: using e.g. only one assay of count data for embedding
- **solution/measure**: for multimodal data use a WNN approach (combining both assays)
2. poor PCA/UMAP/tSNE embedding
- **source**: Dim. reduction embedding, negative control study
- **possible reason(s)**: use raw data for tSNE/UMAP
- **solution/measure**: use a significant portion of PC from the PCA as input for tSNE/UMAP
3. "The first two principle components were used to perform a tSNE" (https://www.science.org/doi/full/10.1126/science.aag3009)
- **source**: Dim. reduction embedding, negative control study
- **possible reason(s)**: use only 2 PC from the PCA for the tSNE/UMAP projection
- **solution/measure**: use a significant portion of PC from the PCA as input for tSNE/UMAP

### Find subpopulations
1. cluster form based for a specific batch index
- **source**: Dim. reduction embedding + clustering, negative control study
- **possible reason(s)**: batch effect
- **solution/measure**: correct for batch effect (e.g. integrate using seurat)

### DEA
1. many DEGs
- **source**: seurat/deseq, negative control study
- **possible reason(s)**: DEG between very small sub-populations
- **solution/measure**: use a population size cutoff or state the number
2. some genes look like dates (1-Mar,...)
- **source**: seurat/deseq, negative control study
- **possible reason(s)**: some genes can be interpreted as dates when using excel for data handling (https://www.science.org/doi/10.1126/science.aah4573)
- **solution/measure**: never ever use excel or at least make sure that cell type is not "AUTO"

# Further resources

# References
