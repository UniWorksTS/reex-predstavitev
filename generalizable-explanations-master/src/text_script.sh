
## ancestry
for set in  "../data/questions/dev.tsv" #"../data/authors/test.tsv"  "../data/bbc/test.tsv" 
do
	for index in  "svm" #"gradient_boosting"
	do
		for subset in  200
		do
			for abs in 0
			do
				for tol in 0.01 #0.15 0.3
				do
					for exp in "shap"
					do
						for minTerms in 10
						do
							for step in 0.975
							do
								echo -e "python reex --reasoner ancestry --expression_dataset $set --classifier $index --subset_size $subset --depth_weight $tol --explanation_method $exp --min_terms $minTerms --step $step --text_input --baseline_IC"
							done
						done
					done
				done
			done
		done
	done
done









