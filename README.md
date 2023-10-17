# Experimento de la Doble Rendija

## 1. Objetivo 📑
---
Replicar y explicar el famoso experimento de la doble rendija por medio de la construcción de una doble rendija a escala y una simulación cuántica computacional.

## 2. Materiales 🔧
---
- Cartón paja
- Aluminio
- Láser rojo
- Escuadra
- Trípode
- Cinta adhesiva
- Silicona líquida
- Cuchilla de precisión

## 3. Resumen y Explicación 📚
---
El experimento de la doble rendija es un fenómeno fundamental de la física cuántica que ilustra las incógnitas y confusiones generadas de la dualidad onda-partícula de la luz y de cómo se crean las superposiciones de estados. Este es un claro ejemplo de cómo la física cuántica difiere de la física clásica, revelando la importancia de los sistemas cuánticos y justificando por medio del experimento la existencia del multiverso, el cual da sentido a las múltiples historias de las partículas. 

En este experimento, partículas como electrones o fotones se envían a través de una barrera con dos rendijas o ranuras paralelas, lo cual lo hace intrigante y único, puesto que no se puede determinar con seguridad cuál barrera atravesará cada fotón, sino que para ello se hacen cálculos probabilísticos propios de la mecánica cuántica. Con ello, el resultado es un patrón de interferencia parecido a bandas o segmentos de líneas con mayor concentración en el centro que se van creando en una pantalla de detección.

El sistema se describe mediante un sistema de estados cuánticos, el cual representa la probabilidad de encontrar la partícula en diferentes posiciones. Este experimento desafía nuestra intuición clásica, ya que muestra que las partículas cuánticas pueden comportarse como si existieran múltiples historias de ella misma.

## 4. Mediciones 📐
---
Haciendo uso de los materiales mencionados anteriormente, y con algunas herramientas adicionales, se elaboró el montaje para el experimento que se muestra en las siguientes imágenes:

<p align="center">
    <img width="200" height="240" src="https://github.com/JAPV-X2612/Experimento_Doble_Rendija/blob/main/I1.png/">  
       
</p>
<p align="center">
    <em>Imagen 1. Montaje del experimento</em>
</p>
<p align="center"> 
    <img width="200" height="240" src="https://github.com/JAPV-X2612/Experimento_Doble_Rendija/blob/main/I2.png/">   
</p>
<p align="center">
    <em>Imagen 2. Doble rendija</em>
</p>

Una vez listo el montaje y ubicada la doble rendija en un lugar oscuro para efectos de una mejor visualización de los resultados, se procedió a encender el láser y a apuntarlo al centro de las dos ranuras, con lo cual parte de la luz se proyectó sobre la pared del fondo generando el patrón que se muestra a continuación:

<p align="center">
    <img width="270" height="220" src="https://github.com/JAPV-X2612/Experimento_Doble_Rendija/blob/main/I3.png/">    
</p>
<p align="center">
    <em>Imagen 3. Patrón del experimento con luz ambiental</em>  
</p>
<p align="center"> 
    <img width="270" height="220" src="https://github.com/JAPV-X2612/Experimento_Doble_Rendija/blob/main/I4.png/">   
</p>
<p align="center">
    <em>Imagen 4. Patrón del experimento en la oscuridad</em> 
</p>

De esta forma, se puede observar con claridad el patrón de interferencia generado por el experimento, cuya explicación teórica se puede realizar a través de una simulación cuántica computacional para demostrar que la probabilidad de hallar cada fotón en una determinada posición de la pantalla después de “disparar” una cantidad significativa de los mismos, es equivalente al patrón generado.

Por tal motivo, a continuación introducimos una simulación para n fotones con estado inicial |ψ₀⟩=[n,0,0,0,0,0,0,0], los cuales van a ser “disparados” por la doble rendija, con la probabilidad de pasar por cada ranura representada a través de una matriz de relaciones M con números complejos, con lo cual se puede generar el siguiente esquema para un mejor entendimiento de la simulación:

<p align="center"> 
    <img width="250" height="370" src="https://github.com/JAPV-X2612/Experimento_Doble_Rendija/blob/main/I5.png/">   
</p>
<p align="center">
    <em>Imagen 5. Esquema de la simulación computacional</em> 
</p>

