---
title: Data Quality Control
category: RDM-Collect
layout: default
docs_css: markdown
---

# Introduction

Data quality is a critical pillar in any research involving complex datasets, especially in fields such as genomics and high-throughput sequencing. Maintaining high data quality ensures that downstream analyses, like differential expression analysis or clustering in single-cell studies, are reliable and reproducible. This guide provides a detailed Quality Control (QC) expert Q&A, addressing common challenges encountered during quality assessment—from RNA-seq to single-cell analysis. The guidelines, tips, and potential solutions summarized in this post are intended to help troubleshoot common issues and inform the design of robust experiments.  

### Legend

* FP = false positive result
* END = no clear solution; the issue may stem from an unsolvable or flawed experimental design  

---

## Metadata & Documentation

---

1. **Incomplete metadata records**
- **Source:** Data submission reports and sample tracking systems  
- **Possible reason(s):** Oversight during sample collection and documentation.
- **Solution/Measure:** Develop and enforce a robust metadata standard, and incorporate automated checks for missing entries.

2. **Inconsistent documentation across experiments**
- **Source:** Lab notebooks and digital records  
- **Possible reason(s):** Variations in data logging practices among team members.
- **Solution/Measure:** Standardize documentation practices and consider using electronic lab notebooks (ELNs) to improve consistency.

3. **Unclear or outdated standard operating procedures (SOPs)**
- **Source:** Internal quality audit  
- **Possible reason(s):** Infrequent updates to SOPs following technological or protocol changes.
- **Solution/Measure:** Regularly review and update SOPs, and ensure all team members have access to the latest guidelines.

---

## Pipeline Validation

---

1. **Failure in reproducibility of analysis results**
- **Source:** Repeated experimental runs and analysis logs  
- **Possible reason(s):** Untracked parameter changes or inconsistent tool versions.
- **Solution/Measure:** Document tool versions and parameters rigorously, and consider containerizing your pipeline using tools like Docker or Singularity. See the provenance guidelines for workflow developer from NFDI4Microbiota ([10.5281/zenodo.15210816](doi.org/10.5281/zenodo.15210816))

2. **Incorrect handling of batch-specific metadata**
- **Source:** Discrepancies in final analysis outputs  
- **Possible reason(s):** Misalignment of sample metadata in the analysis pipeline.
- **Solution/Measure:** Verify metadata files and cross-check sample IDs throughout the pipeline.

3. **Error propagation through multi-step processing**
- **Source:** Analysis logs and output quality assessments  
- **Possible reason(s):** Failures in early processing steps that are not adequately flagged.
- **Solution/Measure:** Implement quality checkpoints after major processing steps to catch and correct errors early.


---

## RNA-seq

---

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

### Quality Control
1. low base call quality at 3'-end
- **source**: fastqc, fastq input (sam/bam are missing Phred)
- **possible reason(s)**: general effect esp. for older data, could be hint for 3'-adapters
- **solution/measure**: check trim again
2. overall low base call quality
- **source**: fastqc, fastq input (sam/bam are missing Phred)
- **possible reason(s)**: universally very good reads + wrong Phred-type detection (FP)
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
- **possible reason(s)**: TSS reads -> start of read = start of gene (FP)
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
9. 2/more peaks in per sequence GC content (alternative scenario)
- **source**: fastqc, Illumina input
- **possible reason(s)**: other contamination, e.g. adapter dimers
- **solution/measure**: adapter dimers => trim
10. high percentage of overrepresented sequences
- **source**: fastqc, Illumina input
- **possible reason(s)**: contamination present in reads
- **solution/measure**: blast most abundant reads, can be adapter sequences => remove post hoc
11. high percentage of overrepresented sequences (alternative scenario)
- **source**: fastqc, Illumina input 
- **possible reason(s)**: overrepresented sequence present in data e.g. rRNAs (FP) can be removed and the downstream analysis can be conducted, although at a loss of sequencing power. Otherwise redo the experiment with propper rRNA depletion steps/kits. 
- **solution/measure**: use blast or similar tools to remove the rRNAs.
12. high percentage of duplicated sequences
- **source**: fastqc, Illumina input
- **possible reason(s)**: low complexity
- **solution/measure**: little starting material / heavy PCR
13. high percentage of duplicated sequences (alternative scenario)
- **source**: fastqc, Illumina input
- **possible reason(s)**: constrained library (only reads starting at TSS) (FP)
- **solution/measure**: You can use random barcoding to distinguish between biol. and tech. replicates if needed

## Contamination Checks

