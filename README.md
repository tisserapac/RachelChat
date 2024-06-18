# RachelChat

- Setting up Python virtual environment.

`$ cd backend/`

`$ python3 -m venv venv`

`$ source venv/bin/activate`

`(venv) $`

`$ pip3 install openai==0.27.0`

`$ pip3 install python-decouple==3.8 python-multipart==0.0.6 requests==2.28.2 fastapi==0.92.0`

`% pip3 install "uvicorn[standard]"`

## Start FastAPI server

`$ uvicorn main:app --reload`

## Front End

`yarn create vite .`

- Copy the exact package.json file provided in thecourse. Then to install the exact package versions run,

`yarn --exact`

- Follow the instructionson the tailwind documentation to configure tailwind.

`npx tailwindcss init -p`

## ElevenLabs

- [ElevenLabs Documentation](https://link-url-here.org)
