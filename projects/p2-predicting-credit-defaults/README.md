Practical 2: Predicting Credit Card Defaults
=

Due: 9. March (23:59)

![](https://blog.bankbazaar.com/wp-content/uploads/2016/03/Surviving-a-Credit-Card-Default.png)
##### Image from [here](https://blog.bankbazaar.com).

Overview
-

Banks and credit card clients often have a high risk in that they don't know if an indvidual will default on their credit card payment or not. Specifically, clients in Taiwan want to reduce this risk by building a model that utilizes features they have in their database about each invidual. The 25 features they have collected are:

* ID: ID of each client
* LIMIT_BAL: Amount of given credit in NT dollars (includes individual and family/supplementary credit
* SEX: Gender (1=male, 2=female)
* EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)
* MARRIAGE: Marital status (1=married, 2=single, 3=others)
* AGE: Age in years
* PAY_0: Repayment status in September, 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, ... 8=payment delay for eight months, 9=payment delay for nine months and above)
* PAY_2: Repayment status in August, 2005 (scale same as above)
* PAY_3: Repayment status in July, 2005 (scale same as above)
* PAY_4: Repayment status in June, 2005 (scale same as above)
* PAY_5: Repayment status in May, 2005 (scale same as above)
* PAY_6: Repayment status in April, 2005 (scale same as above)
* BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar)
* BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar)
* BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar)
* BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar)
* BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar)
* BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar)
* PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar)
* PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar)
* PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar)
* PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar)
* PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar)
* PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar)
* default.payment.next.month: Default payment (1=yes, 0=no)

They've hired you to build a model that can help them predict whether a patient will default on their payment based on these features.

You will turn in the assigment using the submit server. Please make sure your zip file follows the format `project_N_firstname_lastname.zip`. Where `N` is the project number (in this case 1 for the first one), `firstname` is your first name, and `lastname` is your last name. Failing to follow this will result in a 5 point deduction.

Assignment
-
Using what you've learnt in the class, build a neural network model that accomplishes this. It should output a single probability for each individual which represents their likelihood of defaulting. You can take advantage of Keras and any other preprocessing or data libraries in your code.

#### Coding (35 points):
This project is more open ended for implementation as in the real world you won't be given templates to fill your code in. We do however provide a Jupyter Notebook `Practical 2 Code.ipynb` containing a framework for implementing the code that you should follow. All of your code should be written in the Jupyter notebook.

Tne provided notebook is split into 4 different sections for each of the following tasks with each section titled "Section 1", "Section 2", etc. Make sure at the top of the section under the header, you give an explanation (minimum of 3 sentences) explaining what you did. The four sections are:

1. **Loading and processing the data**: In this section you will load the data from the file `UCI_Credit_Card.csv` and process it appropriately. You will also perform the train-test split in this section.
2. **Building the model**: In this section you will write all the code to build your model in Keras. The model should output a single number between 0 and 1 which is the probability which represents whether the individual will default or not.
3. **Training the model**: In this section you will write all the coded needed to train your model on the data from Section 0. Make sure you dont train the model on the data you will test on!
4. **Testing the model and results**: In this section you will compute the accuracy of your model on the test data from Section 0. Make sure you very clearly have a cell that outputs and prints the percentage accuracy of your model. You will also include any code used to analyze the results here.

**WARNING**: We keep have a list of all the implementations and tutorials building models for this on the web. Copying code from them is considered academic dishonesty and will result in a report to the student honor council. However, please feel free to understand the logic behind their code and emulate it yourself. If you do this, please cite any articles in the `README.md`.

#### Analysis (15 points):
1. What were the results of your model? Report any scores or figures you feel neccessary to explain your point. Solely reporting the accuracy will result in a minimal grade. We highly reccomend using figures, additional scores, and data analysis (e.g. which features are the best?).
2. How did you decide on the best architecture for your model?
3. How did you choose the parameters for your model (e.g. parameter sweep)?
4. Did you notice anything interesting about the model performance or any of the features?
5. What challenges did you face when completing this task?

#### Extra credit:
1. Use a validation set as well to visualize the training loss overtime.
2. In depth explanations and data exploration prior to building the model.

What to turn in
-

1. Your `Practical 2 Code.ipynb` Jupyter notebook file containing your code. Please make sure you run all your cells before submitting so I don't have to run them on my end.
2. A `README.md` listing any extra packages that I need to run your code. Also contains any blogs or tutorials you looked at. 
3. An `analysis.pdf` file
    - pictures are better than text
    - include your name at the top of the PDF

Hints
-

1. Follow the notebooks posted on the class webpage as a framework for how to load the data, process it, etc.
2. Library documentation is your friend.


###### Thanks to UCI for the Credit Card Dataset available <a href="https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients">here</a>.
