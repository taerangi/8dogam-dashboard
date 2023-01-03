# Import Library
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def main_overview() :
    fig = go.Figure()

    month = [f'{i}월' for i in range(7, 13)]
    sales = [17456, 21515, 24734, 27233, 19740, 22283]
    revenue = [12945, 15060, 16049, 18094, 17012, 19430]
    fig_1 = go.Bar(x=month, y=sales, name='sales', marker_color='rgb(55, 83, 109)')
    fig_2 = go.Bar(x=month, y=revenue, name='revenue', marker_color='#3b76e1')

    fig.add_trace(fig_1)
    fig.add_trace(fig_2)

    fig.update_layout({
        'margin': {
            't': 0,
            'b': 0,
            'l': 0,
            'r': 0
        },
        'plot_bgcolor': 'White',
        'barmode': 'group',
        'bargap': 0.5,
        'bargroupgap': 0.1,
        'legend': {
            'x': 0.85,
            'y': 1,
            'font': {'size':10}
        },
        'xaxis_tickfont_size': 10,
        'yaxis_tickfont_size': 10
    })
    fig.update_xaxes(showline=True, linewidth=1, linecolor='lightgray')
    fig.update_yaxes(showline=True, linewidth=1, linecolor='lightgray', range=[0, 40000], gridcolor='#f1f3f7')

    return fig


def main_user_1() :
    month = [f'{i}월' for i in range(7, 13)]
    user_active = [7456, 9115, 13734, 6233, 9740, 8283]
    user_new = [1203, 2410, 4302, 1492, 3406, 1023]
    customer = [4052, 8530, 2434, 2723, 6740, 2283]

    fig = go.Figure()
    # fig_1 = go.Scatter(x=month, y=user_active, line_shape='spline', fill='tozeroy', line_color='rgb(55, 83, 109)', name='active user', mode='lines') #
    # fig_2 = go.Scatter(x=month, y=customer, line_shape='spline', fill='tozeroy', line_color='rgb(26, 118, 255)', name='customer', mode='lines') #
    # fig_3 = go.Scatter(x=month, y=user_new, line_shape='spline', fill='tozeroy', line_color='skyblue', name='new user', mode='lines') #
    fig_1 = go.Scatter(x=month, y=user_active, line_shape='spline', fill='tozeroy', line_color='rgb(26, 118, 255)', name='active user', mode='lines') #rgb(55, 83, 109)
    fig_2 = go.Scatter(x=month, y=customer, line_shape='spline', fill='tozeroy', line_color='#7be0e0', name='customer', mode='lines') #rgb(26, 118, 255)
    fig_3 = go.Scatter(x=month, y=user_new, line_shape='spline', fill='tozeroy', line_color='lavender', name='new user', mode='lines') #skyblue
    fig.add_trace(fig_1)
    fig.add_trace(fig_2)
    fig.add_trace(fig_3)

    fig.update_layout({
        'margin': {
            't': 0,
            'b': 0,
            'l': 0,
            'r': 0
        },
        'plot_bgcolor': 'White',
        'legend': {
                'x': 0.85,
                'y': 1,
                'font': {'size':10}
            },
        'xaxis_tickfont_size': 10,
        'yaxis_tickfont_size': 10,
    })
    fig.update_xaxes(showline=True, linewidth=1, linecolor='lightgray')
    fig.update_yaxes(showline=True, linewidth=1, linecolor='lightgray', range=[0, 20000], gridcolor='#f1f3f7')

    return fig


def main_user_2() :
    center = '40,302 user'
    pie_1_1 = 'active user'
    pie_1_2 = 'inactive user'
    pie_2 = 'customer'

    fig_1 = go.Sunburst(
        labels=[center, pie_1_1, pie_1_2, pie_2],
        parents=[""   , center , center , pie_1_1],
        branchvalues="total",
        values=[100, 60, 40, 30],
        insidetextorientation = 'auto', # auto, horizontal, radial, tangential
        marker = {
            "line": {
                "width": 3.5, 
                'color':'white'
            },
            "colors": ['white', 'rgb(156, 185, 251)', 'pink', 'rgb(152, 203, 237)']
        },
        sort=False,
        rotation=90
    )

    fig = go.Figure()
    fig.add_trace(fig_1)

    fig.update_layout({
        'margin': {
            't': 0,
            'b': 0,
            'l': 0,
            'r': 0
        },
        'font': {
            'size': 10
        },
        'paper_bgcolor': 'rgba(0,0,0,0)',
        'plot_bgcolor': 'rgba(0,0,0,0)'
    })

    fig.update_traces(
    textinfo="label+percent parent"
    )

    return fig


def main_response_1() :
    background = [5] + [4]*0 + [3]*5 + [2]*7 + [1]*9
    for i in range(len(background)) :
        background[i] = '★ ' + str(background[i]) + '   '

    review_star = [5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,3,3,3,4,4,2,4,2,4,3,4,2,3,2,2,1,1,1,3,3]
    for i in range(len(review_star)) :
        review_star[i] = '★ ' + str(review_star[i]) + '   '
    
    fig_1 = go.Histogram(y=review_star, marker_color='rgb(55, 83, 109)')
    fig_2 = go.Histogram(y=background, hoverinfo='skip', marker_color="#e6e8ed")

    fig = go.Figure()
    fig.add_trace(fig_1)
    fig.add_trace(fig_2)

    fig.update_layout({
        'margin': {
            't': 0,
            'b': 0,
            'l': 0,
            'r': 0
        },
        'font': {
            'size': 10
        },
        'plot_bgcolor': 'White',
        'barmode': 'relative',
        'bargap': 0.5,
        'showlegend': False
    })
    
    fig.update_yaxes(showline=False, linewidth=1, linecolor='lightgray', categoryorder='category ascending')
    fig.update_xaxes(showticklabels=False)

    return fig


def main_response_2() :
    fig_1 = go.Indicator(
        value = 200,
        delta = {'reference': 160},
        gauge = {
            'axis': {'visible': False},
            'bar': {
                'color': 'rgb(74, 116, 218)',
                'thickness': 1
            },
            'bgcolor': '#e6e8ed',
            'bordercolor': 'white'
        },
        number = {'font': {'size': 25}}
    )

    fig = go.Figure()
    fig.add_trace(fig_1)

    fig.update_layout({
        'margin': {
            't': 0,
            'b': 0,
            'l': 20,
            'r': 20
        },
        'template': {
            'data' : {
                'indicator': [{
                    # 'title': {'text': "Speed"},
                    'mode' : "number+delta+gauge",
                    # 'delta' : {'reference': 90}
                }]
            }
        }
    })

    return fig


def main_response_3() :
    labels = ['Detractors','Passive','Promoters']
    values = [1000, 700, 1853]
    fig_1 = go.Pie(
        labels=labels, 
        values=values, 
        hole=0.5, 
        textinfo='label+percent',
        marker={
            "line": {
                "width": 3.5, 
                'color':'white'
            }
        }
    )

    fig = go.Figure()
    fig.add_trace(fig_1)

    fig.update_layout({
        'margin': {
                't': 0,
                'b': 0,
                'l': 0,
                'r': 0
            },
        'annotations': [dict(text='70점', x=0.5, y=0.5, font_size=16, showarrow=False)],
        'showlegend': False,
        'font': {
            'size': 9.5
        }
    })
    fig.update_traces(
        marker = {
            # 'colors': ['#f56e6e', 'gray', '#63ad6f']
            'colors': ['pink', '#e6e8ed', 'rgb(156, 185, 251)']
        }
    )

    return fig