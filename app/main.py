from fastapi import FastAPI


app = FastAPI()



@app.get("/") #HTTP get
def home_view():
    return {"hello": "world"}


@app.post("/") #HTTP post
def home_detail_view():
    return {"hello": "world"}