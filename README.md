# ML Model to find Adherence Rates 💉 of Patients 🏥

## Description 📓

1. This is a Machine 💻 Learning Model to find adherence rates of patients using variance factors. (for more details please refer <b>Model Analysis</b> folder)

2. This Machine Learning model using <b>K - Means Clustering Algorithm</b> to distinguish b/w adherence groups of patients. (for <b>Elbow Plot</b> please refer <b>Initial Preprocessing and Integrate and apply model files</b> which is present in Modal Analysis folder)

## Tech Stack Used🧑‍💻

<ol >
<li> Python   </li>
<li> Flask (for Model Deployment) </li>
<li> Pandas (for Processing CSV Files) </li>
<li> PyCarret (A very famouse Machine Learning Library) </li>
<li> Heroku (Cloud Hosting Service used for Deployment)  </li>
</ol>


## Installation and Setup 🎛️

1. Install suitable version of Python (3.8.3 is recommended) along with pip.

2. Run the following commands to setup the server and to run it on your system.(make sure you are in same directory is <b>app.py</b>)

```
pip install < requirements.txt
python app.py
```


## Usage ⌨️

You need to send a POST Request at /api with a sample JSON body as shown below : 


```
{
    "key" : "rwg2nilbso05ak918xcz",
    "ENCOUNTERS" : 44, 
    "ENCOUNTER_DURATION" : 2917080,
    "DOSES" : 8, 
    "DISPENSES" : 30, 
    "Total Course Duration" : 811, 
    "PROCEDURES" : 103, 
    "Allergies + Conditions" : 14,
    "HEALTHCARE_EXPENSES + HEALTHCARE_COVERAGE" : 791178.1,
    "TOTAL_CALCULATED_COST" : 451562.01

}

```

## Deployment : 

Model has been deployed to heroku at : 

https://health-ml-model.herokuapp.com/

<br><br>
## Built by developers </>
## Built with ❤️
