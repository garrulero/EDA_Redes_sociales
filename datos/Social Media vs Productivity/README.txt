@'
===========================================================
DATASET: Social Media vs Productivity
Archivo: social_media_vs_productivity.csv
===========================================================

1. DESCRIPCION:
Este dataset contiene 30,000 registros que simulan patrones de comportamiento real para explorar como los habitos digitales diarios (redes sociales, notificaciones y tiempo de pantalla) se relacionan con la productividad, el estres y el bienestar individual. Es ideal para practicar limpieza de datos, ya que incluye valores nulos (NaN) y valores atipicos (outliers) de forma intencionada.

2. DICCIONARIO DE VARIABLES CLAVE:
* age: Edad del individuo (18-65 años).
* gender: Identidad de genero (Male, Female, Other).
* job_type: Sector laboral o estatus (IT, Educacion, Estudiante, etc.).
* daily_social_media_time: Tiempo promedio diario en redes sociales (horas).
* social_platform_preference: Plataforma mas utilizada (Instagram, TikTok, etc.).
* perceived_productivity_score: Productividad autocalificada (escala 0-10).
* actual_productivity_score: Puntuacion de productividad real simulada (escala 0-10).
* stress_level: Nivel de estres actual (escala 1-10).
* days_feeling_burnout_per_month: Dias de agotamiento reportados al mes.
* weekly_offline_hours: Horas totales pasadas desconectado a la semana.

3. OBJETIVOS DEL ANALISIS (EDA):
* Analizar la correlacion entre el tiempo de uso de redes sociales y los niveles de estres y burnout.
* Comparar la brecha entre la productividad percibida por el usuario y su productividad real segun su edad y profesion.
* Investigar si el uso de aplicaciones de enfoque (focus apps) o funciones de bienestar digital realmente mitigan la perdida de productividad.

4. NOTA TECNICA:
Dataset de alta usabilidad (10.0) diseñado para flujos de trabajo de Machine Learning, permitiendo realizar tareas de regresion, clasificacion y deteccion de multicolinealidad entre sus caracteristicas.
'@ | Out-File -FilePath "README_Productivity.txt" -Encoding utf8
LINK:https://www.kaggle.com/datasets/mahdimashayekhi/social-media-vs-productivity