# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 14:09:08 2023

@author: Danny
"""

# Necessary Imports
from fastapi import FastAPI                   # The main FastAPI import
from fastapi.responses import HTMLResponse    # Used for returning HTML responses
from fastapi.staticfiles import StaticFiles   # Used for serving static files
import uvicorn                                # Used for running the app
from fastapi import Request, Form
from fastapi.responses import RedirectResponse
from urllib.request import urlopen
import json

companyName = []
industry = []
sector = []
stockPrice = []

# Configuration
app = FastAPI()                   # Specify the "app" that will run the routing
# Mount the static directory
app.mount("/public", StaticFiles(directory="public"), name="public")


# Example route: return a static HTML page
@app.get("/", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
    with open("index.html") as html:
        return HTMLResponse(content=html.read())
    
@app.get("/page", response_class=HTMLResponse)
def get_page() -> HTMLResponse:
    with open("page.html") as html:
        return HTMLResponse(content=html.read())

@app.get("/stock/{num}")
def get_stock(num:int) -> dict:
    return {"Company Name":companyName[num - 1], "Industry":industry[num -1],"Sector":sector[num-1],"Stock Price":stockPrice[num-1]}

    
    
# Example route: returns JSON
@app.post("/stock")
def post_form(request: Request, symbol1: str = Form(...), symbol2: str = Form(...), symbol3: str = Form(...)):
    # define API key
    """
    INSTANTIATE THIS VARIABLE WITH YOUR API KEY
    """
    api_key = "0bb64e6ffc7829e88424a36e3e849925"
    # create url link
    symbols = [symbol1, symbol2, symbol3]
    for symbol in symbols:
        url = 'https://financialmodelingprep.com/api/v3/profile/' + symbol + '?apikey=' + api_key
    # store the response of URL
        response = urlopen(url)
    # store the JSON response from URL
        data_json = json.loads(response.read())
    # check if empty thus invalid stock symbol
        if len(data_json) == 0:
            companyName.append(['']) 
            industry.append([''])
            sector.append(['']) 
            stockPrice.append(['']) 
            continue
        
        companyName.append(data_json[0]['companyName']) 
        industry.append(data_json[0]['industry'])
        sector.append(data_json[0]['sector']) 
        stockPrice.append(data_json[0]['price']) 
        
        
    # return json data
    return RedirectResponse(url="/page", status_code=302)


    
    
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6543)