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
    "No. of Allergies" : 2,
    "No. of Conditions" : 13,
    "ambulatory" : 31,
    "wellness" : 4, 
    "outpatient" : 5,
    "urgentcare" : 0,
    "emergency" : 3,
    "inpatient" : 1,
    "TOTAL_CLAIM_COST" : 5683.04,
    "DOSES" : 8 ,
    "MEDICINE_COST" : 8820.09,
    "MARITAL" : "S",
    "RACE" : "white",
    "ETHNICITY" : "nonhispanic",
    "GENDER" : "F",
    "COUNTY" : "Suffolk County" ,
    "HEALTHCARE_EXPENSES" : 779464.29, 
    "HEALTHCARE_COVERAGE" : 11713.81,
    "OPERATIONS" : 103, 
    "OPERATION_COST" : 437058.88
}
```

## Deployment : 

Model has been deployed to heroku at : 

https://health-ml-model.herokuapp.com/

<br><br>
## Built by developers </>
## Built with ❤️