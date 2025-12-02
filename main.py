from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"message":"welcome to homepage praveen sakshiga chepthunna raa lafoot "}

