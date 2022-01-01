#!/bin/bash

## ancestry
for set in "../data/final_versions/Breast_A.csv" "../data/final_versions/Breast_B.csv" "../data/final_versions/DLBCL_A.csv" #"../data/final_versions/DLBCL_B.csv" "../data/final_versions/DLBCL_C.csv" "../data/final_versions/DLBCL_D.csv" "../data/final_versions/Multi_A.csv" "../data/final_versions/Multi_B.csv" "../data/final_versions/TCGA.csv"
do
	for index in "gradient_boosting" #"random_forest" "svm"
	do
		for subset in 100 2000
		do
			for abs in 1
			do
				for tol in 0.000001 0.3 0.6 #3
				do
					for exp in "class-ranking" #"shap"
					do
						for minTerms in 10
						do
							for step in 0.975
							do
								python reex --reasoner ancestry --expression_dataset $set --classifier $index --subset_size $subset --depth_weight $tol --explanation_method $exp --min_terms $minTerms --step $step --baseline_IC
							done
						done
					done
				done
			done
		done
	done
done



## selective_staircase
for set in "../data/final_versions/Breast_A.csv" "../data/final_versions/Breast_B.csv" "../data/final_versions/DLBCL_A.csv" #"../data/final_versions/DLBCL_B.csv" "../data/final_versions/DLBCL_C.csv" "../data/final_versions/DLBCL_D.csv" "../data/final_versions/Multi_A.csv" "../data/final_versions/Multi_B.csv" "../data/final_versions/TCGA.csv"
do
	for index in "gradient_boosting" #"random_forest" "svm"
	do
		for subset in 100 2000
		do
			for abs in 1
			do
				for tol in 0 0.2 0.4
				do
					for exp in "class-ranking" #"shap"
					do
						for minTerms in 10
						do
							for step in 0.975
							do
								python reex --reasoner selective_staircase --expression_dataset $set --classifier $index --subset_size $subset --intersection_ratio $tol --explanation_method $exp --min_terms $minTerms --step $step --baseline_IC
							done
						done
					done
				done
			done
		done
	done
done




## quick_ancestry
for set in "../data/final_versions/Breast_A.csv" "../data/final_versions/Breast_B.csv" "../data/final_versions/DLBCL_A.csv" "../data/final_versions/DLBCL_B.csv" "../data/final_versions/DLBCL_C.csv" "../data/final_versions/DLBCL_D.csv" "../data/final_versions/Multi_A.csv" "../data/final_versions/Multi_B.csv" "../data/final_versions/TCGA.csv"
do
	for index in "gradient_boosting" "random_forest" "svm"
	do
		for subset in 100 5000
		do
			for abs in 1
			do
				for tol in 0 0.2 0.4
				do
					for exp in "class-ranking" "shap"
					do
						for minTerms in 10
						do
							for step in 0.975
							do
								for max_iter in 1 5 20
								do
									echo -e "python reex --reasoner quick_ancestry --expression_dataset $set --classifier $index --absolute $abs --subset_size $subset --intersection_ratio $tol --explanation_method $exp --min_terms $minTerms --step $step --iterations $max_iter"
								done
							done
						done
					done
				done
			done
		done
	done
done
