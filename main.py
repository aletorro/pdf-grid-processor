from pdf2image import convert_from_path
from PIL import Image, ImageDraw
import os
import math


def procesar_carpeta_pdf(carpeta_origen, archivo_salida, filas=2, columnas=2):
    # Configuración de página Carta a 300 DPI
    ANCHO_CARTA, ALTO_CARTA = 2550, 3300
    ANCHO_CUAD = ANCHO_CARTA // columnas
    ALTO_CUAD = ALTO_CARTA // filas
    PATH_POPPLER = r"C:\poppler\Library\bin"

    # Obtener lista de PDFs en la carpeta
    archivos = [os.path.join(carpeta_origen, f) for f in os.listdir(carpeta_origen) if f.lower().endswith('.pdf')]
    archivos.sort()  # Ordenar alfabéticamente

    if not archivos:
        print("No se encontraron archivos PDF en la carpeta.")
        return

    paginas_finales = []
    num_por_pagina = filas * columnas
    total_paginas_necesarias = math.ceil(len(archivos) / num_por_pagina)

    for p in range(total_paginas_necesarias):
        # Crear lienzo nuevo para cada página de salida
        lienzo = Image.new('RGB', (ANCHO_CARTA, ALTO_CARTA), (255, 255, 255))
        dibujo = ImageDraw.Draw(lienzo)

        # Seleccionar el grupo de archivos para esta página
        inicio = p * num_por_pagina
        fin = inicio + num_por_pagina
        grupo_archivos = archivos[inicio:fin]

        for idx, ruta in enumerate(grupo_archivos):
            try:
                # Calcular posición en la cuadrícula
                fila_actual = idx // columnas
                col_actual = idx % columnas

                x_base = col_actual * ANCHO_CUAD
                y_base = fila_actual * ALTO_CUAD

                # --- DIBUJAR BORDE DE CORTE ---
                # Dibujamos un rectángulo gris claro alrededor del cuadrante
                dibujo.rectangle(
                    [x_base, y_base, x_base + ANCHO_CUAD, y_base + ALTO_CUAD],
                    outline=(200, 200, 200), width=3
                )

                # Procesar PDF a Imagen
                imgs_pdf = convert_from_path(ruta, dpi=200, poppler_path=PATH_POPPLER)
                img = imgs_pdf[0]

                # Ajustar tamaño (dejando un pequeño margen interno para que el borde no toque el contenido)
                img.thumbnail((ANCHO_CUAD - 40, ALTO_CUAD - 40), Image.Resampling.LANCZOS)

                # Centrar y pegar
                pos_x = x_base + (ANCHO_CUAD - img.width) // 2
                pos_y = y_base + (ALTO_CUAD - img.height) // 2
                lienzo.paste(img, (pos_x, pos_y))

            except Exception as e:
                print(f"Error en {ruta}: {e}")

        paginas_finales.append(lienzo)
        print(f"Página {p + 1} de {total_paginas_necesarias} preparada...")

    # Guardar todo en un solo PDF multi-página
    if paginas_finales:
        paginas_finales[0].save(
            archivo_salida, "PDF", resolution=300.0,
            save_all=True, append_images=paginas_finales[1:]
        )
        print(f"\n✅ ¡LISTO! Se procesaron {len(archivos)} archivos en {len(paginas_finales)} páginas.")


# --- CONFIGURACIÓN DE TU CARPETA ---
# 1. Pon tus 36 PDFs en una carpeta (ej: 'mis_documentos')
# 2. Define cuántos quieres por página (ej: filas=3, columnas=2 para tener 6)
procesar_carpeta_pdf(
    carpeta_origen="C:/PDFs_A_Combinar",
    archivo_salida="Reporte_Masivo_Con_Bordes.pdf",
    filas=2,
    columnas=2
)