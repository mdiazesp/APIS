#!/bin/bash

#Build image application

docker build -t fjcuamatzi/api_cdk_ene2024:$1 .

echo "construido"
