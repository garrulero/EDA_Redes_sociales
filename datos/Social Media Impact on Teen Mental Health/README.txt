@'
===========================================================
DATASET: Social Media vs Productivity
Archivo: Social_Media_Usage_and_Productivity.csv
===========================================================

1. DESCRIPCION:
Este dataset analiza la relación entre el tiempo invertido en redes sociales y la perdida de productividad reportada por los usuarios. Es clave para entender si el uso de las plataformas es recreativo o una distracción que afecta el rendimiento diario.

2. DICCIONARIO DE VARIABLES CLAVE:
* User_ID: Identificador unico del usuario.
* Daily_Usage_Time: Tiempo total diario en redes (minutos/horas).
* Productivity_Loss: Escala o porcentaje de perdida de productividad.
* Platform: Red social principal utilizada.
* User_Category: Segmentacion del usuario (estudiante, profesional, etc.).

3. OBJETIVOS DEL ANALISIS (EDA):
* Investigar si existe una correlacion lineal entre el tiempo de uso y la caida de productividad.
* Identificar que plataformas (ej. Facebook vs LinkedIn) generan mayor "perdida de tiempo" segun el perfil del usuario.
* Validar la hipotesis del "millennial cuñado": ¿Los profesionales de mediana edad pierden mas tiempo en redes de lo que admiten?

4. NOTA TECNICA:
Datos fundamentales para cruzar con los niveles de estres y ver si la baja productividad es causa o consecuencia del malestar digital.
'@ | Out-File -FilePath "README_Productivity.txt" -Encoding utf8
Link:https://www.kaggle.com/datasets/algozee/teenager-menthal-healy