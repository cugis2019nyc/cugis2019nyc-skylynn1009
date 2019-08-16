# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 10:24:01 2019

@author: columbia
"""

import plotly

import pandas

from plotly.offline import plot

import plotly.graph_objs as go


wodf=pandas.read_excel("GISdata.xlsx",sheet_name = "womenOccupation")

womenoccupation=go.Bar(x=wodf["occupation"],y=wodf["women"])
plot([womenoccupation])

womenoccupation=go.Bar(x=wodf["occupation"],y=wodf["women"],
                       marker={"color":wodf["women"],
                               "colorscale":"Jet"})
    
plot([womenoccupation])


#cancercasespresentation
#skyr,jaelins,monserratm,danielled


cancercasesdf=pandas.read_excel("GISdata.xlsx",sheet_name="cancercases")


cancercases1=go.Bar(x=cancercasesdf["CancerType"],y=cancercasesdf["Number"])


cancercases=go.Bar(x=cancercasesdf["CancerType"], y=cancercasesdf["Number"],
                   marker={"color":cancercasesdf["Number"],
                           "colorscale":"Jet"})

plot([cancercases])

titles=go.Layout(title="CancerCasesin2018",
                xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="CancerType",
                                                                   )
    ),
    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Number",
                                                      )
    )
    )
fig=go.Figure(data=[cancercases], layout=titles)

plot(fig)