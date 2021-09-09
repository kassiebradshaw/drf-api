# Lab 31 - Django REST Framework / Docker

*Author*: Kassie Bradshaw

[Link to my GitHub](https://github.com/kassiebradshaw/drf-api)

[Link to my tests](Music/tests.py)

## Overview

Use Django REST Framework to create an API, then "containerize" it with Docker

## Feature Tasks & Requirements

* [x] Rebuild a custom version of `Blog API` demo project from scratch
  * [x] Replace `Blog` and `Post` with your own application and model
  * [x] Your model must have at least as many fields as demo's model
  * [x] Your model must have one field that is a ForeignKey to user
  * [x] **NOTE**: You are not required to build any templates for this lab

## Features - Docker

* [x] **NOTE**: Refer to the class demo for built out `Dockerfile` and `docker-compose.yml` examples
* [x] Update `Dockerfile` and `docker-compose.yml`

## Stretch Goals

* [ ] Research using a production server vs. the built in development server
* [ ] Research using postgres instead of sqlite as database

## Implementation Notes

* [x] You'll need to run a command to conver pyproject.toml dependencies to requirements.txt
  * *`poetry export -f requirements.txt -o requirements.txt`*
* [x] If you get an `allowed host` error examine the bug details and update code as needed.
* [x] When Docker installed and docker files are ready to go then run...
  * [x] `docker-compose up`

* [x] To shut docker down enter `ctrl+c`
* You'll learn a better way soon

## User Acceptance Tests

* [x] Modify provided unit tests in demo to work for your project
