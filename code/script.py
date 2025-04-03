import pandas as pd

def cargar(ruta):
    df = pd.read_csv(ruta, sep=";")
    return df

def pasa_datetime(df, columna):
    df[columna] = pd.to_datetime(df[columna])
    df["year"] = df[columna].dt.year
    return df

if __name__ == "__main__":
    ruta = r"C:\Users\dpine\examen_nacho\data\datos_mock.csv"
    
    df = cargar(ruta)
    df = pasa_datetime(df, "dt")
    
    print(df.head())