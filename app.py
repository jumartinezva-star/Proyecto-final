import streamlit as st
from transformers import pipeline
import plotly.graph_objects as go
import time

# Configuración de la página
st.set_page_config(
    page_title="Análisis de Sentimientos Multilingüe",
    page_icon="🎭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo CSS personalizado
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5rem 1rem;
    }
    .sentiment-box {
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Cache del modelo para mejorar rendimiento
@st.cache_resource
def load_model():
    """Carga el modelo de análisis de sentimientos"""
    return pipeline(
        "text-classification", 
        model="tabularisai/multilingual-sentiment-analysis"
    )

# Función para análisis
def analyze_sentiment(text, pipe):
    """Realiza el análisis de sentimientos"""
    result = pipe(text)
    return result[0]

# Función para crear gráfico de barras
def create_sentiment_chart(label, score):
    """Crea un gráfico de barras para visualizar el sentimiento"""
    colors = {
        'Positive': '#00CC96',
        'Negative': '#EF553B',
        'Neutral': '#636EFA'
    }
    
    fig = go.Figure(go.Bar(
        x=[score],
        y=[label],
        orientation='h',
        marker_color=colors.get(label, '#636EFA'),
        text=[f'{score:.2%}'],
        textposition='auto',
    ))
    
    fig.update_layout(
        xaxis_title="Confianza",
        xaxis=dict(range=[0, 1]),
        height=200,
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False
    )
    
    return fig

# Interfaz principal
def main():
    # Header
    st.title("🎭 Análisis de Sentimientos Multilingüe")
    st.markdown("### Analiza el sentimiento de textos en múltiples idiomas")
    
    # Sidebar
    with st.sidebar:
        st.header("ℹ️ Información")
        st.markdown("""
        **Modelo:** tabularisai/multilingual-sentiment-analysis
        
        **Idiomas soportados:**
        - Español 🇪🇸
        - Inglés 🇬🇧
        - Francés 🇫🇷
        - Alemán 🇩🇪
        - Y muchos más...
        
        **Categorías:**
        - 🤩 Muy Positivo
        - 😊 Positivo
        - 😐 Neutral
        - 😞 Negativo
        - 😡 Muy Negativo
        """)
        
        st.divider()
        
        st.header("📊 Ejemplos")
        example_texts = {
            "Positivo (ES)": "¡Me encanta este producto! Es increíble y funciona perfectamente.",
            "Negativo (ES)": "Terrible experiencia, no lo recomiendo a nadie.",
            "Neutral (ES)": "El producto llegó en la fecha indicada.",
            "Positive (EN)": "This is amazing! I absolutely love it!",
            "Negative (EN)": "Worst purchase ever. Very disappointed.",
        }
        
        selected_example = st.selectbox(
            "Selecciona un ejemplo:",
            ["Ninguno"] + list(example_texts.keys())
        )
    
    # Área principal
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📝 Ingresa tu texto")
        
        # Usar ejemplo si se seleccionó uno
        default_text = ""
        if selected_example != "Ninguno":
            default_text = example_texts[selected_example]
        
        user_input = st.text_area(
            "Escribe o pega el texto a analizar:",
            value=default_text,
            height=150,
            placeholder="Ejemplo: Trump concede a Nvidia permiso para vender chips avanzados..."
        )
        
        analyze_button = st.button("🔍 Analizar Sentimiento", type="primary")
    
    with col2:
        st.subheader("⚙️ Configuración")
        show_raw = st.checkbox("Mostrar datos técnicos", value=False)
        show_chart = st.checkbox("Mostrar gráfico", value=True)
    
    # Análisis
    if analyze_button:
        if not user_input.strip():
            st.warning("⚠️ Por favor, ingresa un texto para analizar.")
        else:
            with st.spinner("Analizando sentimiento..."):
                # Cargar modelo
                pipe = load_model()
                
                # Simular tiempo de procesamiento para UX
                time.sleep(0.5)
                
                # Realizar análisis
                result = analyze_sentiment(user_input, pipe)
                
            # Mostrar resultados
            st.success("✅ Análisis completado!")
            
            st.divider()
            
            # Resultados principales
            st.subheader("📊 Resultados")
            
            # Determinar emoji y color según sentimiento
            sentiment_info = {
                'Positive': {'emoji': '😊', 'color': '#D4EDDA', 'border': '#C3E6CB'},
                'Very Positive': {'emoji': '🤩', 'color': '#D4EDDA', 'border': '#C3E6CB'},
                'Negative': {'emoji': '😞', 'color': '#F8D7DA', 'border': '#F5C6CB'},
                'Very Negative': {'emoji': '😡', 'color': '#F8D7DA', 'border': '#F5C6CB'},
                'Neutral': {'emoji': '😐', 'color': '#D1ECF1', 'border': '#BEE5EB'}
            }
            
            info = sentiment_info.get(result['label'], sentiment_info.get('Neutral', {'emoji': '🤔', 'color': '#D1ECF1', 'border': '#BEE5EB'}))
            
            # Caja de resultado principal
            st.markdown(f"""
                <div style="
                    background-color: {info['color']}; 
                    border-left: 5px solid {info['border']};
                    padding: 1.5rem;
                    border-radius: 10px;
                    margin: 1rem 0;
                ">
                    <h2 style="margin: 0; color: #333;">
                        {info['emoji']} Sentimiento: <strong>{result['label']}</strong>
                    </h2>
                    <p style="margin: 0.5rem 0 0 0; font-size: 1.2rem; color: #555;">
                        Confianza: <strong>{result['score']:.2%}</strong>
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            # Gráfico de visualización
            if show_chart:
                st.plotly_chart(
                    create_sentiment_chart(result['label'], result['score']),
                    use_container_width=True
                )
            
            # Datos técnicos
            if show_raw:
                with st.expander("🔧 Datos técnicos"):
                    st.json(result)
            
            # Interpretación
            with st.expander("💡 Interpretación"):
                confidence = result['score']
                if confidence > 0.8:
                    interpretation = "Alta confianza - El modelo está muy seguro de su predicción."
                elif confidence > 0.6:
                    interpretation = "Confianza moderada - El modelo tiene buena certeza."
                else:
                    interpretation = "Baja confianza - El sentimiento podría ser ambiguo."
                
                st.info(interpretation)
                
                st.markdown("""
                **Sobre el análisis:**
                - El modelo analiza el tono emocional del texto
                - Un score más alto indica mayor confianza
                - Los textos pueden tener matices que afecten la clasificación
                """)
    
    # Footer
    st.divider()
    st.markdown("""
        <div style="text-align: center; color: #666; padding: 1rem;">
            <p>Desarrollado con ❤️ usando Streamlit y Hugging Face Transformers</p>
            <p>Modelo: <a href="https://huggingface.co/tabularisai/multilingual-sentiment-analysis" target="_blank">
                tabularisai/multilingual-sentiment-analysis
            </a></p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
