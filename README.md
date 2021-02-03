# CAREER GUIDANCE PORTAL  

This application is built using python and supporting libraries used to help a student to decide on a suitable career path depending on the student's knowledge, behavior and interests.

## Requirements

You will need the following hardware and software specifications to run this project.

### Hardware Requirements  

System : Intel core I3 , 2.4 GHz and above.  
Ram : 8 GB  
Hard Disk : 1 TB  

### Software Requirements

Operating system : Windows 7/8/10  
Coding Language : Python 3.7 and above

## Python Libraries Required and Installation

1. PyQt5 : The user interface of the system is built using the PyQt toolkit.

```bash
pip install PyQt5
```

2. Selenium : The selenium package is used to automate web browser interaction from Python.  

```bash  
pip install -U selenium
```

3. Pandas : Python package providing fast, flexible, and expressive data structures.  

```bash
pip install pandas
```

4. Numpy : NumPy is the fundamental package for array computing with Python.  

```bash 
pip install numpy
```

5. Tweepy : An easy-to-use Python library for accessing the Twitter API.  

```bash 
pip install tweepy
```

6. Scikit-learn : Scikit-learn is an open source machine learning library that supports supervised and unsupervised learning. It also provides various tools for model fitting, data preprocessing, model selection and evaluation, and many other utilities.

```bash
pip install -U scikit-learn
```

7. Joblib : Joblib is a set of tools to provide lightweight pipelining in Python.

```bash
pip install joblib
```

8. NLTK : The Natural Language Toolkit (NLTK) is a Python package for natural language processing.  

```bash
pip install nltk
```

To download the additional packages:

```python
import nltk
nltk.download('all')
```

## Execution

* This particular project has two sections, V1.0 and V2.0.
* The section V1.0 is stored in the folder ``` Career Guidance UI ```.
* To run this section using command prompt, navigate to this particular folder and run the following commands to launch and run the GUI.

```bash
python LaunchUI.py
```

* The section V2.0 uses machine learning to predict interests of a student from his tweets.
* The code for this section is available in the folder ```Social Media Analysis```.
* To  run this section, navigate to the folder ``` Career Analysis ``` , and run the following command.

```bash
python careeranalysis.py
```

* The code under the folder ```Train_model``` is used to train the machine learning model and generate the model files and vocabulary files used in section V2.0 of the project.  
