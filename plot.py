import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json
from flask import Flask,render_template,url_for,request
import pandas as pd 
import pdfplumber
import os 
from flask import * 

app = Flask(__name__)


def create_plot():


    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    data = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)



    data1 = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON1 = json.dumps(data1, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON , graphJSON1



@app.route('/')
def index():

    bar , bar1 = create_plot()

    return render_template('result4.html', plot=bar, plot1=bar1)


if __name__ == '__main__':
    app.secret_key = 'preethi'
    app.run(debug=True)




