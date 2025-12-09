# 🎭 Análisis de Sentimientos Multilingüe

Aplicación web interactiva para análisis de sentimientos en múltiples idiomas, impulsada por el modelo [tabularisai/multilingual-sentiment-analysis](https://huggingface.co/tabularisai/multilingual-sentiment-analysis) de Hugging Face.

## ✨ Características

- 🌍 **Soporte multilingüe**: Analiza textos en español, inglés, francés, alemán y más
- 🎨 **Interfaz intuitiva**: Diseño limpio y fácil de usar con Streamlit
- 📊 **Visualización de resultados**: Gráficos interactivos con Plotly
- ⚡ **Análisis en tiempo real**: Resultados instantáneos
- 🎯 **Alta precisión**: Utiliza modelos de última generación

## 📋 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- 2GB de RAM mínimo (4GB recomendado)

## 🔧 Instalación

### 1. Clonar el repositorio
```bash
git clone [https://github.com/tu-usuario/multilingual-sentiment-analysis.git
cd multilingual-sentiment-analysis](https://github.com/jumartinezva-star/Proyecto-final.git)
```

### 2. Crear entorno virtual (recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## 💻 Uso

### Ejecutar la aplicación localmente
```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

### Uso básico

1. **Ingresa un texto** en el área de texto
2. **Haz clic** en "Analizar Sentimiento"
3. **Visualiza** los resultados con el sentimiento detectado y el nivel de confianza

## 📁 Estructura del Proyecto
```
multilingual-sentiment-analysis/
│
├── app.py                          # Aplicación principal de Streamlit
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Documentación
├── .gitignore                      # Archivos a ignorar por Git
│
├── model/
│   └── sentiment_analyzer.py      # Clase del analizador de sentimientos
│
├── utils/
│   └── helpers.py                 # Funciones auxiliares
│
└── .streamlit/
    └── config.toml                # Configuración de Streamlit
```

## 🧠 Modelo

Esta aplicación utiliza el modelo **tabularisai/multilingual-sentiment-analysis** de Hugging Face:

- **Arquitectura**: BERT multilingüe
- **Entrenamiento**: Dataset de sentimientos en múltiples idiomas
- **Categorías**: Positivo, Negativo, Neutral
- **Idiomas soportados**: 100+ idiomas

## 📊 Ejemplos de Resultados

| Texto | Sentimiento | Confianza |
|-------|-------------|-----------|
| "¡Increíble! Me encanta" | Positivo | 99.2% |
| "Terrible experiencia" | Negativo | 97.8% |
| "El producto llegó a tiempo" | Neutral | 85.4% |

## 🛠️ Tecnologías Utilizadas

- **Streamlit**: Framework para aplicaciones web
- **Transformers**: Biblioteca de Hugging Face
- **PyTorch**: Framework de deep learning
- **Plotly**: Visualización de datos

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor abre un issue o pull request.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

## 🙏 Agradecimientos

- [Hugging Face](https://huggingface.co/) por el modelo
- [Streamlit](https://streamlit.io/) por el framework
- [Tabularisai](https://huggingface.co/tabularisai) por entrenar el modelo

---

**Hecho con ❤️ usando Streamlit y Hugging Face**
