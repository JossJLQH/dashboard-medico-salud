import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

print("1. Librerías importadas correctamente...")

# 1. Datos simulados de ejemplo para el sector salud
df_ocupacion = pd.DataFrame({
    'Día': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
    'Ocupación (%)': [82, 85, 78, 90, 88, 75, 70]
})

df_deptos = pd.DataFrame({
    'Departamento': ['Urgencias', 'UCI', 'Pediatría', 'Cardiología', 'Ortopedia'],
    'Pacientes': [45, 18, 30, 25, 22]
})

# 2. Inicialización de la aplicación Dash
app = dash.Dash(__name__)
server = app.server

# 3. Diseño de la interfaz (Layout con estilo Dark Mode)
app.layout = html.Div(style={
    'backgroundColor': '#090d16', 
    'color': '#f8fafc', 
    'padding': '40px', 
    'fontFamily': "'Inter', sans-serif", 
    'minHeight': '100vh'
}, children=[
    
    html.H1("Dashboard Clínico & Hospitalario", style={
        'textAlign': 'center', 
        'color': '#38bdf8', 
        'marginBottom': '10px',
        'fontWeight': '800'
    }),
    html.P("Monitoreo en tiempo real de ocupación hospitalaria y flujo de pacientes por departamento.", style={
        'textAlign': 'center', 
        'color': '#94a3b8', 
        'marginBottom': '40px',
        'fontSize': '1.05rem'
    }),
    
    html.Div([
        html.Div([
            dcc.Graph(
                figure=px.line(
                    df_ocupacion, x='Día', y='Ocupación (%)', 
                    title='Tendencia Semanal de Ocupación Hospitalaria',
                    markers=True
                ).update_layout(
                    paper_bgcolor='#1e293b', 
                    plot_bgcolor='#1e293b', 
                    font_color='#f8fafc',
                    title_font_size=16
                )
            )
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px', 'boxSizing': 'border-box'}),
        
        html.Div([
            dcc.Graph(
                figure=px.bar(
                    df_deptos, x='Departamento', y='Pacientes', 
                    title='Distribución de Pacientes por Departamento',
                    color='Pacientes', color_continuous_scale='Blues'
                ).update_layout(
                    paper_bgcolor='#1e293b', 
                    plot_bgcolor='#1e293b', 
                    font_color='#f8fafc',
                    title_font_size=16
                )
            )
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px', 'boxSizing': 'border-box'})
    ], style={'display': 'flex', 'justifyContent': 'center', 'flexWrap': 'wrap', 'maxWidth': '1200px', 'margin': '0 auto'})
])

if __name__ == '__main__':
    print("2. Iniciando servidor Dash...")
    app.run(host='127.0.0.1', port=8050, debug=False)