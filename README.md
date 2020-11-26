# Scalable Marking Feedback
EXPLORE Incubate project for a Scalable-marking-feedback tool

Teachers are the real superheroes of society but due to time constraints they don't always have enough time to give valuable feedback.

Our solution? Create a scalable marking tool that can provide feedback digitally

### How?

* OCR technology to read hand-written math equations
* Mathematical Language Processing (MLP) to classify the answers
* Export feedback to google sheet

### What will the end product look like?

* Teacher sets up a test and a memo with all the possible answers for each question
* After learners completed the tests, the teacher puts all the scripts through a scanner that will scan all the scripts as one pdf file
* Teacher uploads that one pdf file and the memo as a pdf to our software
* Out comes a spreadsheet with each learner's marks and their feedback
* Teacher can choose to just print the sheet or plot graphs on the sheet

## Labeling

For the OCR technology to identify ticks on a paper we first need to label an exisiting dataset.
We did this through AWS SageMaker. 
[![What is an API]](https://youtu.be/Eeg1DEeWUjA)
