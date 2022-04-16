

# IMPORTAMOS LAS LIBRERIAS NECESARIAS

import os

cwd = os.getcwd()

print (cwd)


direccion = 'C:\\Users\\Laura\\Desktop\\Nueva carpeta\\Code'  #os.path.realpath(__file__)'
os.chdir(direccion)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re



from sys import path
path.append('C:\\Users\\Laura\\Desktop\\Nueva carpeta\\Code\\util')
from funciones import drop_columns, cambio_respuestas, insert_column, ponderacion,categorizacion_anxiety,categorizacion_stress,categorizacion_depression,categorizacion_edad,categorizacion_familia,graficos_analisis
from variables import lista_patron, lista_new_columns, dicc_categorias, dicc_respuestas,lista_orden_colum, dicc_orientacion,dicc_genero,dicc_religion,dicc_raza,dicc_estado,dicc_lugar, colores,color_target


from funciones import graficos_conf_matrix

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score,confusion_matrix,recall_score, f1_score
from sklearn.linear_model import LogisticRegression


from sklearn.pipeline import Pipeline
import pickle





import warnings
warnings.filterwarnings("ignore")



# IMPORTAMOS EL CSV
data = pd.read_csv('Data/Raw/data.csv', sep='\t')


# HACEMOS COPIA DEL MISMO PARA PROCEDER CON LAS TRANSFORMACIONES 


data_transf = data.copy()



# FUNCIONES PARA:
    # ELIMINACION DE COLUMNAS,
    # CAMBIAR LAS RESPUESTAS CON VALORACION DE 0 A 3, 
    # INTERCAR COLUMNAS NUEVAS
    # PODERACION DE LAS COLUMNAS NUEVAS CREADAS

data_transf= drop_columns(lista_patron, data_transf)
data_transf = cambio_respuestas(data_transf,dicc_respuestas)
data_transf = insert_column(lista_new_columns, data_transf)
data_transf = ponderacion(dicc_categorias, data_transf)


# FUNCIONES PARA LA CREACION DE NUEVAS COLUMNAS A PARTIR DE LAS ANTERIORES CREADAS Y DARLAS ETIQUETAS EN FUNCION DE LAS ETIQUETAS DEL MANUAL DASS
data_transf["Anxiety_cat"] = data_transf["Anxiety"].map(categorizacion_anxiety)
data_transf["Stress_cat"] = data_transf["Stress"].map(categorizacion_stress)
data_transf["Depression_cat"] = data_transf["Depression"].map(categorizacion_depression)


# FUNCIONES PARA LA TRANSFORMACION DE LOS CEROS 
data_transf['gender'] = np.where(data_transf['gender']== 0,3,data_transf['gender'].values)
data_transf['religion'] = np.where(data_transf['religion']== 0,12,data_transf['religion'].values)
data_transf['orientation'] = np.where(data_transf['orientation']== 0,5,data_transf['orientation'].values)
data_transf['married'] = np.where(data_transf['married']== 0,3,data_transf['married'].values)


# CREACION DE LA TARGET A TRAVES DE LAS COLUMNAS DE CATEGORIZACIÓN CREADAS EN EL PASO ANTERIOR

for x in range(data_transf.shape[0]):
    if data_transf.loc[x,'Depression_cat'] == 'Severe' or data_transf.loc[x,'Depression_cat'] == 'Extremely Severe':
        data_transf.loc[x,'Target'] = 1
    elif data_transf.loc[x,'Anxiety_cat'] == 'Severe' or data_transf.loc[x,'Anxiety_cat'] == 'Extremely Severe':
        data_transf.loc[x,'Target'] = 1
    elif data_transf.loc[x,'Stress_cat'] == 'Severe' or data_transf.loc[x,'Stress_cat'] == 'Extremely Severe':
        data_transf.loc[x,'Target'] = 1
    else:
        data_transf.loc[x,'Target'] = 0
        


# FUNCIONES PARA LA CREACION DE NUEVAS COLUMNAS CATEGORICAS PARA PODER VER LAS VISUALIZACIONES DE MANERA MAS SENCILLA
data_transf['Target'] = data_transf['Target'].apply(round)
data_transf["urban_cat"] = data_transf["urban"].map(dicc_lugar)
data_transf["age_cat"] = data_transf["age"].map(categorizacion_edad)
data_transf["familysize_cat"] = data_transf["familysize"].map(categorizacion_familia)
data_transf["gender_cat"] = data_transf["gender"].map(dicc_genero)
data_transf["religion_cat"] = data_transf["religion"].map(dicc_religion)
data_transf["orientation_cat"] = data_transf["orientation"].map(dicc_orientacion)
data_transf["married_cat"] = data_transf["married"].map(dicc_estado)
data_transf["race_cat"] = data_transf["race"].map(dicc_raza)



# REORGANIZACION DE LAS COLUMNAS

data_transf= data_transf.reindex(columns=lista_orden_colum)


data_listo = data_transf[['urban','age','gender','religion','orientation','married','race','familysize','Depression','Anxiety','Stress','Target']]

# UNA VEZ TRANSFORMADOS TODOS LOS DATOS PROCEDEMOS AL ENTRENAMIENTO DEL MODELO

# DIVIDIMOS EN TRAIN Y EN TEST

X_train, X_test, y_train, y_test = train_test_split(data_listo.drop(columns=['Target','Anxiety','Stress'], axis=1), data_listo.Target, random_state=0, test_size=0.20, shuffle=True)



# CREAMOS UN PIPELINE CON EL MODELO Y LA TRANSFROMACION QUE NECESITAMOS

model_lr = Pipeline (steps = [
                     ('scaler', MinMaxScaler()),
                     ('lr', LogisticRegression(C=0.3, solver='newton-cg'))]
                    )



# ENTRENAMOS EL MODELO Y SACAMOS LAS PREDICCIONES


model_lr.fit(X_train,y_train)
y_predi = model_lr.predict(X_test)


# GUARDAMOS LOS RESULTADOS 

df_scores = {'log_re_data_train' :[recall_score(y_test,y_predi), roc_auc_score(y_test,y_predi),  accuracy_score(y_test, y_predi), f1_score(y_test, y_predi)]}
df_scores = pd.DataFrame(df_scores, index=['Recall','Auc','Accuracy', 'F1_score'])

print (df_scores)


# GUARDAMOS LA MATRIZ DE CONFUSION


# GUARDAMOS LA CONFUSION MATRIX PARA DESPUES GRAFICARLA
c_matrix = confusion_matrix(y_test, y_predi)

print(c_matrix)


# LA GRAFICAMOS


plt.style.use('seaborn-whitegrid')

sns.set(font_scale = 1.3)
graficos_conf_matrix(c_matrix,'Logistic Regresión')



# GUARDAMOS EL MODELO


with open('Model/Final/my_model', 'wb') as archivo_salida:
    pickle.dump(model_lr, archivo_salida)