Ahora, haciendo uso de la [Librería de Simulación de lo Clásico a lo Cuántico](https://github.com/JAPV-X2612/Libreria_Simulacion_Clasico_a_Cuantico), generamos el siguiente código que nos representa el experimento y retorna un gráfico de barras correspondiente a las probabilidades:

<p align="center"> 
    <img width="600" height="270" src="https://github.com/JAPV-X2612/Experimento_Doble_Rendija/blob/main/I6.png/">   
</p>
<p align="center">
    <em>Imagen 6. Código del programa en Python</em> 
</p>

Después de ejecutar el algoritmo obtenemos los siguientes resultados:

<p align="center"> 
    <img width="500" height="72" src="https://github.com/JAPV-X2612/Experimento_Doble_Rendija/blob/main/I7.png/">   
</p>
<p align="center">
    <em>Imagen 7. Resultados de la simulación en Python</em> 
</p>
<p align="center"> 
    <img width="300" height="225" src="https://github.com/JAPV-X2612/Experimento_Doble_Rendija/blob/main/G1.png/">   
</p>
<p align="center">
    <em>Gráfico 1. Representación de los resultados del experimento</em> 
</p>

De esta forma, podemos observar que las probabilidades de hallar los n fotones después de ser “disparados” se distribuye únicamente sobre los nodos 3 a 7, los cuales efectivamente corresponden a la pantalla de detección. Sin embargo, en el gráfico también podemos notar algo muy particular, y es que la probabilidad de hallar alguno de los n fotones en el nodo 5 es "igual a cero"; pero esto se puede justificar por la implementación de los números imaginarios, los cuales al operarse se anularon entre ellos y su interpretación en la vida real es que “luz + luz = sombra”.

## 5. Conclusión 📒
---
El experimento de la doble rendija nos permitió observar la posible existencia del “multiverso”, gracias a la interpretación cuántica de que las partículas, al atravesar las rendijas, se dividían en “varias historias”, lo cual justifica la forma del patrón obtenido de una manera diferente a la convencional que se hace determinísticamente y no da una respuesta concluyente.

## 6. Bibliografía, Textos y Wikis 📖
---
Para mayor información sobre los temas descritos en este proyecto se recomienda revisar los siguientes enlaces:

* Autodesk Instructables. (2013). [How to Make a Simple Double-Slit](https://www.instructables.com/How-To-Make-a-Simple-Double-Slit/).
* Empirical Zeal. (2014). [Electrons go through a double-slit one at a time](https://www.youtube.com/watch?v=1LVkQfCptEs).
* Phisics Demos. (2016). [Interference Demo: Double Slit](https://www.youtube.com/watch?v=PVyJFzx7zig).
* QuantumFracture. (2016). [Este Experimento te Dejará LOCO | La Doble Rendija](https://www.youtube.com/watch?v=Y9ScxCemsPM).
* Wikipedia. (2023). [Números Complejos](https://es.wikipedia.org/wiki/N%C3%BAmero_complejo).
*  Wikipedia. (2023). [Qubit](https://es.wikipedia.org/wiki/C%C3%BAbit)
*  Wikipedia. (2023). [Computación Cuántica](https://es.wikipedia.org/wiki/Computaci%C3%B3n_cu%C3%A1ntica).
* Yanofsky N. S. & Mannucci M. A. (2008). [Quantum Computing for Computer Scientists](https://www.cambridge.org/core/books/quantum-computing-for-computer-scientists/8AEA723BEE5CC9F5C03FDD4BA850C711). First Edition. Cambridge University Press.

## 7. Autores ✒️
---
Este proyecto es de la autoría de ***Nicole Calderon***, ***Jesús Pinzón*** y ***Juan Vera***, ingenieros de sistemas de la Escuela Colombiana de Ingeniería Julio Garavito ([ECIJG](https://www.escuelaing.edu.co/es/)).  

## 8. Licencia 📄
---
Este proyecto tiene licencia de código abierto, por lo cual puede ser usado por cualquier persona u organización con fines educativos y de investigación. No obstante, está **PROHIBIDA SU DISTRIBUCIÓN** parcial o completa con fines lucrativos sin expreso consentimiento de los autores.  
Se recomienda revisar el archivo [LICENSE](https://github.com/JAPV-X2612/Experimento_Doble_Rendija/blob/main/LICENSE.md) adjunto al repositorio para mayor información.