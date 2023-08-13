# Resume Categorization


## Objective: 

Design, implement, and train a machine learning model to automatically categorize resumes based on their domain (e.g., sales, marketing, etc.). Following this, develop a script that can be run via the command line to process a batch of resumes, categorize them, and output results to both directory structures and a CSV file.


## Environment Setup

1. Install [Anaconda](https://www.anaconda.com/download/)
2. Create a new environment with Python 3.6: `conda create -n venv python=3.6`
3. Activate the environment: `source activate venv`
4. Install other dependencies: `pip install -r requirements.txt`


## with virtualenv (if you dont have virtualenv)

1. In your Command Prompt enter:
    `pip install virtualenv`

2. Launch virtualenv : In your Command Prompt navigate to your project:(`cd your_project`) and enter:

    `virtualenv env`

3. Activate virtualenv:
    
   `source env/bin/activate`   
    `env\Scripts\activate` on Windows

4. Install other dependencies: `pip install -r requirements.txt`


## Instructions

1. Open command prompt/terminal/anaconda prompt
2. Goto the directory: `cd C:\Users\{user}\{your directory}`
3. Run script: `python script.py --input_dir cv/ --output_dir sort/`
