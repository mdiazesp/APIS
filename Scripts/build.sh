#!/bin/bash

#Build image application

docker build -t mdiaze/api_cdk_ene2024:$1 .

echo "construido"
