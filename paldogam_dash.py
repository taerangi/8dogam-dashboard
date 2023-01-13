#!/usr/bin/python

import custom_fig
from dash import Dash, html, dcc, dependencies
from dash_svg import Svg, G, Path, Circle
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

contents = {
    'main': html.Div([
        html.Div(
            html.Div([
                html.H4("Overview", className="main-title"),
                html.Div([
                    html.Div(
                        html.Div([
                            html.Div(
                                Svg([
                                    Path(d="M14.5 10.33h6.67A.83.83 0 0 0 22 9.5 7.5 7.5 0 0 0 14.5 2a.83.83 0 0 0-.83.83V9.5a.83.83 0 0 0 .83.83zm.83-6.6a5.83 5.83 0 0 1 4.94 4.94h-4.94z"),
                                    Path(d="M21.08 12h-8.15a.91.91 0 0 1-.91-.91V2.92A.92.92 0 0 0 11 2a10 10 0 1 0 11 11 .92.92 0 0 0-.92-1z")
                                ],
                                xmlns="http://www.w3.org/2000/svg", 
                                fill="#555b6d",
                                viewBox="0 0 24 24",
                                className="overview-1-n-icon")
                            , className="overview-1-n-left"),
                            html.Div([
                                html.Div("Profit", className="overview-1-n-mid-1"),
                                html.Div("8,800,000", className="overview-1-n-mid-2")
                            ], className="overview-1-n-mid"),
                            html.Div(
                                html.Div("+11.1%", className="overview-inde increase")
                            , className="overview-1-n-right")
                        ], className="overview-1-n-wrapper")
                    , id="overview-1-1", className="card"),
                    html.Div(
                        html.Div([
                            html.Div(
                                Svg([
                                    Path(d="M24.0391 6C19.5226 6 15.4068 7.49171 12.9723 8.71108C12.7529 8.82095 12.5472 8.92862 12.3561 9.03278C11.9779 9.2389 11.6568 9.43131 11.4001 9.6L14.1701 13.6776L15.4738 14.1967C20.5701 16.768 27.4044 16.768 32.5007 14.1967L33.9811 13.4286L36.6001 9.6C36.2163 9.34413 35.6856 9.03371 35.0324 8.70362C34.9926 8.68351 34.9524 8.66331 34.9117 8.64306C32.4877 7.43697 28.4719 6 24.0391 6ZM17.5968 10.6162C16.6 10.4322 15.6205 10.1786 14.6959 9.88754C16.9772 8.87454 20.377 7.8 24.0391 7.8C26.5764 7.8 28.9755 8.31593 30.9598 8.96919C28.6344 9.29746 26.1529 9.85159 23.789 10.5354C21.9289 11.0735 19.7548 11.0143 17.5968 10.6162ZM33.5567 15.68L33.3116 15.8037C27.7053 18.6324 20.2693 18.6324 14.6629 15.8037L14.4299 15.6861C6.00829 24.9274 -0.421944 41.9971 24.0391 41.9971C48.5001 41.9971 41.9131 24.6085 33.5567 15.68ZM23.0001 24C21.8956 24 21.0001 24.8954 21.0001 26C21.0001 27.1046 21.8956 28 23.0001 28V24ZM25.0001 22V21H23.0001V22C20.791 22 19.0001 23.7909 19.0001 26C19.0001 28.2091 20.791 30 23.0001 30V34C22.1309 34 21.3887 33.4449 21.1137 32.6668C20.9296 32.146 20.3583 31.8731 19.8376 32.0572C19.3169 32.2412 19.0439 32.8125 19.228 33.3332C19.7766 34.8855 21.2569 36 23.0001 36V37H25.0001V36C27.2093 36 29.0001 34.2091 29.0001 32C29.0001 29.7909 27.2093 28 25.0001 28V24C25.8694 24 26.6115 24.5551 26.8866 25.3332C27.0706 25.854 27.6419 26.1269 28.1627 25.9428C28.6834 25.7588 28.9563 25.1875 28.7723 24.6668C28.2236 23.1145 26.7433 22 25.0001 22ZM25.0001 30V34C26.1047 34 27.0001 33.1046 27.0001 32C27.0001 30.8954 26.1047 30 25.0001 30Z", fillRule="evenodd", clipRule="evenodd", fill="white"),
                                ],
                                xmlns="http://www.w3.org/2000/svg", 
                                fill="none",
                                viewBox="0 0 48 48",
                                className="overview-1-n-icon")
                            , className="overview-1-n-left"),
                            html.Div([
                                html.Div("Revenue", className="overview-1-n-mid-1"),
                                html.Div("20,000,000", className="overview-1-n-mid-2")
                            ], className="overview-1-n-mid"),
                            html.Div(
                                html.Div("+11.1%", className="overview-inde increase")
                            , className="overview-1-n-right")
                        ], className="overview-1-n-wrapper")
                    ,id="overview-1-2", className="card"),
                    html.Div(
                        html.Div([
                            html.Div(
                                Svg([
                                    Path(d="M12 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h8zM4 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H4z"),
                                    Path(d="M4 2.5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-.5.5h-7a.5.5 0 0 1-.5-.5v-2zm0 4a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm3-6a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm3-6a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-4z")
                                ],
                                xmlns="http://www.w3.org/2000/svg", 
                                fill="#555b6d",
                                viewBox="0 0 16 16",
                                className="overview-1-n-icon")
                            , className="overview-1-n-left"),
                            html.Div([
                                html.Div("Cost", className="overview-1-n-mid-1"),
                                html.Div("11,200,000", className="overview-1-n-mid-2")
                            ], className="overview-1-n-mid"),
                            html.Div(
                                html.Div("+12.0%", className="overview-inde increase")
                            , className="overview-1-n-right")
                        ], className="overview-1-n-wrapper")
                    ,id="overview-1-3", className="card"),
                    html.Div(
                        html.Div([
                            html.Div(
                                dcc.Graph(figure=custom_fig.main_overview(), className="fig")
                            , id="overview-2-1"),
                            html.Div(
                                html.Div([
                                    html.Div(
                                        html.Div([
                                            html.Div("Customer", className="overview-2-2-n-1"),
                                            html.Div([
                                                html.Div("1,000", className="overview-2-2-n-2-1"),
                                                html.Div(
                                                    html.Div("+5.26%", className="overview-inde increase")
                                                , className="overview-2-2-n-2-2")
                                            ], className="overview-2-2-n-2")    
                                        ], className="overview-2-2-n-wrapper")
                                    , className="overview-2-2-n"),
                                    html.Div(
                                        html.Div([
                                            html.Div("Operating Expense", className="overview-2-2-n-1"),
                                            html.Div([
                                                html.Div("8,300,000", className="overview-2-2-n-2-1"),
                                                html.Div(
                                                    html.Div("-1.18%", className="overview-inde decrease")
                                                , className="overview-2-2-n-2-2")
                                            ], className="overview-2-2-n-2")    
                                        ], className="overview-2-2-n-wrapper")
                                    , className="overview-2-2-n"),
                                    html.Div(
                                        html.Div([
                                            html.Div("Average Consumption", className="overview-2-2-n-1"),
                                            html.Div([
                                                html.Div("20,000", className="overview-2-2-n-2-1"),
                                                html.Div(
                                                    html.Div("-0.25%", className="overview-inde decrease")
                                                , className="overview-2-2-n-2-2")
                                            ], className="overview-2-2-n-2")    
                                        ], className="overview-2-2-n-wrapper")
                                    , className="overview-2-2-n"),
                                    html.Div(
                                        html.Div([
                                            html.Div("Fixed Cost", className="overview-2-2-n-1"),
                                            html.Div([
                                                html.Div("3,200,000", className="overview-2-2-n-2-1"),
                                                html.Div(
                                                    html.Div("-3.12%", className="overview-inde decrease")
                                                , className="overview-2-2-n-2-2")
                                            ], className="overview-2-2-n-2")    
                                        ], className="overview-2-2-n-wrapper")
                                    , className="overview-2-2-n"),
                                    html.Div(
                                        html.Div([
                                            html.Div("Sales Quantitiy", className="overview-2-2-n-1"),
                                            html.Div([
                                                html.Div("1,700", className="overview-2-2-n-2-1"),
                                                html.Div(
                                                    html.Div("+0.3%", className="overview-inde increase")
                                                , className="overview-2-2-n-2-2")
                                            ], className="overview-2-2-n-2")    
                                        ], className="overview-2-2-n-wrapper")
                                    , className="overview-2-2-n"),
                                    html.Div(
                                        html.Div([
                                            html.Div("Variable Cost", className="overview-2-2-n-1"),
                                            html.Div([
                                                html.Div("8,000,000", className="overview-2-2-n-2-1"),
                                                html.Div(
                                                    html.Div("+15.5%", className="overview-inde increase")
                                                , className="overview-2-2-n-2-2")
                                            ], className="overview-2-2-n-2")    
                                        ], className="overview-2-2-n-wrapper")
                                    , className="overview-2-2-n")
                                ], id="overview-2-2-wrapper")
                            , id="overview-2-2")
                        ], id="overview-2-wrapper")
                    , id="overview-2", className="card")
                ], id="main-overview-content")
            ], id="main-overview-wrapper")
        , id="main-overview"),

        html.Div(
            html.Div([
                html.H4("User", className="main-title"),
                html.Div([
                    html.Div(
                        html.Div(
                            dcc.Graph(figure=custom_fig.main_user_1(), className="fig")
                        , id="main-user-left-wrapper")
                    , id="main-user-left", className="card"),
                    html.Div(
                        html.Div(
                            dcc.Graph(figure=custom_fig.main_user_2(), id="main-user-right-fig")
                        ,id="main-user-right-wrapper")
                    , id="main-user-right", className="card")
                ], id="main-user-content")
            ], id="main-user-wrapper")
        , id="main-user"),
        
        html.Div(
            html.Div([
                html.H4("Response", className="main-title"),
                html.Div(
                    html.Div([
                        html.Div([
                            html.H5('Review', className="response-title"),
                            html.Div([
                                html.Div("4.2", id="response-1-1"),
                                html.Div(
                                    html.Div([
                                        html.Div([
                                            html.Span("★"), html.Span("★"), html.Span("★"), html.Span("★"), html.Span("★")
                                        ], id="star-ratings-fill", style={"width": f"{90}%"}),
                                        html.Div([
                                            html.Span("★"), html.Span("★"), html.Span("★"), html.Span("★"), html.Span("★")
                                        ], id="star-ratings-base")
                                    ], id="star-ratings")
                                , id="response-1-2"),
                                html.Div("(1,000 based)", id="response-1-3"),
                                html.Div(
                                    dcc.Graph(figure=custom_fig.main_response_1(), className="fig")    
                                , id="response-1-4")
                            ], id="response-1-wrapper")
                        ], id="response-1"),
                        html.Div([
                            html.H5('Repurchase Rate', className="response-title"),
                            html.Div([
                                html.Div(
                                    dcc.Graph(figure=custom_fig.main_response_2(), className="fig")
                                , id="response-2-1"),
                                html.Div("(1,700 based)", id="response-2-2")
                            ], id="response-2-wrapper")
                        ], id="response-2"),
                        html.Div([
                            html.H5('NPS', className="response-title"),
                            html.Div([
                                dcc.Graph(figure=custom_fig.main_response_3(), className="fig"),
                                html.Div("(1,000 based / 2022 Dec)", id="response-3-2")
                            ], className="response-n-wrapper")
                        ], id="response-3")
                    ], id="response-content-wrapper")
                , id="main-response-content", className="card")
            ], id="main-response-wrapper")
        , id="main-response")
    ], id="content-main-wrapper"),
    
    'user': html.Div([
        html.Div(
            html.Div([
                html.H4("User Status", className="main-title"),
                html.Div(
                    dcc.Graph(figure=custom_fig.user_status(), id="user-status-fig")
                , className="user-content card")
            ], id="user-status-wrapper")
        , id="user-status"),
        html.Div(
            html.Div([
                html.H4("User Retention", className="main-title"),
                html.Div(
                    html.Div(
                        dcc.Graph(figure=custom_fig.user_retention(), className="fig")
                    , className="fig-wrapper")
                , className="user-content card")
            ], id="user-retention-wrapper")
        , id="user-retention"),
        html.Div(
            html.Div([
                html.H4("User Flow", className="main-title"),
                html.Div(
                    html.Div(
                        dcc.Graph(figure=custom_fig.user_flow(), className="fig")
                    , className="fig-wrapper")
                , className="user-content card")
            ], id="user-flow-wrapper")
        , id="user-flow"),
        html.Div(
            html.Div([
                html.H4("User Persona", className="main-title"),
                html.Div(
                    html.Div([
                        html.Div([
                            html.Img(src="assets/persona.png", className="persona-1-1"),
                            html.Div([
                                html.Div("김팔도", className="persona-1-2-1 response-title"),
                                html.Div('"음식에 투자하는 것을 아끼지 말자!"', className="persona-1-2-2")
                            ], className="persona-1-2")
                        ], className="persona-1"),
                        html.Div([
                            html.H5("Personal Info", className="persona-2-1 persona-title"),
                            html.Div([
                                html.Div("Age", className="persona-2-2-1"),
                                html.Div("43"),
                                html.Div("Gender", className="persona-2-2-1"),
                                html.Div("Woman"),
                                html.Div("Location", className="persona-2-2-1"),
                                html.Div("Seoul, Gangnam"),
                                html.Div("Household", className="persona-2-2-1"),
                                html.Div("4 people"),
                                html.Div("Budget", className="persona-2-2-1"),
                                html.Div("₩ 1,000,000 / month"),
                                html.Div("Cooking", className="persona-2-2-1"),
                                html.Div("15 times / week")
                            ], className="persona-2-2")
                        ], className="persona-2"),
                        html.Div([
                            html.H5("Activity", className="persona-3-1 persona-title"),
                            html.Div([
                                html.Div("Using App", className="persona-2-2-1"),
                                html.Div("27 / month"),
                                html.Div("Avg Pageview", className="persona-2-2-1"),
                                html.Div("7"),
                                html.Div("Avg Duration", className="persona-2-2-1"),
                                html.Div("00:05:30"),
                                html.Div("Purchase", className="persona-2-2-1"),
                                html.Div("240,000 / month"),
                            ], className="persona-2-2"),
                        ], className="persona-3"),
                        html.Div([
                            html.H5("Purchase History by Category", className="persona-4-1 persona-title"),
                            dcc.Graph(figure=custom_fig.user_persona(), className="persona-4-2")
                        ], className="persona-4"),
                    ], id="persona-content-wrapper")
                , className="user-content card")
            ], id="user-persona-wrapper")
        , id="user-persona")
    ], id="content-user-wrapper"),
    
    'product': html.Div([
        html.Div(
            html.Div([
                html.H4("10 Best-Selling Products", className="main-title"),
                html.Div(
                    html.Div(
                        dcc.Graph(figure=custom_fig.product_top10(), className="fig")
                    , className="fig-wrapper")
                , className="card user-content")
            ], id="product-top10-wrapper")
        , id="product-top10"),
        html.Div(
            html.Div([
                html.H4("Sales by Category", className="main-title"),
                html.Div(
                    html.Div(
                        dcc.Graph(figure=custom_fig.product_category(), className="fig")
                    , className="fig-wrapper")
                , className="card user-content")
            ], id="product-category-wrapper")
        , id="product-category"),
        html.Div(
            html.Div([
                html.H4("Details", className="main-title"),
                html.Div(
                    html.Div([
                        dcc.Dropdown(
                            {"sort1" : "국산 1/1+등급 무항생돈 냉장 양념돼지갈비 650g"}
                        , id="product-detail-dropdown"),
                        html.Div([
                            html.Div(
                                html.H4("국산 1/1+등급 무항생돈 냉장 양념돼지갈비 650g", className="persona-title")
                            , id="product-detail-1-1"),
                            html.Div([
                                html.Img(src="assets/seller.jpeg", id="product-detail-1-2-1"),
                                html.Div("부산기장 강현주", id="product-detail-1-2-2"),
                                html.Div("₩ 17,000", id="product-detail-1-2-3")
                            ], id="product-detail-1-2")
                        ], id="product-detail-1"),
                        html.Div([
                            html.Div(
                                html.Img(src="assets/product_detail.jpeg", className="fig")
                            , id="product-detail-2-1"),
                            html.Div([
                                html.Div([
                                    html.Div("4.8", id="response-1-1"),
                                    html.Div(
                                        html.Div([
                                            html.Div([
                                                html.Span("★"), html.Span("★"), html.Span("★"), html.Span("★"), html.Span("★")
                                            ], id="star-ratings-fill", style={"width": f"{92}%"}),
                                            html.Div([
                                                html.Span("★"), html.Span("★"), html.Span("★"), html.Span("★"), html.Span("★")
                                            ], id="star-ratings-base")
                                        ], id="star-ratings")
                                    , id="response-1-2"),
                                    html.Div("(2,000 based)", id="response-1-3"),
                                    html.Div(
                                        dcc.Graph(figure=custom_fig.product_detail_review(), className="fig")    
                                    , id="response-1-4")
                                ], id="product-detail-2-2-1")
                            ], id="product-detail-2-2"),
                            html.Div(
                                html.Img(src="assets/product_wordcloud.png", className="fig")
                            , id="product-detail-2-3"),
                            html.Div([
                                html.H5("Repurchase", id="product-detail-2-4-1"),   
                                dcc.Graph(figure=custom_fig.product_detail_repurchase(), id="product-detail-2-4-2")
                            ], id="product-detail-2-4"),
                            html.Div([
                                html.H5("Sales", id="product-detail-2-5-1"),
                                dcc.Graph(figure=custom_fig.product_detail_sales(), id="product-detail-2-5-2")
                            ], id="product-detail-2-5"),
                            html.Div(
                                dcc.Graph(figure=custom_fig.product_network(), className="fig")
                            , id="product-detail-2-6")
                        ], id="product-detail-2"),
                        html.Div(id="product-detail-line")
                    ], id="product-detail-content-wrapper")
                , className="card user-content")
            ], id="product-detail-wrapper")
        , id="product-detail")
    ], id="content-product-wrapper")
}

