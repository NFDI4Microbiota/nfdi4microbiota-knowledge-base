---
title: Proteomics TMT labelled SP3 method
category: Experimental-Procedure-Standards-SOPs
layout: default
docs_css: markdown
---


TMT-labelled SP3 method {% cite Protein_purification_Protein_Expression_and_Purification_Core_Facility %}

Buffers:
NP40-Lysis buffer
898.5 µl PBS
80 µl 10% NP-40 in PBS
1.5 ul 1M MgCl2
20 µl 50x protease inhibitor cocktail EDTA-free

Plate wash buffer
920 µl PBS
80 µl 10% NP-40 in PBS

DTT (reducing buffer)
200 mM dithiothreitol (DTT) in 50 mM HEPES/NaOH, pH 8.5 or Milli Q (add 500 µl)

CAA (alkylating buffer)
400 mM 2-chloroacetamide (CAA) in 50 mM HEPES/NaOH pH 8.5 or Milli Q (add 500 µl)

Cell Lysis and Protein Preparation
1. Add 100 µl of ice-cold NP40-Lysis buffer to a cell pellet of 1*106 HEK293T cells and resuspend the cell pellet by pipetting up and down. 
2. Sample A: transfer 36 µl to 1.5 ml Eppendorf tube and add 1.5 µl of benzonase. Incubate the sample on ice until Sample B is prepared. 
3. Sample B: Equilibrate a 0.45 µm filter plate with 50 µl plate wash buffer. Place the filter plate on a 96well plate and spin down for 2 min at 1.200 rpm at 4 °C. Place the filter plate on a new 96well plate and transfer the remaining NP40 lysate to the equilibrated filter plate. Centrifuge (500 g, 10 min, 4°C). Transfer 36 µl of the filtrate to a 1.5 ml Eppendorf tube. Add 1.5 µl benzonase and incubate sample for 5 min on ice. 
4. Add 2 µl of 20% SDS to samples A and B and incubate both lysates for 10 min at 37°C while shaking. 
5. Add 2 µL of 200 mM DTT (10 mM final concentration) and incubate for 20 minutes at 45°C. 
6. Add 2 µL of 400 mM CAA (20 mM final concentration) and incubate for 20 minutes at 24°C. 
7. Add 1 µL of 200 mM DTT to quench the reaction.

SP3 Protein Clean-up
Always prepare 70% ethanol fresh and get also acetonitrile fresh from the stock bottle.
1. Transfer 10 µl of lysate (~10 µg of protein) to a PCR tube.
2. Add 40 µl of 50 mM HEPES to the lysate, followed by 2 µl of beads, and mix them well by pipetting.
3. Immediately add acetonitrile to obtain a final percentage of 50%, (52 µl).
4. Incubate for 8 minutes at room temperature of the magnetic rack.
5. Place on a magnetic rack and incubate for further 2 minutes at room temperature.
6. Remove and discard supernatant, on the magnet.
7. Add 200 µL of 70% ethanol and incubate for 15 seconds on a magnetic stand. Remove and discard supernatant.
8. Add 200 µL of 70% ethanol and incubate for 15 seconds on a magnetic stand. Remove and discard supernatant.
9. Add 180 µL of acetonitrile and incubate for 15 seconds on a magnetic stand. Remove and discard supernatant (all droplets) and air dry beads for 30-60 seconds.
10. For digestion, reconstitute beads in 10 µL of digestion solution (e.g. 50mM HEPES pH 8.0 + 200 ng of trypsin (1:50 enzyme to substrate ratio). It is not necessary to completely homogenize the beads, as they will be stuck to each other and excessive handling will generate bubbles. The cluster will degrade as proteins are digested.
11. Incubate for 14 hours at 37°C.
Digested peptides can be recovered from the beads by placing the tube on a magnetic rack and removing the supernatant containing them.

SP3 Peptide Recovery and Preparation for TMT
1. Vortex and spin your samples then sonicate the tubes for 5 minutes in the ultrasound bath. Resuspend
beads after digestion by vortexing and spinning shortly.
2. Place the tube on a magnetic rack and incubate for further 2 minutes at room temperature.
3. Transfer the supernatant into a new PCR tube
4. Wash the tube with the beads with 10 µl 50 mM HEPES, spin down, and place the tube again for 2 minutes on the magnet. Note: do not use any amine-containing buffer (e.g. TRIS) in this step, as amines will also react with the NHS group of TMT-labelling reagent.
5. Combine the supernatants in the new tube.
Recovered samples can be directly used for TMT labeling.

SP3 TMT-Labelling
1. Reconstitute the aliquot of TMT labeling reagent in 5 µL of acetonitrile and pipette mix.
2. Add 4 µl of one TMT label to the digestion mixture and pipette mix. Incubate for 30 min to 1 hour at room temperature.
3. Add 4 µl 5% hydroxylamine, pipette mix, and incubate for 15 minutes at room temperature.
The isobaric tag serves as a ‘barcode’ that indicates from which sample peptides derived. Therefore, you can now mix TMT labeled peptides in a 1:1 ratio or you can perform label checks on each sample separately to determine the labeling efficiency and also to compare the overall amount of the samples for later mixing.
4. Dilute sample with 40 µl Buffer A from OASIS workflow.
5. Pool all samples for TMT16 multiplexing into a new Eppendorf tube.
6. Wash PCR tube once more with 40 µl Buffer A and combine it with the Eppendorf tube.
You need to reduce the acetonitrile concentration in the sample before starting the desalting, else the sample will not be able to bind to the C18 material and you lose it.
Desalting the samples by OASIS

Buffer A
0.05% formic acid (FA) in water

Buffer B
80% acetonitrile (CAN), 0.05% FA in water

Reverse phase clean-up step of peptide mix using OASIS HLB µElution Plate, which consists of a Hydrophilic-Lipophilic Balanced reverse phase sorbent. A vacuum is applied for each step: 

Equilibrate the well of an OASIS plate:

Activation of C18 material:
1. Wash with 100 µl B
2. Wash with 100 µl B

Equilibration to enable sample binding:
3. Wash with 100 µl A
4. Wash with 100 µl A

Sample loading and binding to C18:
5. Load sample

Desalting step:
6. Wash with 100 µl A
7. Wash with 100 µl A

Sample elution & collection:
8. Place glass vial to collect eluate below OASIS well
9. Elute with 50 µl B
10. Elute with 50 µl B
Dry samples in Speedvac and reconstitute peptides in 1% formic acid supplemented with 4% acetonitrile. Samples are now ready for the injection on a mass spectrometer
