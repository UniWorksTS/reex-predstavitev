## a python script to generate benchmark jobs.

import glob

reasoners = ['reex-lgg','hedwig']
explanation_methods = ['class-ranking','shap']
intersection_rs = [0,0.3,0.5,0.8]
subset_sizes = [500,1000,2000,5000]

for dataset in glob.glob("../data/final_versions/*"):
    for explainer in explanation_methods:
        for subset in subset_sizes:
            for reasoner in reasoners:
                if reasoner == "reex-lgg":
                    for intersection in intersection_rs:
                        cmd = "python reex --reasoner {} --subset_size {} --expression_dataset {} --explanation_method {}".format(reasoner,subset,dataset,explainer)
                        print(cmd)

                elif reasoner == "hedwig":                    
                        cmd = "python reex --reasoner {} --expression_dataset {} --explanation_method {}".format(reasoner,dataset,explainer)
                        print(cmd)
