# Import Library
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def main_overview() :
    fig = go.Figure()

    month = [f'{i}월' for i in range(7, 13)]
    revenue = [12000000, 17000000, 22000000, 17000000, 18000000, 20000000]
    profit = [5800000, 6000000, 10000000, 5800000, 8000000, 8800000]
    fig_1 = go.Bar(x=month, y=revenue, name='Revenue', marker_color='rgb(55, 83, 109)')
    fig_2 = go.Bar(x=month, y=profit, name='Profit', marker_color='#3b76e1')

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
    fig.update_yaxes(showline=True, linewidth=1, linecolor='lightgray', gridcolor='#f1f3f7', range=[0,28000000])

    return fig


def main_user_1() :
    month = [f'{i}월' for i in range(7, 13)]
    user_active = [1400, 1700, 3000, 2000, 1700, 2000]
    user_new = [500, 1100, 800, 500, 700, 500]
    customer = [800, 850, 1600, 850, 950, 1000]

    fig = go.Figure()
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
        'hovermode': 'x unified'
    })
    fig.update_xaxes(showline=True, linewidth=1, linecolor='lightgray')
    fig.update_yaxes(showline=True, linewidth=1, linecolor='lightgray', range=[0, 4000], gridcolor='#f1f3f7')

    return fig


def main_user_2() :
    center = '7,000 user'
    pie_1_1 = 'active user'
    pie_1_2 = 'inactive user'
    pie_2 = 'customer'

    fig_1 = go.Sunburst(
        labels=[center, pie_1_1, pie_1_2, pie_2],
        parents=[""   , center , center , pie_1_1],
        branchvalues="total",
        values=[7000, 2000, 5000, 1000],
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
            'r': 20
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
    background = [5]*50 + [4]*0 + [3]*370 + [2]*400 + [1]*430
    for i in range(len(background)) :
        background[i] = '★ ' + str(background[i]) + '   '

    review_star = [5]*400 + [4]*450 + [3]*80 + [2]*50 + [1]*20
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
        value = 35,
        delta = {'reference': 30},
        gauge = {
            'axis': {
                'visible': False, 
                'range': [0, 100]
            },
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
                    'mode' : "number+delta+gauge",
                    'delta' : {'suffix': '%p'},
                    'number' : {
                        'suffix': '%',
                    }
                }]
            }
        }
    })

    return fig


def main_response_3() :
    labels = ['Detractors','Passive','Promoters']
    values = [150, 250, 600]
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
        'annotations': [dict(text='45점', x=0.5, y=0.5, font_size=16, showarrow=False)],
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


def user_retention() :
    month = [f'{i} week' for i in range(7)]
    cohort_1 = [100, 40, 33, 30, 27, 25, 24]
    cohort_2 = [100, 30, 25, 23, 22, 21, 20]
    cohort_3 = [100, 22, 20, 18, 16, 14, 12]

    fig = go.Figure()
    fig_1 = go.Scatter(x=month, y=cohort_1, line_shape='spline', line_color='rgb(26, 118, 255)', name='cohort 1', mode='lines')
    fig_2 = go.Scatter(x=month, y=cohort_2, line_shape='spline', line_color='#7be0e0', name='cohort 2', mode='lines')
    fig_3 = go.Scatter(x=month, y=cohort_3, line_shape='spline', line_color='lavender', name='cohort 3', mode='lines')
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
        'hovermode': 'x unified'
    })
    fig.update_xaxes(showline=True, linewidth=1, linecolor='lightgray')
    fig.update_yaxes(showline=True, linewidth=1, linecolor='lightgray', range=[0, 100], gridcolor='#f1f3f7')

    return fig


