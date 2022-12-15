## Prerequisite

You need to have conda distribution installed on the machine to create setup required for this workshop. On Linux, open Terminal and on Windows, open Conda prompt to run following commands.


## Create Conda Environment

### Create using *environment.yml*.

```
cd <github-repo-home>
conda env create -f environment.yml
```

### Create using *requirements.txt*

```
cd <github-repo-home>
conda env create --name ieee-workshop-env python==3.8.13
conda activate ieee-workshop-env
pip install -r requirements.txt
```

These commands will take some time to execute as they will create a new conda environment with name *ieee-workshop-env*. Now let's register this environment as a new kernel in Jupyter notebook instance.


## Install kernel in Jupyter notebook instance

```
conda activate ieee-workshop-env
python -m ipykernel install --user --name=ieee-workshop-env
```
This command will register a new kernel in Jupyter notebook instance with name *ieee-workshop-env*.


## Start Jupyter notebook

You may want to deactivate ieee-workshop-env before running following command.

```
conda deactivate
cd <github-repo-home>/notebooks
jupyter notebook
```

If you get following error - *Jupyter command `jupyter-notebook` not found* - please run following commands:
```
pip install jupyter
jupyter notebook --notebook-dir=<github-repo-home>\notebooks
```


## Run App

```
conda activate ieee-workshop-env
cd <github-repo-home>/app
streamlit run webapp.py
```
This will start a server on port 8501 and will open webpage in the default browser. If webpage does not open automatically, open browser and go to address http://localhost:8501/

Click on 'Predict' button to verify that the app returns some number. Note that this app, by default, returns a random number.


## Start MLFlow

### Start MLFlow on Linux

Navigate to mlflow and edit *start.sh*.

```
cd <github-repo-home>/mlflow
vi start.sh
```

Update path to *conda.sh* on the first line and save the file. Then run following commands to start MLFlow.

```
chmod 755 start.sh
./start.sh
```

### Start MLFlow on Windows

Run following commands:
```
cd <github-repo-home>\mlflow
conda activate ieee-workshop-env
mlflow server --backend-store-uri sqlite:///mlrunsdb.sqlite --default-artifact-root file:///mlruns
```


## Host Model Locally

### Obtain runid

Open MLFlow Tracking Server. Navigate to experiment *Graduate Admission Predictor*. Click on *Linear Regression*, copy *Run ID* from top left corner.

Now let's host the model.

### Linux users

Navigate to mlflow and edit *serve.sh*.
Replace '\<\<runid>>' with runid of given experiment from MLFlow.

```
conda activate ieee-workshop-env
cd <github-repo-home>/mlflow
chmod 755 serve.sh
./serve.sh
```

### Windows users

#### Obtain model path
Navigate to *MLFlow Tracking Server* -> *Graduate Admission Predictor* -> *Linear Regression* and copy *Full Path*. Use this command as *model-path* in the following command.

Run following commands:
```
cd <github-repo-home>/mlflow
conda activate ieee-workshop-env
mlflow models serve --model-uri <model-path> --host 0.0.0.0 --port 5001 --no-conda
```

