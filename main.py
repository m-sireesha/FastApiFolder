
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello sireesha, Docker & FastAPI!"}

@app.get("/greet/{name}")
def greet_user(name: str):
    """
    This endpoint takes a 'name' from the URL path and returns a personalized greeting.
    The 'name' variable is automatically treated as a string by FastAPI.
    """
    return {"message": f"Hello, {name}! Your Dockerized FastAPI is working perfectly."}

#1.cd fastapifolder
#2.docker build -t fastapi-app .

#stop executing container if it is running
#docker stop fastapi-test
#remove the container if it is stopped 
#docker rm fastapi-test
#3.docker run -d --name fastapi-test -p 8000:8000 fastapi-app
#4.see the o/p in localhost:8000/

# if every thing works fine with these 4 stepts then need to push into git repo


# to test our code before pushing into git hub we need to use
#"/Users/seshuranjitkumargunturu/My Python Projects/.venv/bin/uvicorn" main:app --host 0.0.0.0 --port 8000
# see o/p in browser
#git add .
#git commit -m "Your commit message"
#git push origin main
# (.venv) seshuranjitkumargunturu@Seshus-MBP FastApiFolder % git push --set-upstream origin main