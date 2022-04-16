

# LISTA PARA ELIMINAR LAS COLUMNAS QUE CUMPLAN LAS CONDICIOENS ESPECIFICADAS

lista_patron= ['^Q.+I$', '^Q.+E$', '^Q.+I$', 'source',
               'introelapse','testelapse','surveyelapse',
               '^TIPI.','VCL', 'screensize','uniquenetworklocation','hand', 'major','country','engnat','voted']


# LISTA CON LAS NUEVAS COLUMNAS A CREAR

lista_new_columns = ['Depression', 'Anxiety', 'Stress']



# DICCIONARIO DONDE SE ASOCIAN LAS COLUMNAS DEL DATAFRAM QUE PERTENECE A CADA CATEGORIA (ANSIEDAD, ESTRES Y DEPRESION) Y QUE VA A SER PARAMETRO DE FUNCION

dicc_categorias = {'Anxiety': ['Q2A', 'Q4A', 'Q7A', 'Q9A', 'Q15A', 'Q19A', 'Q20A', 'Q23A', 'Q25A', 'Q28A', 'Q30A', 'Q36A', 'Q40A', 'Q41A'],
                   'Stress': ['Q1A', 'Q6A', 'Q8A', 'Q11A', 'Q12A', 'Q14A', 'Q18A', 'Q22A', 'Q27A', 'Q29A', 'Q32A', 'Q33A', 'Q35A', 'Q39A'],
                   'Depression': ['Q3A', 'Q5A', 'Q10A', 'Q13A', 'Q16A', 'Q17A', 'Q21A', 'Q24A', 'Q26A', 'Q31A', 'Q34A', 'Q37A', 'Q38A', 'Q42A'],
                   }


# DICCIONARIO QUE VA A SER PARAMETRO DE FUNCION PARA CAMBIAR TODOS LOS VALORES DE LAS COLUMNAS PERTENECIENTES A DICC_CATEGORIAS
dicc_respuestas = {1 : 0,
                   2 : 1,
                   3 : 2,
                   4 : 3}


# LISTA CON EL ORDEN QUE TIENE QUE TENER EL DATAFRAM Y QUE SERA PARAMETRO DE FUNCION
lista_orden_colum = ['Q1A',	'Q2A',	'Q3A',	'Q4A',	'Q5A',	'Q6A',	'Q7A',	'Q8A',	'Q9A',	'Q10A',	'Q11A',	'Q12A',	'Q13A',	'Q14A',	'Q15A',	'Q16A',
                     'Q17A', 'Q18A', 'Q19A',	'Q20A',	'Q21A',	'Q22A',	'Q23A',	'Q24A',	'Q25A',	'Q26A',  'Q27A',	'Q28A',	'Q29A',	'Q30A',	'Q31A',	'Q32A',
                     'Q33A',	'Q34A',	'Q35A',	'Q36A',	'Q37A',	'Q38A',	'Q39A',	'Q40A', 'Q41A',	'Q42A',
                     'education','urban','urban_cat','age','age_cat','gender','gender_cat','religion','religion_cat','orientation','orientation_cat','married','married_cat','race','race_cat',
                     'familysize','familysize_cat','Depression','Depression_cat','Anxiety','Anxiety_cat','Stress','Stress_cat','Target']


# DICCIONARIO CON LA CLASIFICACION QUE VA A TENER LA COLUMNA urban_cat
dicc_lugar = {0: 'Other',
              1: 'Rural (country side)',
              2: 'Suburban',
              3: 'Urban (town-city)',
                   }


# DICCIONARIO CON LA CLASIFICACION QUE VA A TENER LA COLUMNA genger_cat

dicc_genero = {1: 'Male',
              2: 'Female',
              3: 'Other',
                   }

# DICCIONARIO CON LA CLASIFICACION QUE VA A TENER LA COLUMNA religion_cat

dicc_religion = {1: 'Agnostic',
                2: 'Atheist',
                3: 'Buddhist',
                4: 'Catholic',
                5: 'Mormon',
                6: 'Protestant',
                7: 'Other',
                8: 'Hindu',
                9: 'Jewish',
                10: 'Muslim',
                11: 'Slikh',
                12: 'Other'}


# DICCIONARIO CON LA CLASIFICACION QUE VA A TENER LA COLUMNA orientation_cat
dicc_orientacion = {1: 'Heterosexual',
                   2: 'Bisexual',
                   3: 'Homosexual',
                   4: 'Asexual',
                   5: 'Other'}


# DICCIONARIO CON LA CLASIFICACION QUE VA A TENER LA COLUMNA married_cat
dicc_estado = {1: 'Never married',
              2: 'Currently married',
              3: 'other',
                   }

# DICCIONARIO CON LA CLASIFICACION QUE VA A TENER LA COLUMNA religion_cat

dicc_raza = {10: 'Asian',
            20: 'Arab',
            30: 'Black',
            40: 'Indigenous Australian',
            50: 'Native American',
            60: 'White',
            70: 'Other'}


# LISTA CON LOS COLORES DEL TARGET PARA LOS GRAFICOS

color_target = ['#EEE8AA','#808000']

# LISTA CON LOS COLORES DEL DEL RESTO DE COLUMNAS DEL DATAFAME QUE VAN A SER GRAFICADAS

colores = ['#EEE8AA','#F0E68C','#D2B48C','#CD853F','#808000']