app = Dash(__name__, title="Paldogam Business Dashboard", assets_external_path=".")
server = app.server

app.layout = html.Div([
    html.Div(
        html.Img(src="assets/팔도감_로고.webp", id="logo-img")
    , id="logo"),

    html.Header([
        html.H3("Paldogam Business Dashboard", id="header-text"),
        # html.P("by 태랑", id="header-made-by")
    ], id="header"),

    html.Div([
        html.Div(id="menu-selected-bar", style={"top": "15px"}),
        html.Div([
            html.Div([
                html.Button([
                    Svg([
                        Path(
                            d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6zm5-.793V6l-2-2V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5z",
                            fill="white"     
                        ),
                        Path(
                            d="M7.293 1.5a1 1 0 0 1 1.414 0l6.647 6.646a.5.5 0 0 1-.708.708L8 2.207 1.354 8.854a.5.5 0 1 1-.708-.708L7.293 1.5z", 
                            fill="white"
                        )],
                        xmlns="http://www.w3.org/2000/svg",
                        fill="currentColor", 
                        viewBox="0 0 16 16",
                        className="menu-button-icon"
                    ),
                    html.Div("Main", className="menu-button-text")
                ], id="button-main", className="menu-button")
            ], className="menu-button-cell"),
            html.Div([
                html.Button([
                    Svg([
                        Path(d="M9 11a4 4 0 1 0-4-4 4 4 0 0 0 4 4z"),
                        Path(d="M17 13a3 3 0 1 0-3-3 3 3 0 0 0 3 3z"),
                        Path(d="M21 20a1 1 0 0 0 1-1 5 5 0 0 0-8.06-3.95A7 7 0 0 0 2 20a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1")
                        ],
                        xmlns="http://www.w3.org/2000/svg", 
                        fill="#555b6d", 
                        viewBox="0 0 24 24",
                        className="menu-button-icon"
                    ),
                    html.Div("User", className="menu-button-text")
                ], id="button-user", className="menu-button")
            ], className="menu-button-cell"),
            html.Div([
                html.Button([
                    Svg([
                        Path(d="M20.12 6.71l-2.83-2.83A3 3 0 0 0 15.17 3H8.83a3 3 0 0 0-2.12.88L3.88 6.71A3 3 0 0 0 3 8.83V18a3 3 0 0 0 3 3h12a3 3 0 0 0 3-3V8.83a3 3 0 0 0-.88-2.12zM12 16a4 4 0 0 1-4-4 1 1 0 0 1 2 0 2 2 0 0 0 4 0 1 1 0 0 1 2 0 4 4 0 0 1-4 4zM6.41 7l1.71-1.71A1.05 1.05 0 0 1 8.83 5h6.34a1.05 1.05 0 0 1 .71.29L17.59 7z"),
                        ],
                        xmlns="http://www.w3.org/2000/svg", 
                        fill="#555b6d", 
                        viewBox="0 0 24 24",
                        className="menu-button-icon"
                    ),
                    html.Div("Product", className="menu-button-text")
                ], id="button-product", className="menu-button")
            ], className="menu-button-cell")
        ], id="menu-button-wrapper")
    ], id="menu"),
    html.Div(
        contents['main']
    , id="content")
])

@app.callback(
    dependencies.Output(component_id='content', component_property='children'),
    dependencies.Output(component_id='menu-selected-bar', component_property='style'),
    dependencies.Input(component_id='button-main', component_property='n_clicks_timestamp'),
    dependencies.Input(component_id='button-user', component_property='n_clicks_timestamp'),
    dependencies.Input(component_id='button-product', component_property='n_clicks_timestamp')
)
def update_output(button_main_ts, button_user_ts, button_product_ts):
    ts_dict = {
        'main': button_main_ts if button_main_ts!=None else 0,
        'user': button_user_ts if button_user_ts!=None else 0,
        'product': button_product_ts if button_product_ts!=None else 0
    }
    recent_button = max(ts_dict, key=ts_dict.get)
    # recent_button = 'product' # for debug

    menu_selected_bar_top_dict = {
        'main': 15,
        'user': 15 + 20 + 39,
        'product': 15 + 20*2 + 39*2
    }
    menu_selected_bar_top = menu_selected_bar_top_dict[recent_button]

    return contents[recent_button], {"top": f"{menu_selected_bar_top}px"}


if __name__ == "__main__":
    app.run_server(debug=True)