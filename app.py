from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/", include_in_schema=False)
def root():
    return Response(content="OK", media_type="text/plain")

@app.get("/health")
def health():
    return {"status": "ok"}
