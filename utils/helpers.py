import streamlit as st
from typing import Dict

def get_sentiment_emoji(sentiment: str) -> str:
    """Retorna emoji según el sentimiento"""
    emojis = {
        'Positive': '😊',
        'Negative': '😞',
        'Neutral': '😐'
    }
    return emojis.get(sentiment, '🤔')

def get_sentiment_color(sentiment: str) -> Dict[str, str]:
    """Retorna colores según el sentimiento"""
    colors = {
        'Positive': {'bg': '#D4EDDA', 'border': '#C3E6CB', 'text': '#155724'},
        'Negative': {'bg': '#F8D7DA', 'border': '#F5C6CB', 'text': '#721C24'},
        'Neutral': {'bg': '#D1ECF1', 'border': '#BEE5EB', 'text': '#0C5460'}
    }
    return colors.get(sentiment, colors['Neutral'])

def interpret_confidence(score: float) -> str:
    """Interpreta el nivel de confianza"""
    if score > 0.9:
        return "Muy alta confianza"
    elif score > 0.8:
        return "Alta confianza"
    elif score > 0.6:
        return "Confianza moderada"
    elif score > 0.4:
        return "Baja confianza"
    else:
        return "Muy baja confianza"

def format_percentage(value: float) -> str:
    """Formatea un valor como porcentaje"""
    return f"{value:.2%}"