# ML_Depresion_Estres_Ansiedad

Proyecto para el módulo de Machine Learning durante el bootcamp de Data Science.

El objetivo de este proyecto es construir un modelo de predicción que permita ofrecer ayuda psicológica gratuita a las personas cuyo resultado cumplan las condiciones para ello.
Se generará  la target o variable objetivo que nos permitirá trabajar con nuestro modelo de predicción (clasificación).
La métrica que se utilizará es la AUC y 
Los datos  sobre los que se trabajarán están basados en una encuesta realizada a casi 40.000 personas de todo el mundo, en la que a parte de recoger las contestaciones, se recopila información relativa a la género, edad,  religión, número de hijos, orientación sexual etc.
Esta encuesta, llamada DASS (Depression, Ansiety, Stress Scales), es un instrumento diseñado para medir estados emocionales relacionados con la depresión, la ansiedad y el estrés elaborado por la Fundación de Psicología de Australia.

Está compuesta por 42 preguntas, 14 preguntas para cada bloque (depresión, ansiedad y estrés)

Existen 4 respuestas posibles:
->  No me siento identificado.
-> Me siento identificado en cierto grado.
-> Me siento identificado en un grado considerable.
-> Me siento identificado en gran medida o la mayor parte del tiempo.

Estas, son etiquetas de “gravedad” consideradas por el manual DASS:

![image](https://user-images.githubusercontent.com/97395621/168214687-ae795be4-eb8d-4915-aa89-691c6d61cbeb.png)

El modelo clasificará como:
1 o “necesita ayuda”
0 o “ no necesita ayuda
a las personas cuyo resultado en la encuesta para cualquier de las casuísticas sea “Severe” o “Extremely Severe”. 






 

