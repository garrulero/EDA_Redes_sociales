import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    print("Iniciando la automatización del EDA...")

    # --- 1. CONFIGURACIÓN DE RUTAS ---
    # Detectar el directorio donde está este script (carpeta 'codigo')
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # El directorio raíz será un nivel arriba
    ROOT_DIR = os.path.dirname(BASE_DIR)
    
    # Definir rutas relativas a la raíz
    DATA_PATH = os.path.join(ROOT_DIR, 'datos', 'Social Media vs Productivity', 'social_media_vs_productivity.csv')
    GRAFICAS_DIR = os.path.join(ROOT_DIR, 'graficas')

    # Crear la carpeta 'graficas' si no existe
    os.makedirs(GRAFICAS_DIR, exist_ok=True)
    print(f"Carpeta de destino para gráficas validada/creada: {GRAFICAS_DIR}")

    # --- 2. IMPORTACIÓN Y LIMPIEZA ---
    print("Cargando y limpiando datos...")
    try:
        smp = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo en {DATA_PATH}")
        return

    # Limpieza de nulos
    smp_limpio = smp.dropna().copy()
    print(f"Datos limpios listos. Registros finales: {len(smp_limpio)}")

    # --- 3. INGENIERÍA DE CARACTERÍSTICAS (FEATURE ENGINEERING) ---
    print("Asignando generaciones...")
    def asignar_generacion(edad):
        if edad <= 26: return 'Gen Z/Alfa'
        elif 27 <= edad <= 42: return 'Millennial'
        elif 43 <= edad <= 58: return 'Gen X'
        else: return 'Boomer'

    smp_limpio['generacion'] = smp_limpio['edad'].apply(asignar_generacion)
    orden_generaciones = ['Gen Z/Alfa', 'Millennial', 'Gen X', 'Boomer']

    # --- 4. GENERACIÓN Y GUARDADO DE GRÁFICAS ---
    print("Generando gráficas...")

    # Gráfico 1: Distribuciones Clave
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    sns.histplot(smp_limpio['edad'], bins=20, kde=True, ax=axes[0], color='#3498db')
    axes[0].set_title('Distribución de Edades')
    axes[0].set_xlabel('Edad')

    sns.histplot(smp_limpio['tiempo_diario_redes_sociales'], bins=20, kde=True, ax=axes[1], color='#e74c3c')
    axes[1].set_title('Tiempo Diario en Redes Sociales')
    axes[1].set_xlabel('Horas al día')

    sns.histplot(smp_limpio['horas_sueno'], bins=20, kde=True, ax=axes[2], color='#2ecc71')
    axes[2].set_title('Distribución de Horas de Sueño')
    axes[2].set_xlabel('Horas de sueño')
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICAS_DIR, '01_distribuciones_clave.png'), dpi=300)
    plt.close()

    # Gráfico 2: Distribución por Generación
    plt.figure(figsize=(10, 5))
    sns.countplot(data=smp_limpio, x='generacion', order=orden_generaciones, hue='generacion', palette='viridis', legend=False)
    plt.title('Distribución de Usuarios por Generación')
    plt.ylabel('Número de usuarios')
    plt.xlabel('Generación')
    plt.savefig(os.path.join(GRAFICAS_DIR, '02_conteo_generaciones.png'), dpi=300)
    plt.close()

    # Gráfico 3: Estrés por Generación
    plt.figure(figsize=(10, 6))
    sns.barplot(data=smp_limpio, x='generacion', y='nivel_estres', order=orden_generaciones, hue='generacion', palette='viridis', errorbar='ci', legend=False)
    plt.title('Nivel Promedio de Estrés por Generación')
    plt.ylabel('Nivel de Estrés (Escala 0-10)')
    plt.ylim(0, 10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig(os.path.join(GRAFICAS_DIR, '03_estres_generaciones.png'), dpi=300)
    plt.close()

    # Gráfico 3B (¡Añadido!): Tiempo de uso y sueño por generación (Para corroborar hipótesis 1 y 2)
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    sns.barplot(data=smp_limpio, x='generacion', y='tiempo_diario_redes_sociales', order=orden_generaciones, hue='generacion', palette='viridis', ax=axes[0], legend=False)
    axes[0].set_title('Tiempo Diario en Redes por Generación')
    axes[0].set_ylabel('Horas al día')
    
    sns.barplot(data=smp_limpio, x='generacion', y='horas_sueno', order=orden_generaciones, hue='generacion', palette='viridis', ax=axes[1], legend=False)
    axes[1].set_title('Horas de Sueño por Generación')
    axes[1].set_ylabel('Horas de sueño')
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICAS_DIR, '03b_tiempo_y_sueno_generaciones.png'), dpi=300)
    plt.close()

    # Gráfico 4: Mapa de Correlación
    corr_matrix = smp_limpio.select_dtypes(include=[np.number]).corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=False, cmap='coolwarm', vmin=-1, vmax=1, center=0, linewidths=.5)
    plt.title('Mapa de Correlación: Variables Digitales y Bienestar')
    plt.savefig(os.path.join(GRAFICAS_DIR, '04_heatmap_correlacion.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # Gráfico 5: Impacto del Bienestar Digital
    medias = smp_limpio.groupby('bienestar_digital_activado')['nivel_estres'].mean()
    media_no = medias[False]
    media_si = medias[True]

    plt.figure(figsize=(7, 6))
    ax = sns.barplot(x=['No activado', 'Activado'], y=[media_no, media_si], hue=['No activado', 'Activado'], palette=['#ff9999', '#66b3ff'], legend=False)

    # Añadir los valores exactos encima de las barras
    for i, v in enumerate([media_no, media_si]):
        ax.text(i, v + 0.2, f'{v:.2f}', ha='center', va='bottom', fontsize=14, fontweight='bold')

    plt.ylim(0, 10)  # Eje ajustado para escala real de 0-10
    plt.title('Impacto del Bienestar Digital en el Estrés', fontsize=14, pad=20)
    plt.ylabel('Nivel Promedio de Estrés (0-10)')
    plt.xlabel('Estado del Bienestar Digital')
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.savefig(os.path.join(GRAFICAS_DIR, '05_impacto_bienestar.png'), dpi=300)
    plt.close()

    # Gráfico 6: Estrés según Plataforma y Generación
    plt.figure(figsize=(12, 6))
    sns.barplot(data=smp_limpio, x='plataforma_preferida', y='nivel_estres', hue='generacion', hue_order=orden_generaciones, palette='magma')
    plt.title('Nivel de Estrés según Plataforma Preferida y Generación')
    plt.ylabel('Estrés Promedio (0-10)')
    plt.xlabel('Plataforma')
    plt.legend(title='Generación', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.ylim(0, 10) # Eje ajustado a escala 0-10
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICAS_DIR, '06_estres_plataforma.png'), dpi=300)
    plt.close()

    print(f"¡Éxito! El EDA se ha ejecutado y todas las gráficas se guardaron en la carpeta: '{GRAFICAS_DIR}'")

if __name__ == "__main__":
    main()