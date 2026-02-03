# PDF Grid Processor (N-up with Cut Guides)

Este script de Python permite combinar múltiples archivos PDF en una sola página tamaño Carta, organizándolos en una cuadrícula personalizable (2x2, 3x2, 6 por página, etc.). Es ideal para optimizar la impresión de credenciales, carnets de seguros o reportes médicos.

## 🚀 Características
* **Aplanamiento por Imagen**: Convierte cada PDF a imagen para eliminar errores de capas, metadatos y traslapes de texto.
* **Guías de Corte**: Genera bordes automáticos (gris tenue) que facilitan el recorte y doblado manual preciso.
* **Procesamiento Masivo**: Capacidad de escanear carpetas completas y generar automáticamente múltiples páginas de salida.
  
### Requisitos
* Python 3.x
* Bibliotecas: `pdf2image`, `Pillow`
* **Poppler**: Necesario para la conversión de PDF a imagen en Windows.

### Instalación y Uso
1. Instala las dependencias: `pip install pdf2image pillow`
2. Descarga los binarios de Poppler y ajusta la ruta `PATH_POPPLER` en el código.
3. Ejecuta el script apuntando a tu carpeta de documentos.


## 🛠️ Requisitos e Instalación DETALLADOS

### 1. Dependencias de Python
Asegúrate de tener Python instalado y ejecuta el siguiente comando en tu terminal para instalar las librerías necesarias:
`pip install pdf2image pillow`

### 2. Configuración de Poppler (Windows)
Para que la conversión de PDF a imagen funcione, el script requiere los binarios de Poppler.
Descarga los binarios de Poppler para Windows. (https://github.com/oschwartz10612/poppler-windows/releases/)
Descomprime la carpeta en una ubicación conocida (ej. C:\poppler).
El script está configurado para buscar los ejecutables en la ruta:
C:\poppler\Library\bin (donde se encuentran pdftocairo.exe, pdfinfo.exe, etc.).

### 📝 Uso del Script
Simplemente apunta el script a tu carpeta de origen y define la distribución:

procesar_carpeta_pdf(
    carpeta_origen = "RUTA_DE_TUS_PDFS", 
    archivo_salida = "Resultado_Final.pdf",
    filas = 3, 
    columnas = 2
)

### 📂 Contexto del Proyecto
Este proyecto nació de la necesidad de consolidar múltiples documentos PDF de aseguradoras (como Aetna y GNP) que presentaban dificultades técnicas al ser combinados mediante métodos vectoriales tradicionales. Los archivos originales contenían capas y coordenadas de visualización que causaban traslapes de información. La solución mediante "renderizado de imagen" garantiza que el resultado final sea visualmente idéntico al original, permitiendo una distribución limpia para impresión y archivo.

### 🤝 Créditos
Desarrollador: Alexander Torres Rodríguez
Librerías: Basado en pdf2image (wrapper de Poppler) y Pillow (PIL Fork).

#### Nota: Este script fue probado con éxito procesando reportes de seguros médicos internacionales, garantizando la legibilidad de textos pequeños y logotipos corporativos.
