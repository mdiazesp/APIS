#!/bin/bash

#run container app

docker stop test_api01 || true

#docker run -itd --name test_api01  -p 3001:3000 --rm app:1.0

docker run -itd --name test_api01  -p 3001:3000 --rm fjcuamatzi/api_cdk_ene2024:$1



