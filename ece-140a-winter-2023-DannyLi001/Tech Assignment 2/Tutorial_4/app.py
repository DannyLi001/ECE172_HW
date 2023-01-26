# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 14:59:54 2023

@author: Danny
"""

from fastapi import FastAPI, Request, Form
from fastapi.responses import Response
from fastapi.responses import HTMLResponse
import uvicorn
from urllib.request import urlopen
import json

app = FastAPI()


# Example route: return a HTML page
@app.get("/", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
    with open("index.html") as html:
        return HTMLResponse(content=html.read())

# Example route: returns JSON
@app.post("/stock")
def post_form(request: Request, symbol: str = Form(...)):
    # define API key
    """
    INSTANTIATE THIS VARIABLE WITH YOUR API KEY
    """
    api_key = "0bb64e6ffc7829e88424a36e3e849925"
    # create url link
    url = 'https://financialmodelingprep.com/api/v3/profile/' + symbol + '?apikey=' + api_key


    # store the response of URL
    response = urlopen(url)


    # store the JSON response from URL
    data_json = json.loads(response.read())


    # check if empty thus invalid stock symbol
    if len(data_json) == 0:
        return {}


    # return json data
    return data_json
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6543)
