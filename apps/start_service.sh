#!/bin/sh
python3 /code/service.py &
envoy -c /etc/service-envoy.yaml --service-cluster service_${SERVICE_NAME} --service-node service_${SERVICE_NAME}

