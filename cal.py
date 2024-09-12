import pandas as pd
import numpy as np

# Cargar el CSV en un DataFrame
df = pd.read_csv('tips.csv')

# 1. Revisar la existencia de valores nulos
def check_nulls(df):
    nulls = df.isnull().sum()
    print("Valores nulos en cada columna:")
    print(nulls[nulls > 0])

# 2. Verificar el tipo de datos de cada columna
def check_dtypes(df):
    print("\nTipos de datos en cada columna:")
    print(df.dtypes)

# 3. Detectar valores fuera de rango esperados
def check_ranges(df):
    # "Total bill" y "tip" deben ser positivos
    if not (df['total_bill'] >= 0).all():
        print("Valores negativos en 'total_bill'")
    if not (df['tip'] >= 0).all():
        print("Valores negativos en 'tip'")

    # "Size" debe ser un entero positivo
    if not (df['size'] > 0).all():
        print("Valores no positivos en 'size'")

# 4. Comprobar valores duplicados
def check_duplicates(df):
    duplicates = df.duplicated().sum()
    print(f"\nNúmero de filas duplicadas: {duplicates}")

# Ejecutar las funciones de chequeo
check_nulls(df)
check_dtypes(df)
check_ranges(df)
check_duplicates(df)
