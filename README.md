This project compares the performance of transformer models and simpler neural network models on two tasks using the New York Times article dataset. 
The first task is classification of the tone of the articles using the headline, abstract, and keywords as input features. 
The second task is regression to predict the number of comments an article will receive using the topic, tone, length, hour of the day, 
and day of the week as input features. We compare the results of transformer models and the simpler models for both tasks.

## Transformer vs Simpler NNs

! pip install -r requirements.txt

### Directory Structure
```
Deep_Learning_Project

- data
   |
    ----> cleaned_train.csv
    ----> cleaned_test.csv
    
- evaluation
    |
     ---> Classification_Comparison.ipynb
     ---> Regression_Comparison.ipynb
     
- feature_engineering
    |
     ---> tokenisation.py  

- models
    |
    ---> notebooks
        |
         ===> Classification_Transformer.ipynb
         ===> MLP_Regression.ipynb
         ===> Regression_Transformer.ipynb
         ===> RNN_Classifier.ipynb
    ----> MLP_regression_model.h5
    ----> RNN_classification_model.h5
    ----> transformer_classification_model.h5
    ----> transformer_regression_model.h5
    
- pre_processing
    ---> BERT_Sentiment_Analysis.ipynb
    ---> decrement.py
    ---> one_hot_encoding.py
    ---> publish_time.py
    ---> Regression_Data_Preprocessing.ipynb
    ---> zero_padding.py
    
README.html
README.ipynb
requirements.txt
```

## Classification
A sentiment analysis transformer model and RNN model was created. Each model finds the tone of an article based on the article's headline, abstract and key words. The BERT sentiment analysis pre-trained model was initially used to find the ground truth values for all of the data. The notebook for this is in the pre_processing folder

### Training & Validation
The training is all done in the models/notebook folder. This can be reproduced if you have the cleaned_train.csv and cleaned_test.csv files in the data folder. The best weights are chosen for each model based on the validation score during the training.

### Evaluation
The models are then compared in the evaluation folder. Both trained models are evaluated on the test data. They're performance is represented in plots.

## Regression
Another transformer model and a MLP model is created to predict the number of comments an article will get based on the article's topic, tone, length, hour of the day and day of the week.

### Training & Validation
The training and validation is done in a similar format to the classification models.

### Evaluation
Since there was no number of comments data in the provided test dataset, the training dataset was split. The pre-processing of the regression data can be found in the pre_processing/Regression_Data_Preprocessing notebook. The models were then analised similarly to the classification models.
