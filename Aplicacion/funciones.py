import pandas as pd

def agrupar_ventas_mensuales(df):
    df_mensual = df.groupby(pd.Grouper(key='Fecha', freq='M')).sum()
    return df_mensual


def ventas_anuales(df, helado):
    return df[helado].sum()


def ventas_ordenadas_por_fecha(df, fecha):
    if df.index is None:
        df_ordenado = df.set_index('Fecha').loc[fecha].sort_values(ascending=False)
        return df_ordenado
    else:
        df_ordenado = df.loc[fecha].sort_values(ascending=False)
        return df_ordenado
