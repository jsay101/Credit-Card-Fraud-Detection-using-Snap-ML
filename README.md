# Credit-Card-Fraud-Detection-using-Snap-ML
This project aims to detect credit card fraud using Snap ML, a machine learning library designed for scalable and efficient training of models on large datasets.
ataset
The dataset used in this project is the Credit Card Fraud Detection dataset from Kaggle (https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). It contains credit card transactions made by European cardholders over a period of two days in September 2013. The dataset is highly imbalanced, with only 0.17% of transactions being fraudulent.

Due to confidentiality reasons, most of the features in the dataset have been anonymized and are represented by the columns V1 through V28. The target variable is the Class column, which takes the value 1 in case of fraud and 0 otherwise.

Libraries Used
snapml
numpy
pandas
sklearn
matplotlib
Installation
You can install the required libraries using pip:

sh
Copy code
!pip install snapml numpy pandas sklearn matplotlib
Usage
Clone this repository:
sh
Copy code
git clone https://github.com/<username>/<repository>.git
Navigate to the project directory:
sh
Copy code
cd credit-card-fraud-detection-snapml
Run the Jupyter notebook:
sh
Copy code
jupyter notebook credit_card_fraud_detection.ipynb
Follow the instructions in the notebook to run the code and analyze the results.
Conclusion
Snap ML offers an efficient and scalable solution for training machine learning models on large datasets. In this project, we used Snap ML to train a decision tree and a support vector machine for credit card fraud detection. The results showed that Snap ML was able to achieve high accuracy and ROC-AUC scores while reducing training time compared to traditional machine learning libraries.
