#! /bin/bash
docker image rm -f glucose:1.10
docker image build -t glucose:1.10 .
docker rm -f glucose_website
docker run -it --name glucose_website -p 80:5000 glucose:1.10