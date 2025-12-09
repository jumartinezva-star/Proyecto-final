from transformers import pipeline
from typing import Dict, List

class SentimentAnalyzer:
    """Clase para manejar el análisis de sentimientos"""
    
    def __init__(self, model_name: str = "tabularisai/multilingual-sentiment-analysis"):
        """
        Inicializa el analizador de sentimientos
        
        Args:
            model_name: Nombre del modelo de Hugging Face
        """
        self.model_name = model_name
        self.pipe = None
    
    def load_model(self):
        """Carga el modelo de análisis de sentimientos"""
        if self.pipe is None:
            self.pipe = pipeline("text-classification", model=self.model_name)
        return self.pipe
    
    def analyze(self, text: str) -> Dict:
        """
        Analiza el sentimiento de un texto
        
        Args:
            text: Texto a analizar
            
        Returns:
            Diccionario con label y score
        """
        if self.pipe is None:
            self.load_model()
        
        result = self.pipe(text)
        return result[0]
    
    def analyze_batch(self, texts: List[str]) -> List[Dict]:
        """
        Analiza múltiples textos
        
        Args:
            texts: Lista de textos a analizar
            
        Returns:
            Lista de resultados
        """
        if self.pipe is None:
            self.load_model()
        
        results = self.pipe(texts)
        return results