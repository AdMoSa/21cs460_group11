#!/usr/bin/env python
# coding: utf-8

# In[140]:


import csv
file = open("points data till gw7withplayerids.csv")
csvreader = csv.reader(file)
header = next(csvreader)

rows = []
for row in csvreader:
    rows.append(row)

file.close()
fpltarget = []
for e in range(613):
    if int(rows[e][15])>1:
        fpltarget.append(1)
    else:
        fpltarget.append(0)
        
fpldata=[]
for e in range(613):
    fpldata.append(rows[e][3:14])


from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(fpldata, fpltarget, test_size=0.3,random_state=5)


#Import svm model
from sklearn import svm

#Create a svm Classifier
clf = svm.SVC(C=1,kernel='linear') # Linear Kernel

#Train the model using the training sets
clf.fit(X_train, y_train)
print(clf.fit)
#Predict the response for test dataset
y_pred = clf.predict(X_test)
print(y_pred,y_test)
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Model Accuracy: how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# Model Precision: what percentage of positive tuples are labeled as such?
print("Precision:",metrics.precision_score(y_test, y_pred))

# Model Recall: what percentage of positive tuples are labelled as such?
print("Recall:",metrics.recall_score(y_test, y_pred))


# In[ ]:





# In[ ]:




