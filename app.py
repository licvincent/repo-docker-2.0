import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
import os

# URL del archivo CSV (asegúrate de que esta URL sea correcta)
url = 'https://raw.githubusercontent.com/licvincent/Hipertension_Arterial_Mexico/refs/heads/main/Hipertension_Arterial_Mexico.csv'

try:
    df = pd.read_csv(url)
    print(df.head())
    print(df.describe())

    # Creación de Grupos de Edad
    def categorize_age(edad):
        if edad < 18:
            return 'Niños'
        elif edad < 36:
            return 'Jóvenes'
        elif edad < 61:
            return 'Adultos'
        else:
            return 'Adultos Mayores'

    df['Grupo_Edad'] = df['edad'].apply(categorize_age)

    # Agrupar por 'Sexo' y 'Grupo_Edad' y calcular la media de hipertensión
    grouped = df.groupby(['sexo', 'Grupo_Edad'])['riesgo_hipertension'].mean().reset_index()

    # Convertir la proporción a porcentaje
    grouped['Riesgo (%)'] = grouped['riesgo_hipertension'] * 100

    print(grouped)

    # Crear la visualización
    fig = px.bar(grouped,
                    x='Grupo_Edad',
                    y='Riesgo (%)',
                    color='sexo',
                    barmode='group',
                    title='Riesgo de Hipertensión por Sexo y Grupo de Edad',
                    labels={'Grupo_Edad': 'Grupo de Edad', 'Riesgo (%)': 'Porcentaje de Hipertensión'},
                    color_discrete_map={
                        'Hombre(1)': 'blue',
                        'Mujer(2)': 'pink'
                    }
                    )

    # Crear la app de Dash
    app = dash.Dash(__name__)
    server = app.server  # Necesario para Cloud Run

    app.layout = html.Div(style={'backgroundColor': '#F9F9F9', 'padding': '20px'}, children=[
        html.Div([
            html.H1("Dashboard de Hipertensión Arterial en México", style={'textAlign': 'center'}),
            html.P("Comparación del riesgo de hipertensión entre hombres y mujeres agrupados por edades.", style={'textAlign': 'center'})
        ], style={'padding': '20px', 'backgroundColor': '#e9ecef', 'marginBottom': '20px'}),
        html.Div([
            dcc.Graph(id='graph', figure=fig)
        ])
    ])

#    if __name__ == '__main__':
#        app.run_server(debug=True)

    if __name__ == '__main__':
        port = int(os.getenv("PORT", 8080))
        app.run_server(host='0.0.0.0', port=port, debug=False)        

except Exception as e:
    print(f"Error al cargar el archivo desde la URL: {e}")
