## DVC example 

This project is a simple project to show the usage of DVC. Here, we will have a Sentiment classification model using distilbert LM. 
The project is built on python 3.12
## File system
<ol>
<li>sentiment_analysis.py -> This is a python file that runs predicts sentiment </li>
<li>requirements.txt -> package requirements to be used in the file. </li>
<li>classification_model/native_distilbert-base-cased.dvc -> Our classification model.</li>


## How to run program

<ol>
<li>Initialise a python environment with python 3.12.* using command below </li>
```
    python -m venv venv_dvc
```
<li>Install all dependencies using following command </li>
```
    pip install -r requirements.txt
```
<li> pull model from dvc</li>
```
    dvc pull
```
<li> run sentiment analysis</li>
```
    python sentiment_analysis.py
```
</ol>

