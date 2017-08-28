#!/usr/bin/env bash

# This file might be useful if we decide to deploy to heroku
#apt-get update -qy
#apt-get install -y ruby-dev
#apt-get install rubygems
gem install dpl
dpl --provider=heroku --app=spark_webapp --app-key=$HEROKU_STAGING_API_KEY
