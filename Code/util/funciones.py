import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns



# FUNCION QUE RECIBE POR PARAMETRO LA LISTA CON LAS COLUMNAS QUE HAY QUE ELIMINAR

def drop_columns (lista, info):
    for a in range(len(lista)):
        for i in info.columns: 
            if i:
                if re.findall(lista[a], i):
                    info.drop(columns= i, axis=1, inplace= True)
                else:
                    continue
    return info


# FUNCION QUE RECIBE EL DATA FRAME CON LAS COLUMNAS QUE DEBE CAMBIAR Y EL DICCIONARIO CON LOS VALORES NUEVOS QUE HAY QUE FIJAR
    
def cambio_respuestas (info,dicc):
    for a in range(info.iloc[ : , :42].shape[1]):
        info.iloc[: ,a] = info.iloc[: ,a].map(dicc)
    return info



# FUNCION QUE RECIBE POR PARAMETRO LA LISTA DE LAS NUEVAS COLUMNAS Y EL DATAFRAME DONDE TIENE QUE GENERARLAS (DEPRESION, ANSIEDAD O ESTRES)

def insert_column (lista, info):
    for a in range(len(lista)):
        info[lista[a]] = np.nan
    
    return info


# FUNCION QUE PONDERA LAS COLUMNAS INSERTADAS CON LA FUNCION ANTERIOR Y LES DA EL VALOR DE LA SUMA QUE CORRESPONDE A SU CATEGORIA (DEPRESION, ANSIEDAD O ESTRES)

def ponderacion (dicc, info):
    for a in dicc.keys():
       info[a] = info[dicc[a]].sum(axis=1)   
    return info


# FUNCION QUE RECIBE POR PARAMETRO UNA COLUMNA DEL DATAFRAME (EDAD) PARA QUE LA CATEGROICE EN FUNCION DE LAS CASUISTICAS INDICADAS EN LA MISMA FUNCION     
    
def categorizacion_edad(valor):
    if valor<=10:
        return '< 10'
    if  10<=valor<=16:
        return ' 10-16'
    if 17<=valor<=21:
        return '17-21'
    if 22<=valor<=35:
        return '22-35'
    if 36<=valor<=48:
        return '36-48'
    if valor>=49:
        return '> 48'


# FUNCION QUE RECIBE POR PARAMETRO UNA COLUMNA DEL DATAFRAME (FAMILIA) PARA QUE LA CATEGROICE EN FUNCION DE LAS CASUISTICAS INDICADAS EN LA MISMA FUNCION 

def categorizacion_familia(valor):
    if valor==2:
        return '<=2'
    if  3<=valor<=5:
        return '3-5 '
    if 6<=valor<=10:
        return '6-10'
    if valor>=11:
        return '>10'

    
# FUNCION QUE RECIBE POR PARAMETRO UNA COLUMNA DEL DATAFRAME (DEPRESSION_CAT) PARA QUE LA CATEGROICE EN FUNCION DE LAS CASUISTICAS INDICADAS EN LA MISMA FUNCION 

def categorizacion_depression (valor):
    if valor <= 9:
        return 'Normal'
    if 10<= valor <=13:
        return 'Mild'
    if 14<=valor <=20:
        return 'Moderate'
    if 21<=valor <=27:
        return 'Severe'
    if valor>28:
        return 'Extremely Severe'

# FUNCION QUE RECIBE POR PARAMETRO UNA COLUMNA DEL DATAFRAME (ANSIETY_CAT) PARA QUE LA CATEGROICE EN FUNCION DE LAS CASUISTICAS INDICADAS EN LA MISMA FUNCION  
    
def categorizacion_anxiety (valor):
    if valor <= 7:
        return 'Normal'
    if 8<=valor <=9:
        return 'Mild'
    if 10<= valor <=14:
        return 'Moderate'
    if 15<= valor <=19:
        return 'Severe'
    if valor>19:
        return 'Extremely Severe'


# FUNCION QUE RECIBE POR PARAMETRO UNA COLUMNA DEL DATAFRAME (STRESS_CAT) PARA QUE LA CATEGROICE EN FUNCION DE LAS CASUISTICAS INDICADAS EN LA MISMA FUNCION 

def categorizacion_stress (valor):
    if valor <= 14:
        return 'Normal'
    if 15 <= valor <=18:
        return 'Mild'
    if 19 <= valor <=25:
        return 'Moderate'
    if 26<=valor <=33:
        return 'Severe'
    if valor>=34:
        return 'Extremely Severe'
    


# FUNCION  PARA CREAR GRAFICO Y QUE RECIBE POR PARAMETRO EL DATAFRAME, UNA COLUMNA DEL DATAFRAME, OTRA COLUMNA MAS DEL DATAFRAME PARA UTILIZARLA EN EL HUE Y EL TITULO DEL GRAFICO     
  
def graficos_analisis (info, valor, valor2, valor3, color_target,color):
    
   

    if valor2 == 'Target':
        plt.legend(['0','1'])
        sns.set(font_scale = 1.3)
        sns.countplot(info[valor],hue=info[valor2],palette= color_target)
    else:
        sns.set(font_scale = 1.3)
        sns.countplot(info[valor],hue=info[valor2],palette= color)
        plt.legend(['Normal','Mild','Moderate','Severe','Extremly Severe'])
    plt.xlabel('')
    plt.title(valor3,fontsize=17)
    plt.xticks(rotation=16)    


# FUNCION PARA CREAR GRAFICO QUE RECIBE POR PARAMETRO LAS MATRICES DE CONFUSION Y EL TITULO DEL GRAFICO 


def graficos_conf_matrix (info,valor1):
    
    sns.heatmap(info/np.sum(info), annot=True, 
            fmt='.2%', cmap='YlGn');
    plt.title(valor1,fontsize=15)