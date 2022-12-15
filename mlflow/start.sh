source ~/opt/miniconda3/etc/profile.d/conda.sh
conda activate ieee-workshop-env

mlflow server --backend-store-uri sqlite:///mlrunsdb.sqlite --default-artifact-root file://$(pwd)/mlruns
