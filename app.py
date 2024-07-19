import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, Response
import uvicorn

from textSummarizer.pipeline.model_inference_pipeline import ModelInferencePipeline

app = FastAPI()


#* Redirect to docs
@app.get("/", tags=["Authentication"])
async def index():
    return RedirectResponse(url="/docs")



@app.get("/train", tags=["Training"])
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful!")

    except Exception as e:
        return Response(f"Error occurred: {e}")
    


@app.post("/predict", tags=["Inference"])
async def predict_route(text):
    try:

        obj = ModelInferencePipeline()
        text = obj.main(input_text=text)

        return text
    
    except Exception as e:
        raise e
    

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
