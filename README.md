# Death chatbot
This is an chatbot implementation that can be connected to Skype for Business

## Project
The project is a implementation to demonstrate a desired architecture of CONVERSE components using the latest tensforflow embeddings

## How to start

Requirements - Docker

### First Step
Build core and enterprise images

```sh
cd core/business
docker build -t core/business_logic:init .
cd ..
cd core/confidence
docker build -t core/confidence_controller:init .
cd ..
cd core/configuration
docker build -t core/configuration_service:init .
cd ..
cd core/context
docker build -t core/context_manager:init .
cd ..
cd core/dialog
docker build -t core/dialog_manager:init .
cd ..
cd core/memory
docker build -t core/memory_manager:init .
cd ..
cd core/response
docker build -t core/response_manager:init .
cd ..
cd core/security
docker build -t core/security_service:init .
cd ..
cd enterprise/rasa
docker build -t enterprise/rasa_core:init .
cd ..
cd enterprise/rasa/usecase/callcenter/nlg
docker build -t enterprise/rasa_core/nlg:init .
cd ..
cd enterprise/rasa/usecase/callcenter/actions/
docker build -t enterprise/rasa_core/action_server:init .
cd ..
cd enterprise/rpa
docker build -t enterprise/rpa:init .
cd ..
cd enterprise/sap
docker build -t enterprise/sap:init .
cd ..
cd enterprise/watson
docker build -t enterprise/watson:init .
cd ..
cd ..
cd deploy/docker
docker-compose build
docker-compose up
```

### Traning
Models for Rasa-Core are not pre-trained,

To train
```sh
docker-compose up
docker exec -it enterprise/rasa_core:init bash
python -m rasa_core.train -s data/stories.md -d domain.yml -o models/dialogue --debug
```

## Run chatbot
```sh
docker exec -it enterprise/rasa_core:init bash
python -m rasa_core.run -d models/dialogue -o logs/rasa_core.log --endpoints endpoints.yml --port 5005
python -m rasa_core_sdk.endpoint --actions actions
```


#### Note
Draft subject to modifications
