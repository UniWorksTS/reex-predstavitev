#!/bin/bash

## reex-lgg
for set in "../data/final_versions/Breast_A.csv" "../data/final_versions/Breast_B.csv" "../data/final_versions/DLBCL_A.csv" "../data/final_versions/DLBCL_B.csv" "../data/final_versions/DLBCL_C.csv" "../data/final_versions/DLBCL_D.csv" "../data/final_versions/Multi_A.csv" "../data/final_versions/Multi_B.csv" "../data/final_versions/TCGA.csv"
do
	python reex --reasoner selective_staircase --expression_dataset $set	
	#python reex --reasoner selective_staircase --expression_dataset $set --reverse_graph false	
done

#for set in "../data/final_versions/Breast_A.csv" "../data/final_versions/Breast_B.csv" "../data/final_versions/DLBCL_A.csv" "../data/final_versions/DLBCL_B.csv" "../data/final_versions/DLBCL_C.csv" "../data/final_versions/DLBCL_D.csv" "../data/final_versions/Multi_A.csv" "../data/final_versions/Multi_B.csv" "../data/final_versions/TCGA.csv"
#do
#	python reex --reasoner quick_ancestry --expression_dataset $set --reverse_graph false							
#done

## reex-ancestor-speed
#for set in  "../data/final_versions/Breast_B.csv" "../data/final_versions/DLBCL_A.csv" "../data/final_versions/DLBCL_B.csv" "../data/final_versions/DLBCL_C.csv" "../data/final_versions/DLBCL_D.csv" "../data/final_versions/Multi_A.csv" "../data/final_versions/Multi_B.csv" "../data/final_versions/TCGA.csv"
#do
#	python reex --reasoner quick_ancestry --expression_dataset $set>> quickAncestry.json 2>> output.err							
#done


## reex-ancestor
#for set in  "../data/final_versions/Breast_B.csv" "../data/final_versions/DLBCL_A.csv" "../data/final_versions/DLBCL_B.csv" "../data/final_versions/DLBCL_C.csv" "../data/final_versions/DLBCL_D.csv" "../data/final_versions/Multi_A.csv" "../data/final_versions/Multi_B.csv" "../data/final_versions/TCGA.csv"
#do
#	python reex --reasoner reex-ancestor --expression_dataset $set>> output.tsv 2>> output.err							
#done




