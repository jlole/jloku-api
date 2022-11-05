# jloku-api
Go Doku - 5x5 Sudoku

### Local dev
`SCRIPT_NAME=/api gunicorn --bind 127.0.0.1:5000 --timeout 600 --reload --log-level='debug' app:app`
