# PDF Grid Processor (N-up with Cut Guides)

Este script de Python permite combinar múltiples archivos PDF en una sola página tamaño Carta, organizándolos en una cuadrícula personalizable (2x2, 3x2, etc.). 

### Características principales
* **Aplanamiento por Imagen**: Convierte cada PDF a imagen para evitar traslapes de capas y errores de coordenadas técnicas.
* **Guías de Corte**: Añade bordes automáticos configurables para facilitar el recorte y doblado manual.
* **Procesamiento Masivo**: Escanea carpetas completas y genera automáticamente todas las páginas necesarias.

### Requisitos
* Python 3.x
* Bibliotecas: `pdf2image`, `Pillow`
* **Poppler**: Necesario para la conversión de PDF a imagen en Windows.

### Instalación y Uso
1. Instala las dependencias: `pip install pdf2image pillow`
2. Descarga los binarios de Poppler y ajusta la ruta `PATH_POPPLER` en el código.
3. Ejecuta el script apuntando a tu carpeta de documentos.
