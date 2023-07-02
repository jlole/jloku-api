# jloku-api
Go Doku - 5x5 Sudoku

### Local dev
Check `jloku-ui` README to run the whole app locally
`pip install gunicorn`
`pip install -r requirements.txt`
`MONGO_USERNAME=____ MONGO_PASSWORD=____ SCRIPT_NAME=/api gunicorn --bind 127.0.0.1:5000 --timeout 600 --reload --log-level='debug' app:app`


### VPS SETUP
`docker swarm init`
`docker run -d -p 5002:5002 --network host  -e REGISTRY_HTTP_ADDR=0.0.0.0:5002 --name registry registry:2`
