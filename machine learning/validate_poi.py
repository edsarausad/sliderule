#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("/Users/Ed/apps/ud120-projects/tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn import tree

data_dict = pickle.load(open("/Users/Ed/apps/ud120-projects/final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print accuracy_score(clf.predict(features), labels)

### it's all yours from here forward!  


