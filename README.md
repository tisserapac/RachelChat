# RachelChat

- Setting up Python virtual environment.

`$ cd backend/`
`$ python3 -m venv venv`
`$ source venv/bin/activate`
`(venv) $` 
`$ pip3 install openai==0.27.0`
`$ pip3 install python-decouple==3.8 python-multipart==0.0.6 requests==2.28.2 fastapi==0.92.0`
`% pip3 install "uvicorn[standard]"`

Start FastAPI server
`$ uvicorn main:app --reload`



Front End

yarn create vite .

yarn --exact

npx tailwindcss init -p
