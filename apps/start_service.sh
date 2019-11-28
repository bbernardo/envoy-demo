#!/bin/sh
python3 /code/service.py &
envoy -c /etc/service-envoy.yaml -l info --service-cluster service_${SERVICE_NAME} --service-node service_${SERVICE_NAME} --log-format '[METADATA][%Y-%m-%d %T.%e][%t][%l][%n] %v'
