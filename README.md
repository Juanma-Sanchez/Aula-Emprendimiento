### Aula de Emprendimiento

Proyecto de Juan Manuel Sánchez Mateo

## Premisa

El objetivo del proyecto es realizar un análisis de sentimientos de la voz humana desde una perspectiva exclusivamente fonética, con el objetivo de clasificarlos en cuatro categorías: happy (alegre), sad (triste), angry (enfadado) y neutral.

## Planteamiento

Para lograr el objetivo expuesto previamente, empleamos las muestras de audio de un estudio del departamento de Psicología de la universidad de Toronto (https://tspace.library.utoronto.ca/handle/1807/24487). Dado que los audios de muestra se corresponden con voz humana, sabemos que constan de una serie de fonemas, la unidad mínima del lenguaje que se corresponde aproximadamente al sonido de una única letra. Además cada uno de estos fonemas se puede representar como una serie de componentes frecuenciales (generalmente entre 1 y 4 kHz).

Utilizando el script get_max_audio_length.py, determinamos que la frecuencia de muestreo es de 24.4 kHz. Dividiendo el audio en tramas de 128 muestras (unos 5 ms)  podemos garantizar que cada trama se corresponde con un único fonema (que probablemente se repita varias veces).

Empleando el script de Python localizado en este repositorio, generate_data_sets.py, dividimos cada fichero de audio en tramas, obtenemos su representación en frecuencias mediante la Transformada Discreta de Fourier (https://en.wikipedia.org/wiki/Discrete_Fourier_transform) y tras una normalización, almacenamos la concatenación de expectros frecuenciales en imágenes del estilo:

![Alt text](audio_as_img.png?raw=True "Ejemplo de imagen resultante")

## Resultados

## Conclusiones

## Posibles mejoras

Las muestras empleadas son de corta duración y representan un único sentimiento, pero provienen de tan sólo dos personas, los "sentimientos" no son naturales sino actuados y todos los audios son de la forma "Say the word [...]". El primer punto a mejorar del sistema sería entrenar al modelo con audios se correspondieran realmente con lo que se pretende clasificar.

De igual modo que se ha suprimido el offset del audio porque no nos aportaba información, sería posible realizar un filtrado en paso banda del audio para quedarse únicamente con las frecuencias que puede emitir una voz humana, eliminando el mayor ruido posible en el proceso.

Un análisis sintáctico complementaría perfectamente al análisis fonético que hemos implementado en el proyecto, permitiendo analizar qué se dice y cómo.Ponderando resultados en función de la fiabilidad de cada análisis deberíamos poder obtener un resultado bastante confiable del sentimiento que transimte una grabación de voz.
![Alt text](voice_analysis.png?raw=True "Análisis fonético-sintáctico")