#!/usr/bin/env bash
nohup ipython notebook --profile=pyspark --port 8888 --ip=0.0.0.0 --no-browser &
