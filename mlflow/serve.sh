#!/bin/bash

mlflow models serve --model-uri file://./mlruns/1/<<runid>>/artifacts/model --host 0.0.0.0 --port 5001 --no-conda
