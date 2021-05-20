#Currency-Converter

This is a simple project to learn more how api's request works and how to pipe commands.

## Command:
    `curl -s http://api.exchangeratesapi.io/v1/latest?access_key=fbdfe17849f010c1916de67f2ad7d1cb | jq 'del(.success)' > ./request.json ; python3 script.py `


This command makes a api request, then the json file is piped into the jq filter that deletes the success key. After that, the filtered json is saved into the request.json and the script is executed.

## Requirements:

1. Make sure you have Python 3.* on your machine.
2. Install jq -> sudo apt install jq.
3. Install prettytable -> pip install prettytable.


## How to run the script:
1. Download the project
2. Run the command on your shell
3. Enjoy!