def user_flow() :
    label_list = [
        'SNS', 'Offline', 'etc', # 0, 1, 2
        'Activation', # 3
        'Home', 'Best', 'New', 'Category', 'Search', # 4, 5, 6, 7, 8
        'Cart', # 9
        'Purchase', # 10
        'Repurchase', # 11
    ]

    data = pd.read_csv('data/user_flow.csv')

    fig_1 = go.Sankey(
        node = dict(
            pad = 15,
            thickness = 20,
            # line = dict(color = data['line_color'], width = 0.5),
            label = label_list,
            # color = ["green", "orange"] * 4
        ),
        link = dict(
            # source[n] -> target[n] = value[n]
            source = data['index_s'],
            target = data['index_t'],
            value = data['value'],
            color = '#e6e8ed' # data['line_color']
        )
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
    })

    return fig


def user_persona() :
    background = ['Meat ']*1 + ['Seafood ']*0 + ['Fruit ']*5 + ['Beverage ']*7 + ['Vegetable ']*4

    category = ['Meat ']*11 + ['Seafood ']*12 + ['Fruit ']*7 + ['Beverage ']*5 + ['Vegetable ']*8
    
    fig_1 = go.Histogram(y=category, marker_color='rgb(55, 83, 109)')
    fig_2 = go.Histogram(y=background, hoverinfo='skip', marker_color="#e6e8ed")

    fig = go.Figure()
    fig.add_trace(fig_1)
    fig.add_trace(fig_2)

    fig.update_layout({
        'margin': {
            't': 0,
            'b': 0,
            'l': 70,
            'r': 10
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


def product_top10() :
    data = pd.read_csv('data/product_top10.csv')

    background = []
    product = []
    max_num = data['num'].max()
    text = data['product'].to_list()
    text.reverse()  
    for i in range(10) :
        product += [data.loc[i, 'product']] * data.loc[i, 'num']
        background += [data.loc[i, 'product']] * (max_num - data.loc[i, 'num'])

    fig_1 = go.Histogram(y=product, marker_color=['#cecef5', '#bfbfff', '#a3a3ff', '#7879ff', '#5752de', '#4949ff', '#3b3be3', '#1414e3', '#0f0fa6', '#0c0c96'], text=text, insidetextanchor='start')
    fig_2 = go.Histogram(y=background, hoverinfo='skip', marker_color="#e6e8ed")

    fig = go.Figure()
    fig.add_trace(fig_1)
    fig.add_trace(fig_2)

    fig.update_layout({
        'margin': {
            't': 0,
            'b': 0,
            'l': 20,
            'r': 10
        },
        'font': {
            'size': 11
        },
        'plot_bgcolor': 'White',
        'barmode': 'relative',
        'bargap': 0.5,
        'showlegend': False
    })

    fig.update_yaxes(
        showline=False, 
        linewidth=1, 
        linecolor='lightgray', 
        # categoryorder='category ascending',
        categoryorder='total descending'
        # tickangle=10,
        # tickfont={'size':10}
    )
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)

    return fig


def product_category() :
    background = ['Meat ']*0 + ['Seafood ']*400 + ['Fruit ']*200 + ['Beverage ']*600 + ['Vegetable ']*500

    category = ['Meat ']*700 + ['Seafood ']*300 + ['Fruit ']*500 + ['Beverage ']*100 + ['Vegetable ']*200
    
    fig_1 = go.Histogram(y=category, marker_color='rgb(55, 83, 109)'    ) #'rgb(55, 83, 109)'
    fig_2 = go.Histogram(y=background, hoverinfo='skip', marker_color="#e6e8ed")

    fig = go.Figure()
    fig.add_trace(fig_1)
    fig.add_trace(fig_2)

    fig.update_layout({
        'margin': {
            't': 0,
            'b': 0,
            'l': 70,
            'r': 10
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


def product_network() :
    data = pd.read_csv('data/product_network.csv')

    fig = go.Figure()

    fig_1 = go.Scatter(
        x=data['x'],
        y=data['y'],
        mode='markers+text',
        marker=dict(
            size=data['size'],
            color=data['color'],
            opacity=1
        ),
        text=data['text'],
        textposition="top center",
        hovertemplate="%{marker.size}"
    )

    for i in range(1, 9) :
        fig_n = go.Scatter(
            x = data.loc[[0, i], 'x'],
            y = data.loc[[0, i], 'y'],
            mode='lines',
            line={
                'width': 1,
                'color': 'lightgray'
            },
            hoverinfo='skip'
        )
        fig.add_trace(fig_n)

    fig.update_layout({
        'margin': {
            't': 0,
            'b': 0,
            'l': 20,
            'r': 0
        },
        'font': {
            'size': 11
        },
        'plot_bgcolor': 'White',
        'showlegend': False
    })

    fig.add_trace(fig_1)

    fig.update_yaxes(showticklabels=False, range=[0,10])
    fig.update_xaxes(showticklabels=False, range=[0,10])

    return fig


def product_detail_repurchase() :
    fig_1 = go.Indicator(
        value = 45,
        delta = {'reference': 38},
        gauge = {
            'shape': 'bullet',
            'axis': {
                'visible': False, 
                'range': [0, 100]
            }, 
            'bar': {
                'color': 'rgb(74, 116, 218)',
                'thickness': 1
            },
            'bgcolor': '#e6e8ed',
            'bordercolor': 'white',
        },
        number = {'font': {'size': 18}}
    )

    fig = go.Figure()
    fig.add_trace(fig_1)

    fig.update_layout({
        'margin': {
            't': 20,
            'b': 40,
            'l': 20,
            'r': 20
        },
        'template': {
            'data' : {
                'indicator': [{
                    # 'title': {'text': "Speed"},
                    'mode' : "number+delta+gauge",
                    'delta' : {'suffix': '%p'},
                    'number' : {
                        'suffix': '%',
                    }
                }]
            }
        }
    })

    return fig


def product_detail_sales() :
    month = [f'{i}월' for i in range(7, 13)]
    sales = [17000*500, 17000*650, 17000*900, 17000*550, 17000*650, 17000*750]

    fig = go.Figure()
    fig_1 = go.Scatter(x=month, y=sales, line_shape='spline', fill='tozeroy', line_color='rgb(26, 118, 255)', name='active user', mode='lines') #rgb(55, 83, 109)
    fig.add_trace(fig_1)
    
    fig.update_layout({
        'margin': {
            't': 0,
            'b': 0,
            'l': 0,
            'r': 0
        },
        'plot_bgcolor': 'White',
        'xaxis_tickfont_size': 10,
        'yaxis_tickfont_size': 10,
        'hovermode': 'x unified'
    })
    fig.update_xaxes(showline=True, linewidth=1, linecolor='lightgray')
    fig.update_yaxes(showline=True, linewidth=1, linecolor='lightgray', gridcolor='#f1f3f7', range=[3000000, 18000000])

    return fig


def product_detail_review() :
    background = [5]*0 + [4]*1650 + [3]*1670 + [2]*1700 + [1]*1730
    for i in range(len(background)) :
        background[i] = '★ ' + str(background[i]) + '   '

    review_star = [5]*1750 + [4]*100 + [3]*80 + [2]*50 + [1]*20
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


def user_status() :
    center = '7,000 user'
    pie_1_1 = 'active user'
    pie_1_2 = 'inactive user'
    pie_2 = 'customer'

    fig_1 = go.Sunburst(
        labels=[center, pie_1_1, pie_1_2, pie_2],
        parents=[""   , center , center , pie_1_1],
        branchvalues="total",
        values=[7000, 2000, 5000, 1000],
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

    fig_2 = go.Indicator(
        mode = "delta",
        value = 7000,
        delta = {
            "reference": 6500, 
            "valueformat": ".0f",
            'font': {'size': 10}
        },
        domain = {'y': [0, 0.88], 'x': [0.25, 0.75]}
    )

    fig = go.Figure()
    fig.add_trace(fig_1)

    fig.update_layout({
        'margin': {
            't': 20,
            'b': 0,
            'l': 0,
            'r': 40
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

    fig.add_trace(fig_2)

    return fig