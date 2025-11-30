#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Artículos para Trading desde Cero
Crea artículos HTML optimizados para AdSense y SEO
"""

import os
import sys

# Plantilla HTML base
TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{meta_description}">
    <meta name="keywords" content="{keywords}">
    <title>{title} | Trading desde Cero</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>📈 Trading desde Cero</h1>
            <p class="tagline">Aprende Trading y Forex</p>
            <nav>
                <ul>
                    <li><a href="../index.html">Inicio</a></li>
                    <li><a href="../index.html#forex-basico">Forex Básico</a></li>
                    <li><a href="../index.html#trading">Trading</a></li>
                    <li><a href="../index.html#estrategias">Estrategias</a></li>
                    <li><a href="../index.html#herramientas">Herramientas</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <div class="ad-container"><div class="ad-placeholder">📢 Anuncio AdSense</div></div>

    <main class="container">
        <a href="../index.html" class="back-button">← Volver</a>

        <article>
            <div class="article-header">
                <h1>{h1_title}</h1>
                <p class="article-meta">📅 Enero 2025 | ⏱️ {reading_time} min | 🏷️ {category}</p>
            </div>

            <div class="article-content">
                <h2>Introducción</h2>
                <p>{intro_paragraph}</p>

                <div class="info-box">
                    <strong>💡 Punto Clave:</strong> {key_point}
                </div>

                <h2>{section_1_title}</h2>
                <p>{section_1_content}</p>

                <h3>{subsection_1_title}</h3>
                <p>{subsection_1_content}</p>

                <ul>
                    <li>{bullet_1}</li>
                    <li>{bullet_2}</li>
                    <li>{bullet_3}</li>
                </ul>

                <div class="ad-container"><div class="ad-placeholder">📢 Anuncio AdSense</div></div>

                <h2>{section_2_title}</h2>
                <p>{section_2_content}</p>

                <h3>{subsection_2_title}</h3>
                <p>{subsection_2_content}</p>

                <div class="highlight-box">
                    <strong>💡 Consejo Práctico:</strong> {practical_tip}
                </div>

                <h2>{section_3_title}</h2>
                <p>{section_3_content}</p>

                <div class="warning-box">
                    <strong>⚠️ Advertencia:</strong> {warning_message}
                </div>

                <div class="ad-container"><div class="ad-placeholder">📢 Anuncio AdSense</div></div>

                <h2>Conclusión</h2>
                <p>{conclusion}</p>

                <div class="info-box">
                    <strong>📚 Continúa Aprendiendo:</strong>
                    <ul>
                        <li><a href="{related_1}.html">{related_1_title}</a></li>
                        <li><a href="{related_2}.html">{related_2_title}</a></li>
                        <li><a href="../index.html">Volver al Inicio</a></li>
                    </ul>
                </div>
            </div>
        </article>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2025 Trading desde Cero</p>
            <p><small>⚠️ El trading implica riesgo</small></p>
        </div>
    </footer>
</body>
</html>
"""

# Ejemplos de artículos predefinidos
ARTICULOS_PREDEFINIDOS = {
    "rsi-indice-fuerza-relativa": {
        "meta_description": "RSI (Índice de Fuerza Relativa): Guía completa para usar este indicador en trading. Aprende a identificar sobrecompra, sobreventa y divergencias.",
        "keywords": "RSI, índice fuerza relativa, indicador RSI, sobrecompra sobreventa, RSI trading",
        "title": "RSI (Índice de Fuerza Relativa): Guía Completa",
        "h1_title": "RSI: Guía Completa del Índice de Fuerza Relativa",
        "reading_time": "10",
        "category": "Indicadores",
        "intro_paragraph": "El RSI (Relative Strength Index o Índice de Fuerza Relativa) es uno de los indicadores técnicos más populares en trading. Desarrollado por J. Welles Wilder en 1978, el RSI mide la velocidad y el cambio de los movimientos de precio para identificar condiciones de sobrecompra o sobreventa.",
        "key_point": "El RSI oscila entre 0 y 100. Valores superiores a 70 indican sobrecompra, mientras que valores inferiores a 30 indican sobreventa.",
        "section_1_title": "¿Qué es el RSI y Cómo se Calcula?",
        "section_1_content": "El RSI es un oscilador de momentum que compara la magnitud de las ganancias recientes con las pérdidas recientes para determinar si un activo está sobrecomprado o sobrevendido.",
        "subsection_1_title": "Fórmula del RSI",
        "subsection_1_content": "RSI = 100 - (100 / (1 + RS)), donde RS = Promedio de ganancias / Promedio de pérdidas en el período (típicamente 14 períodos).",
        "bullet_1": "RSI > 70: Sobrecompra (posible reversión bajista)",
        "bullet_2": "RSI < 30: Sobreventa (posible reversión alcista)",
        "bullet_3": "RSI 50: Zona neutral, momentum equilibrado",
        "section_2_title": "Cómo Usar el RSI en Trading",
        "section_2_content": "Existen varias estrategias para usar el RSI efectivamente en tus operaciones.",
        "subsection_2_title": "Estrategia 1: Sobrecompra/Sobreventa",
        "subsection_2_content": "Cuando el RSI supera 70, considera vender o cerrar posiciones largas. Cuando cae por debajo de 30, considera comprar.",
        "practical_tip": "No operes solo basándote en RSI. Combínalo con análisis de soporte/resistencia y otros indicadores como MACD o medias móviles.",
        "section_3_title": "Divergencias del RSI",
        "section_3_content": "Las divergencias ocurren cuando el precio y el RSI se mueven en direcciones opuestas, señalando posibles reversiones de tendencia.",
        "warning_message": "En tendencias fuertes, el RSI puede permanecer en zona de sobrecompra (>70) o sobreventa (<30) durante períodos prolongados. No asumas automáticamente una reversión.",
        "conclusion": "El RSI es una herramienta poderosa para identificar momentum y posibles reversiones, pero debe usarse en combinación con otros indicadores y análisis de contexto de mercado para maximizar su efectividad.",
        "related_1": "macd-indicador",
        "related_1_title": "MACD: Cómo Interpretar este Indicador",
        "related_2": "medias-moviles",
        "related_2_title": "Medias Móviles: Simples vs Exponenciales"
    },

    "apalancamiento-forex": {
        "meta_description": "Apalancamiento en Forex: Qué es, cómo funciona, ventajas y riesgos. Aprende a usar el apalancamiento de forma segura para maximizar tus ganancias.",
        "keywords": "apalancamiento forex, leverage trading, apalancamiento 1:100, riesgo apalancamiento",
        "title": "¿Qué es el Apalancamiento en Forex?",
        "h1_title": "Apalancamiento en Forex: Guía Completa",
        "reading_time": "9",
        "category": "Herramientas",
        "intro_paragraph": "El apalancamiento es una de las características más atractivas y peligrosas del trading de Forex. Te permite controlar posiciones grandes con una cantidad relativamente pequeña de capital, multiplicando tanto tus ganancias potenciales como tus pérdidas.",
        "key_point": "Con apalancamiento 1:100, puedes controlar $100,000 con solo $1,000 de capital. Esto amplifica tus ganancias... y tus pérdidas.",
        "section_1_title": "¿Cómo Funciona el Apalancamiento?",
        "section_1_content": "El apalancamiento es esencialmente un 'préstamo' que tu broker te otorga para operar con posiciones más grandes de las que tu capital permitiría normalmente.",
        "subsection_1_title": "Ejemplo Práctico",
        "subsection_1_content": "Quieres operar 1 lote estándar de EUR/USD ($100,000). Con apalancamiento 1:100, solo necesitas $1,000 como margen. El broker 'presta' los otros $99,000.",
        "bullet_1": "Apalancamiento 1:10 = Puedes controlar 10x tu capital",
        "bullet_2": "Apalancamiento 1:50 = Puedes controlar 50x tu capital",
        "bullet_3": "Apalancamiento 1:500 = Puedes controlar 500x tu capital (muy arriesgado)",
        "section_2_title": "Ventajas del Apalancamiento",
        "section_2_content": "El apalancamiento tiene beneficios claros cuando se usa correctamente.",
        "subsection_2_title": "Maximizar Oportunidades",
        "subsection_2_content": "Puedes participar en el mercado con capital limitado. Un movimiento de 1% con apalancamiento 1:100 resulta en 100% de ganancia sobre tu margen.",
        "practical_tip": "Para principiantes, usa apalancamiento bajo (1:10 o 1:20 máximo). Nunca uses más de 1:100, incluso con experiencia.",
        "section_3_title": "Riesgos del Apalancamiento",
        "section_3_content": "El apalancamiento amplifica pérdidas igual que ganancias. Muchos traders novatos pierden todo su capital por usar apalancamiento excesivo.",
        "warning_message": "Con apalancamiento 1:100, un movimiento de 1% contra ti elimina el 100% de tu margen. Puedes perder tu cuenta en minutos.",
        "conclusion": "El apalancamiento es una herramienta poderosa pero peligrosa. Úsalo con precaución, siempre con stop loss, y nunca arriesgues más del 1-2% de tu capital por operación.",
        "related_1": "stop-loss-proteger-capital",
        "related_1_title": "Stop Loss: Cómo Proteger tu Capital",
        "related_2": "margen-margen-libre",
        "related_2_title": "Margen y Margen Libre: Diferencias"
    }
}

def generar_articulo(slug, datos=None):
    """
    Genera un artículo HTML a partir de un slug y datos
    """
    if datos is None and slug in ARTICULOS_PREDEFINIDOS:
        datos = ARTICULOS_PREDEFINIDOS[slug]
    elif datos is None:
        print(f"❌ No hay datos predefinidos para '{slug}'")
        print("Proporciona los datos manualmente o elige uno de los predefinidos:")
        print(", ".join(ARTICULOS_PREDEFINIDOS.keys()))
        return False

    # Generar HTML
    html = TEMPLATE.format(**datos)

    # Guardar archivo
    ruta_articulos = "articulos"
    if not os.path.exists(ruta_articulos):
        os.makedirs(ruta_articulos)

    ruta_archivo = os.path.join(ruta_articulos, f"{slug}.html")

    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Artículo creado: {ruta_archivo}")
    return True

def listar_predefinidos():
    """Lista todos los artículos predefinidos disponibles"""
    print("\n📚 Artículos Predefinidos Disponibles:\n")
    for i, slug in enumerate(ARTICULOS_PREDEFINIDOS.keys(), 1):
        datos = ARTICULOS_PREDEFINIDOS[slug]
        print(f"{i}. {slug}")
        print(f"   Título: {datos['title']}")
        print(f"   Categoría: {datos['category']}\n")

def generar_todos():
    """Genera todos los artículos predefinidos"""
    print("🚀 Generando todos los artículos predefinidos...\n")
    for slug in ARTICULOS_PREDEFINIDOS.keys():
        generar_articulo(slug)
    print(f"\n✅ {len(ARTICULOS_PREDEFINIDOS)} artículos generados exitosamente!")

if __name__ == "__main__":
    print("=" * 60)
    print("  GENERADOR DE ARTÍCULOS - TRADING DESDE CERO")
    print("=" * 60)

    if len(sys.argv) > 1:
        comando = sys.argv[1]

        if comando == "--listar" or comando == "-l":
            listar_predefinidos()
        elif comando == "--todos" or comando == "-t":
            generar_todos()
        elif comando == "--ayuda" or comando == "-h":
            print("""
Uso: python generar-articulo.py [OPCION]

Opciones:
  --listar, -l      Lista artículos predefinidos disponibles
  --todos, -t       Genera todos los artículos predefinidos
  --ayuda, -h       Muestra esta ayuda
  <slug>            Genera un artículo específico por su slug

Ejemplos:
  python generar-articulo.py --listar
  python generar-articulo.py --todos
  python generar-articulo.py rsi-indice-fuerza-relativa
            """)
        else:
            # Generar artículo específico
            slug = comando
            generar_articulo(slug)
    else:
        print("\n🎯 Modo Interactivo\n")
        print("1. Generar todos los artículos predefinidos")
        print("2. Listar artículos predefinidos")
        print("3. Generar artículo específico")
        print("4. Salir\n")

        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            generar_todos()
        elif opcion == "2":
            listar_predefinidos()
        elif opcion == "3":
            listar_predefinidos()
            slug = input("\nIngresa el slug del artículo: ").strip()
            generar_articulo(slug)
        elif opcion == "4":
            print("👋 ¡Hasta luego!")
        else:
            print("❌ Opción inválida")
