# Practical 4: Identifying Duplicate Questions on Quora

Due: 6. May (23:59)

![](https://qph.fs.quoracdn.net/main-qimg-3f50dc82e91955847fbb07c169b4ff61)
##### Image from [here](https://www.quora.com/How-should-Quora-handle-duplicate-answers).

## Overview
One of the biggest problems on Quora is that many people tend to post questions that have already been asked (duplicates). This crowds the website with repeated information and also prevents a single list of answers from being created. For example, if someone asks "How do I run faster?" and another asks "How do I get faster at running?" we want to mark these as duplicates and conflate them into the same quesiton. To fix this problem, Quora believes that deep learning might be the answer. They've hired you to build a model that can predict whether two questions are duplicates or not.

## Assignment
Using what you've learnt in the class, build a LSTM model that accomplishes this. It should output 1 value which is the probability of being a duplicate question. As you can guess, this is a binary classification problem. You can take advantage of Keras and any other preprocessing or data libraries in your code.

### Downloading the Data
This project uses data provided by Kaggle that is too large to upload to GitHub. To download the data, download the `.csv` files from [here](https://www.kaggle.com/c/quora-question-pairs/data) and extract it to your project directory.
**Question Data:** https://www.kaggle.com/c/quora-question-pairs/data

You will also need the pretrained vectors for the Word2Vec model. You can download those here: https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing

### Coding (35 pts):
Building the model in this project is open ended intentionally. You can decide how you want to build your model but we strongly reccomend using a Siamese network as discussed in class. In the real world, you won't be provided a template for coding but for the sake of the class we provide a Jupyter Notebook Practical 2 Code.ipynb containing a framework for implementing the code that you should follow. All of your code should be written in the Jupyter notebook.

Tne provided notebook is split into 4 different sections for each of the following tasks with each section titled "Section 1", "Section 2", etc. Make sure at the top of the code you write, you give an explanation explaining what you did. The four sections are:
1. **Load Data:** Nothing to code.
2. **Data Processing:** This section processes all the code to be used as an input to the model. You will have to fill out the preprocessing function `clean_text()` as well as create the embedding matrix.
3. **Building the Model:** In this section you will have to build your model that can take in two inputs (both the questions) and output the probability that the questions are duplicates. Once again, I highly reccomend using a Siamese network.
4. **Training the model:** Nothing to code.

**WARNING:** We keep have a list of all the implementations and tutorials building models for this on the web. Copying code from them is considered academic dishonesty and will result in a report to the student honor council. However, please feel free to understand the logic behind their code and emulate it yourself. If you do this, please cite any articles in the README.md.

### Analysis (15 pts):
**NOTE:** Short answers (< 2 sentences) won't get very much credit.
1. What were the results of your model (on validation data)? Report any scores or figures you feel neccessary to explain your point. Solely reporting the accuracy will result in a minimal grade. We highly reccomend using figures, additional scores, and data analysis (e.g. which features are the best?).
2. How did you preprocess your text? Why did you pick each strategy when preprocessing?
3. How did you go about creating your embedding matrix?
4. Describe your model architecture. Explain how the data is propagated through it, and how you came about the architecture.
5. What challenges did you face when completing this task?


### Extra Credit
1. Train the model for at least 30 epochs and observe the results.
2. Try using a more advanced model that does more than just concatenate the two hidden representations together. Perhaps add in features such as the cosine similarity between the two sentences, their Levensthein distance, etc.

## What to turn in
You will turn in the assigment using the submit server. Please make sure your zip file follows the format `project_N_firstname_lastname.zip`. Where `N` is the project number, `firstname` is your first name, and `lastname` is your last name. Failing to follow this will result in a 5 point deduction.

1. Your `Practical 4 Code.ipynb` Jupyter notebook file containing your code. Please make sure you run all your cells before submitting so I don't have to run them on my end.
2. An `analysis.pdf` file
    - pictures are better than text
    - include your name at the top of the PDF
3. A `README.md` listing any extra packages that I need to run your code. Also contains any blogs or tutorials you looked at.


## Hints
* Follow the notebooks posted on the class webpage as a framework for how to load the data, process it, etc.
* Library documentation is your friend.

###### Thanks to Kaggle for the Quora Dataset available <a href="https://www.kaggle.com/c/quora-question-pairs/data">here</a>.
