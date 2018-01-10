# CMSC389A: Practical Deep Learning

![](http://brandmark.io/intro/deeplearning.svg)

###### Image taken from <a href = "http://brandmark.io/intro/">here</a> 

## Course Description

“Deep Learning” systems, typified by deep neural networks, are increasingly taking over all AI tasks, ranging from language understanding, and speech and image recognition, to machine translation, planning, and even game playing and autonomous driving. As a result, expertise in deep learning is quickly transitioning into a prerequisite in many advanced academic/research settings, and a large advantage in the industrial job market.

This course provides a comprehensive, practical introduction to modern deep learning networks and their applications to AI tasks. Specifically, the course will cover basic concepts in optimization, neural networks, convolutional neural networks (CNN), and recurrent neural networks (RNN). By the end of the course, it is expected that students will have a strong familiarity with the subject and be able to design and develop deep learning models for a variety of tasks.

## Course Details

- **Course**: [CMSC389A](https://ntst.umd.edu/soc/search?courseId=cmsc389a&sectionId=&termId=201801&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on)
- **Prerequisites**: C- or better in CMSC330 and CMSC250, Proficiency in Python, Basic knowledge of Machine Learning
- **Credits**: 1
- **Seats**: 30
- **Lecture Time**: Fridays, 12:00-12:50 PM
- **Location**: CSIC 2118
- **Semester**: Spring 2018
- **Textbook**: None
- **Course Facilitators**: [Sujith Vishwajith](https://www.linkedin.com/in/sujithv28), [Sashank Thupukari](https://www.linkedin.com/in/sthupukari)
- **Faculty Advisor**: [Jordan Boyd-Graber](http://www.umiacs.umd.edu/~jbg/)
- **Syllabus Last Updated**: November 27, 2017

The course assumes that you know:

- Linear Algebra, Calculus (vectors, matrices, basic integrals)
- Probability (Bayes theorem, expectation, variance)
- Basic machine learning (linear models, regression, decision trees)
- Coding (python, numpy, sklearn)

If you're "not sure" about some of them, it's most likely okay: you'll be able to grasp the missing concepts as you go through the course.

## Textbooks
Required: None

Recommended: 
- [_Deep Learning_](http://www.deeplearningbook.org) by Ian Goodfellow
- [_Deep Learning with Python_](https://www.amazon.com/Deep-Learning-Python-Francois-Chollet/dp/1617294438/ref=as_li_ss_tl?ie=UTF8&qid=1492989997&sr=8-27&keywords=deep+learning&linkCode=sl1&tag=authordanjeff-20&linkId=8113fcf15a34ec8f224ba5ea560f4580) by Francois Chollet (Keras creator)

## Topics Covered
- Optimization
  - Linear models review (logistic regression, etc.)
  - Gradient descent
  - Stochastic gradient descent
- Neural Networks
  - Mulitlayer perceptron
  - Backpropagation
  - Gradients/Weights 
  - Learning rates and data normalization
  - Activation functions, Optimizers, Regularization
  - Dropout, Momentum, BatchNorm, etc.
- Convolutional Neural Networks
  - Motivation
  - Convolution operations
  - Pooling
  - Image classification
  - Modern CNN architectures (VGG, ResNet, etc.)
- Recurrent Neural Networks
  - Motivation
  - Vanishing/Exploding gradient problem
  - Applications to sequences (text)
  - Modern RNN architectures (LSTM, GRU, etc.)
- Tuning/Debugging Neural Networks
  - Parameter search
  - Overfitting
  - Visualizations
- Pretrained Models
  - Word2Vec, ImageNet, etc.
  - Using pretrained models for different task
- Libraries
  - Keras
  - PyTorch
  - Numpy

## Grading
Grades will be maintained on the CS Department <a href="https://grades.cs.umd.edu/">grades server</a>.

You are responsible for all material discussed in lecture and posted on the class repository, including announcements, deadlines, policies, etc.

Your final course grade will be determined according to the following percentages:

| Percentage | Title | Description |
| ------------- | -----|-------- |
| 40% | Projects  | Weekly individual projects that teach practical skills and real life applications. |
| 20% | Midterm | Examination  |
| 40% | Final Project | Final project to demonstrate mastery of all topics learned and apply knowledge to create a new application from scratch. |

Any request for reconsideration of any grading on coursework must be submitted within one week of when it is returned. No requests will be considered afterwards.

### Timeline

| Week | Topic | Assignment |
| ----|----|----- |
| 1 (1/26) | Introduction to Deep Learning + Syllabus| |
| 2 (2/2) | Review | [P1 OUT](projects/p1-logistic-regression/README.md) |
| 3 (2/9) | Optimization | |
| 4 (2/16) | Neural Networks | P1 DUE, P2 OUT |
| 5 (2/23) | Neural Networks (cont.) | |
| 6 (3/2) | Tuning and Debugging Neural Networks | |
| 7 (3/9) | Deep Learning for Images | P2 DUE, P3 OUT |
| 8 (3/16) | Deep Learning for Images (cont.) | |
| 9 (3/23) | SPRING BREAK | |
| 10 (3/30) | Deep Learning for Sequences | P3 DUE, P4 OUT |
| 11 (4/6) | Deep Learning for Sequences (cont.) | Final Project Proposals DUE |
| 12 (4/13) | EXAM | P4 DUE |
| 13 (4/20) | Pretrained Models | |
| 14 (4/27) | Review / Guest Speaker TBD | |
| 15 (5/4) | PRESENTATIONS | Final Project DUE |

The timeline is not final and can be subject to change.

## Projects
Projects must be submitted electronically following the instructions given in each project assignment. Projects may not be submitted by any other means (e.g., please do not email your projects to us). It is your responsibility to test your program and verify that it works properly before submitting. All projects are due at 11:59 PM on the day indicated on the project assignment.

Projects may be submitted up to 24 hours late for a 10% penalty. If you submit both on-time & late, your project will receive the maximum of the penalty-adjusted scores.  You may submit multiple times.

Unlike lower-level programming classes, we will not provide you with test cases (e.g., public tests) before projects are due. You will be responsible for developing your own tests and for using appropriate testing techniques. Also, we expect your projects to use proper style and documentation.

## Final Project
The final project will be an oppurtunity to apply the course material into a deep learning application that you will build from the ground up to accomplish a task of your choosing. Some example tasks could be facial recognition, predicting stock prices, disease classification, etc. Students will also be required to submit a writeup and/or 2-5 minute video highlighting how their application works. More information on the final project will be available as the course progresses.

## Outside-of-class communication with course staff
We will interact with students outside of class in primarily two ways: in-person during office hours and piazza. Email should
only be used for emergencies and not class related questions (e.g., projects).

Instructor:

Dr. Jordan Boyd-Graber - jbg@umiacs.umd.edu

TAs:

Sujith Vishwajith - svishwaj@terpmail.umd.edu

Sashank Thupukari - sthupuka@terpmail.umd.edu

## Excused Absence and Academic Accommodations
See the section titled "Attendance, Absences, or Missed Assignments" available at <a href="http://www.ugst.umd.edu/courserelatedpolicies.html">Course Related Policies</a>.

## Disability Support Accommodations

See the section titled "Accessibility" available at <a href="http://www.ugst.umd.edu/courserelatedpolicies.html">Course Related Policies</a>.


## Academic Integrity
Note that academic dishonesty includes not only cheating, fabrication, and plagiarism, but also includes helping other students commit acts of academic dishonesty by allowing them to obtain copies of your work. In short, all submitted work must be your own. Cases of academic dishonesty will be pursued to the fullest extent possible as stipulated by the <a href="http://osc.umd.edu/OSC/Default.aspx">Office of Student Conduct</a>.

It is very important for you to be aware of the consequences of cheating, fabrication, facilitation, and plagiarism. For more information on the Code of Academic Integrity or the Student Honor Council, please visit http://www.shc.umd.edu.

# Course Evaluations

If you have a suggestion for improving this class, don't hesitate to tell the instructor or TAs during the semester. At the end of the semester, please don't forget to provide your feedback using the campus-wide CourseEvalUM system. Your comments will help make this class better.

###### Thanks to the writers of <a href = "https://www.cs.umd.edu/class/fall2016/cmsc330/syllabus.shtml">this</a> syllabus and  <a href = "http://deeplearning.cs.cmu.edu">this</a> syllabus for the wording of much of this document.
