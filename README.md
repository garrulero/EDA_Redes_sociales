# Informe EDA: Redes Sociales y Generaciones

## Objetivo

Evaluar si la edad es verdaderamente determinante en la relación de los usuarios con las plataformas digitales, analizando métricas de productividad, estrés, ansiedad y toxicidad.

Este proyecto está automatizado mediante un script en Python que procesa los datos y genera las visualizaciones clave de manera dinámica.

---

## Estructura del Proyecto

```text
/
├── datos/
│   └── Social Media vs Productivity/
│       └── social_media_vs_productivity.csv   # Dataset original
├── codigo/
│   └── main.py                                # Script principal de automatización
├── graficas/                                  # Carpeta generada automáticamente con los resultados
└── README.md
```

---

## Cómo ejecutar el proyecto

Para ejecutar el análisis automatizado y generar todas las gráficas, asegúrate de tener instaladas las dependencias y ejecuta el siguiente comando desde la raíz del proyecto:

```bash
python codigo/main.py
```

Al finalizar, todas las visualizaciones se guardarán automáticamente en formato `.png` dentro de la carpeta `graficas/`.

---

## Hipótesis Iniciales

- **Gen Z/Alfa:** ¿A pesar de ser nativos digitales, su uso intensivo les genera niveles más altos de ansiedad y disrupciones de sueño que a los adultos?
- **Millennials y Boomers:** ¿Experimentan una dependencia distinta y afirman no tener las consecuencias negativas de los jóvenes?
- **Toxicidad Digital:** ¿La forma en que se manifiesta el estrés depende de la generación y la plataforma elegida?

---

## Hallazgos Clave

### 1. El Estrés es Transversal (Derribando el mito generacional)

Los datos demuestran que la generación (edad) no es un factor determinante para los niveles de estrés.

Las diferencias promedio de estrés entre generaciones son estadísticamente insignificantes (una variación máxima de apenas 0.07 puntos en una escala de 0 a 10).

De igual manera, el tiempo de uso y las horas de sueño mantienen promedios muy similares sin importar el año de nacimiento.

**Conclusión:** El malestar digital es una problemática generalizada y multicausal, no una cuestión de brecha de edad. *(Refuta Hipótesis 1 y 2).*

---

### 2. El Bienestar Digital como factor protector real

La matriz de correlación nos indicó que el estrés no se explica de forma lineal por la edad, sino por los hábitos.

El uso activo de herramientas de Bienestar Digital redujo el estrés promedio de `5.54` a `5.42`.

Aunque la diferencia numérica parece sutil, es el doble de grande que cualquier diferencia generacional encontrada.

**Conclusión:** La gestión activa de la herramienta es mucho más efectiva para cuidar la salud mental que el simple hecho de pertenecer a una generación u otra.

---

### 3. La Gen Z y el estrés en plataformas no nativas (Facebook vs TikTok)

Al cruzar los niveles de estrés por plataforma y generación, descubrimos un patrón inesperado:

Para los más jóvenes (Gen Z / Alfa), Facebook (`5.71`) resulta ser una plataforma más estresante que TikTok (`5.65`).

**Conclusión:** La "toxicidad" no depende solo del algoritmo de moda, sino de cómo interactúa el usuario con redes para las que quizás no son el público objetivo o donde ocurren dinámicas familiares/sociales distintas. *(Valida Hipótesis 3).*

---

## Tecnologías Utilizadas

- Python 3.12
- Pandas *(Limpieza y manipulación de datos)*
- NumPy *(Operaciones numéricas)*
- Matplotlib & Seaborn *(Visualización de datos y exportación de gráficas)*
