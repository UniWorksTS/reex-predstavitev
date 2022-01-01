import glob

## parameter space.
datasets = glob.glob("../data/final_versions/*")[0:3]
learners = ["gradient_boosting","svm"]
subset = [5000]
abss = [1]
tol = [0,0.2]
explainers = ["shap"]
minterms = [10]
steps = [0.975]
reasoners = ["ancestry","selective_staircase"]
specialization = ["true","false"]

for reasoner in reasoners:
    for dataset in datasets:
        for classifier in learners:
            for absolute in abss:
                for sss in subset:
                    for tolx in tol:
                        for explainer in explainers:
                            for mt in minterms:
                                for step in steps:
                                    for spec in specialization:
                                        cmd ="python reex --reasoner {} --expression_dataset {} --classifier {} --absolute {} --subset_size {} --intersection_ratio {} --explanation_method {} --min_terms {} --step {} --reverse_graph {}".format(reasoner,dataset,classifier,absolute,sss,tolx,explainer,mt,step,spec)
                                        print(cmd)
