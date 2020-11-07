#!/usr/bin/env python
# coding: utf-8

# In[2]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


# In[8]:


data_remonte = pd.read_csv('Export Pipedrive (canal remontée de projet).csv',sep=";",encoding='latin-1') 
data_digital = pd.read_csv('Export Prod (canal digital).csv',sep=";",encoding='latin')
xls = pd.ExcelFile('Suivi des clients signés - 24022020-FR.xlsx')
data_suivi_RP = pd.read_excel(xls,'Canal RP')
data_suivi_digital = pd.read_excel(xls,'Canal Digital')


# In[14]:





# In[10]:


import plotly.express as px
external_stylesheets = ['https://codepen.io/anon/pen/mardKv.css']
import flask

server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,server=server)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


# In[40]:
fig5 = px.pie(data_digital, values='LicencesCount', names='OfferType', title='LicencesCount per OfferType')
fig6 = px.bar(data_digital, x='OfferLabel', y='PotentialARR',text='Name',title='Potential ARR for every OfferLabel')
fig6.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig7 = px.pie(data_digital, values='LicencesCount', names='OfferLabel', title='LicencesCount per OfferLabel')
fig8 = px.pie(data_digital, values='LicencesCount', names='Name', title='LicencesCount per Organization')
fig9 = px.line(data_suivi_digital, x="Date d'activation des licences", y="ARR Potentiel Expensya", title='ARR evolution by time')
for i in range(len(data_suivi_digital)):
    if data_suivi_digital["ARR Potentiel Expensya"][i]>200:
        fig9.add_annotation(x=data_suivi_digital["Date d'activation des licences"][i], y=data_suivi_digital["ARR Potentiel Expensya"][i],
            text=data_suivi_digital['Nom du client'][i],
            showarrow=True,
            arrowhead=1)

fig = px.timeline(data_suivi_RP, x_start="Offre - Offre créée", x_end="Offre - Date de conclusion", y="Nom du client", color="ARR Potentiel Expensya",title="Offers timeline and details")


# In[41]:


dt_group = data_suivi_RP.sort_values('ARR Potentiel Expensya').groupby('HARP - Liste des Filiales')['ARR Potentiel Expensya'].sum().sort_values()


# In[ ]:
df_new = data_suivi_RP.groupby(pd.to_datetime(data_suivi_RP['Offre - Date de conclusion'],format='"dddd, dd MMMM yyyy HH:mm').dt.month)['ARR Potentiel Expensya'].sum().sort_values()
fig4 = px.bar(data_suivi_RP,x=data_suivi_RP['Offre - Date de conclusion'].dt.month ,y='ARR Potentiel Expensya',text='Nom du client',title="ARR Potential by month") # otherwise tasks are listed from the bottom up
fig4.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig4.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)





# In[43]:
fig2 = px.pie(data_suivi_RP, values='ARR Potentiel Expensya', names='HARP - Liste des Filiales',title='ARR percentage by filliale')
fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


fig1 = px.bar(dt_group,title="ARR potential by affiliates") # otherwise tasks are listed from the bottom up
fig1.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

fig1.show()


# In[44]:


# otherwise tasks are listed from the bottom up
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig5.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig6.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig7.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig8.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig9.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


# In[45]:


app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    # All elements from the top of the page
    html.Div([
        html.H1(children='Investement:TEST DASHBOARD',style={'textAlign': 'center' ,'color': 'Blue'}),
        html.Div(children='''
            Canal RP.
        ''',style={'textAlign': 'center','color': 'Blue', 'fontSize': 18} ),

        dcc.Graph(
            id='graph1',
            figure=fig
        ),
        html.Div(children='''
         This interactive Graph represent the timeline of every assigned clients offer with the ARR potential for every offer.
         We can see that the CDR GROUP-HARP has a high ARR but in  long duration in meantime the Ax eau -Harp's ARR is lower than the others
         but the outcome will be in short time
        '''),

    ]),
    # New Div for all elements in the new 'row' of the page
    html.Div([


        dcc.Graph(
            id='graph2',
            figure=fig1
        ), 

    ]),
    html.Div([


        dcc.Graph(
            id='graph3',
            figure=fig2
        ),

    ]),
    html.Div([


        dcc.Graph(
            id='graph4',
            figure=fig4
        ),
                html.Div(children='''
            Canal Digital
        ''',style={'textAlign': 'center','color': 'Blue', 'fontSize':18  }),

    ]),

    html.Div([


        dcc.Graph(
            id='graph5',
            figure=fig5
        ),
             
           
       

    ]),
    html.Div([


        dcc.Graph(
            id='graph6',
            figure=fig6
        ),




    ]),

    html.Div([


        dcc.Graph(
            id='graph7',
            figure=fig7
        ),




    ]),
    html.Div([


        dcc.Graph(
            id='graph8',
            figure=fig8
        ),




    ]),
    html.Div([


        dcc.Graph(
            id='graph9',
            figure=fig9
        ),




    ]),




])
if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port='8000')
# In[ ]:



