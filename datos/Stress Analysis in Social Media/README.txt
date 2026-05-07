@'
===========================================================
DATASET: Stress Analysis in Social Media (Dreaddit)
Archivo: dreaddit-train.csv / dreaddit-test.csv
===========================================================

1. DESCRIPCION:
Dreaddit es un conjunto de datos multidominio diseñado para identificar el estres a traves del lenguaje utilizado en comunidades de Reddit. Los datos provienen de cinco categorias de subreddits (anxiety, relationships, ptsd, etc.) y estan etiquetados para indicar si el contenido refleja un estado de estres. Es una herramienta clave para el analisis de comportamiento humano mediante procesamiento de texto.

2. DICCIONARIO DE VARIABLES CLAVE:
* subreddit: Comunidad especifica de origen (ej. anxiety, relationships).
* post_id: Identificador unico de la publicacion de Reddit.
* text: El contenido textual de la publicacion para analizar.
* label: Clasificacion binaria (1 = Indica estres, 0 = No indica estres).
* confidence: Nivel de confianza en la asignacion de la etiqueta de estres.
* social_karma: Puntuacion de aceptacion de la publicacion en la comunidad.
* syntax_ari: Indice de legibilidad (Automated Readability Index) del texto.
* social_timestamp: Marca de tiempo en formato Unix de la publicacion.

3. OBJETIVOS DEL ANALISIS (EDA):
* Identificar que tipos de comunidades de Reddit (subreddits) presentan los niveles mas altos de lenguaje estresante.
* Analizar la relacion entre la complejidad del texto (ARI) y la presencia de etiquetas de estres.
* Investigar si las publicaciones con etiquetas de estres reciben mas o menos interaccion social (karma) por parte de otros usuarios.

4. NOTA TECNICA:
Dataset con alta usabilidad (9.41) ideal para entrenar modelos de clasificacion de texto y realizar analisis de sentimientos profundos sobre la toxicidad y el malestar digital.
'@ | Out-File -FilePath "README_Stress_Analysis.txt" -Encoding utf8