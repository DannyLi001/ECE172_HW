# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Necessary Imports
from fastapi import FastAPI                   # The main FastAPI import
from fastapi.responses import HTMLResponse    # Used for returning HTML responses
import uvicorn                                # Used for running the app
                          # Used for running the app
# Configuration
app = FastAPI()               # Specify the "app" that will run the routing

# Example route: return a static HTML page
@app.get("/", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
  with open("index.html") as html:
    return HTMLResponse(content=html.read())

# Example route: returning just JSON
@app.get("/json/{name}")
def get_json(name:str) -> dict:
  return {"Hello": name}

# Running the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6543)
