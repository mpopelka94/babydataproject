# BabyDataApp
Parents of infants have the ever-important job of ensuring their little one is nourished and cared for around the clock. When a baby's erratic sleep schedule is considered, keeping track of important baby statistics such as diaper changes and feedings becomes difficult. And when the little one inevitably gets sick, keeping track of baby’s intakes and outputs, as well as medicine administered, helps parents monitor their baby’s condition and adjust care as needed. 

Traditionally, these statistics might be documented on a notebook or notepad, but these pages can get lost, destroyed, and are hard to read at 3AM when your baby won’t sleep. BabyDataApp provides a quick and convenient web user interface that allows parents to track their little one. Paper and pen can be retired in favor of the parents’ cell phones for ease of use. BabyDataApp tracks information such as the dates and times of wet diapers, dirty diapers, medicine used, fluids/feedings ingested, and any general notes that might go with one of these aspects (super fussy at diaper change, for example).

## Installation
Running from the Docker file:
1) Download the Docker images from hub.docker.com. Two images are required:
   - The DB Docker image from "https://hub.docker.com/repository/docker/mpopelka/babydataproject
     - Here is the pull request to copy: "docker pull mpopelka/babydataproject:latest"
   - The web Docker image from https://hub.docker.com/repository/docker/mpopelka/babydataproject-web
     - Here is the pull request to copy: "docker pull mpopelka/babydataproject-web:latest".
2) Build the image on your Docker-running computer using the following command:
   - docker-compose build
3) Once it is built, run the image on your Docker-running computer using the following command:
   - docker-compose up

Running from Github (local connection):
1) Fork a copy of the application repository from the following link: https://github.com/mpopelka94/babydataproject
2) Install all dependencies as required by requirements.txt
3) Run the application using the following command: waitress-serve --listen=*:8000 BabyDataProject.wsgi.application

The application is then available at http://localhost:8000/accounts/login/.



## Deliverables
- [User/Mis-User Cases](https://github.com/mpopelka94/babydataproject/blob/main/docs/UseMisuseStories.md)
- [BabyDataApp Mockup](https://github.com/mpopelka94/babydataproject/tree/main/docs#babydataapp-mockup)
- [BabyDataApp C4 Diagrams](https://github.com/mpopelka94/babydataproject/blob/main/docs/README.md#babydataapp-c4-architecture-diagrams)

## License
The MIT License (MIT)

Copyright (c) 2024 Matthew J. Popelka

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