1. human DNA in non-human dataset or microbial contamination in plant dataset ...
- **source**: ncbi-Kraken output or alignment result to reference  
- **possible reason(s)**: cross-contamination in lab / sample mislabeling
- **solution/measure**: implement clean bench practices, include blank controls (END)

### Barcode & Multiplexing

1. high barcode collision rate  
- **source**: demultiplexing report, UMI-tools output  
- **possible reason(s)**: insufficient barcode diversity or high cell loading  
- **solution/measure**: use barcodes with higher Hamming distance, optimize loading concentration  

2. unexpected sample mixing  
- **source**: downstream clustering or PCA  
- **possible reason(s)**: barcode bleed-through or mislabeling  
- **solution/measure**: double-check index sequences and demux assignments, validate with synthetic spike-ins  

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
- **possible reason(s)**: mislabeling
- **solution/measure**: check design matrix, documentation, ...
6. no clear separation between conditions (ctrl, KO) 
- **source**: PCA, negative control study
- **possible reason(s)**: e.g. biol. and tech. replicates are mixed up
- **solution/measure**: END-RESTART

### Differential Expression Analysis (DEA)
1. dispersion-plot: gene estimation does not follow red fit
- **source**: DESeq2, negative control study
- **possible reason(s)**: model does not represent data
- **solution/measure**: Deseq is not applicable
2. dispersion-plot: high fit dispersion for high mean count
- **source**: DESeq2, negative control study
- **possible reason(s)**: low number of replication + high variability
- **solution/measure**: careful with reported DEGs
3. almost all genes are DE (differentially expressed)
- **source**: DESeq2, negative control study
- **possible reason(s)**: e.g. biol. and tech. replicates are mixed up
- **solution/measure**: END-RESTART
4. almost no gene is DE
- **source**: DESeq2, negative control study
- **possible reason(s)**: negative control study (FP)

### Visualization
1. using CPM to visualize DEGs (differentially expressed genes)
- **source**: Plot, negative control study
- **possible reason(s)**: mixed up within- and between-sample normalization
- **solution/measure**: use correct normalization
2. use raw Ratios to visualize DEGs effect size
- **source**: Plot, negative control study
- **possible reason(s)**: humans are bad with ratios (0.01 = almost 0 and 100 is just large but not the largest bar ever)
- **solution/measure**: use any log transformation (e.g. log10: 0.01 => -2, 100 => +2)

---

## Single Cell

---

### Quality Check
1. peak at left/right side in gene or reads per cell histogram or log10-cumulative-number of reads per cell id
- **source**: BD rhapsody pipeline, negative control study
- **possible reason(s)**: left=cell fragments, right=multiplets present
- **solution/measure**: remove with cut-offs
2. inflated UMI counts
- **source**: BD rhapsody pipeline, negative control study
- **possible reason(s)**: using raw UMI counts
- **solution/measure**: use DBEC/RSEC UMI counts

### Dimension Reduction
1. poor PCA/UMAP/tSNE embedding
- **source**: Dim. reduction embedding, negative control study
- **possible reason(s)**: using e.g. only one assay of count data for embedding
- **solution/measure**: for multimodal data use a WNN approach (combining both assays)
2. poor PCA/UMAP/tSNE embedding
- **source**: Dim. reduction embedding, negative control study
- **possible reason(s)**: use raw data for tSNE/UMAP
- **solution/measure**: use a significant portion of PC from the PCA as input for tSNE/UMAP
3. "The first two principle components were used to perform a tSNE" {% cite see_2017 %}
- **source**: Dim. reduction embedding, negative control study
- **possible reason(s)**: use only 2 PC from the PCA for the tSNE/UMAP projection
- **solution/measure**: use a significant portion of PC from the PCA as input for tSNE/UMAP

### Find Subpopulations
1. cluster form based for a specific batch index
- **source**: Dim. reduction embedding + clustering, negative control study
- **possible reason(s)**: batch effect
- **solution/measure**: correct for batch effect (e.g. integrate using seurat)

### Differential Expression Analysis (DEA)
1. many DEGs (differentially expressed genes)
- **source**: seurat/deseq, negative control study
- **possible reason(s)**: DEG between very small sub-populations
- **solution/measure**: use a population size cutoff or state the number
2. some genes look like dates (1-Mar,...)
- **source**: seurat/deseq, negative control study
- **possible reason(s)**: some genes can be interpreted as dates when using excel for data handling { % cite villani_2017 %}
- **solution/measure**: never ever use excel or at least make sure that cell type is not "AUTO"
