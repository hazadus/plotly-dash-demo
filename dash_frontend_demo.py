# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
# https://987703-hazadus.tmweb.ru:8050
# Tutorial: https://dash.plotly.com/layout

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df_users = pd.DataFrame({
    "Пользователь": ["Флоренцев", "Голдовский", "Поздняков", "Иванов", "Мельников"],
    "Количество": [112, 46, 9, 10, 2],
})

df_words = pd.DataFrame({
    "Слово": ["Хуй", "Ебать", "Пизда", "Блядь", "Пидор"],
    "Количество": [85, 51, 21, 17, 5],
})

fig_users = px.bar(df_users, x="Пользователь", y="Количество", color="Пользователь", barmode="group")
fig_words = px.bar(df_words, x="Слово", y="Количество", color="Слово", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Рейтинг Большого Брата'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='user-graph',
        figure=fig_users
    ),

    dcc.Graph(
        id='word-graph',
        figure=fig_words
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
