# Informe de los formatos usados en `hermosa-sipiran-2018.pdf`

En el paper de reconstrucción en 3D usan Generative Adversarial Network con
la finalidad de completar objetos arqueológicos. En el caso de los modelos 3D usan
el formato Objet File Format (.off), este formato son de Princeton Shape
Benchmark los cuales lo hicieron para ayudar a representar de forma geométrica
el modelo, se debe especificar los polígonos de la superficie de la figura, la
forma de los polígonos puede contener cualquier número vértices. Estos tipos de
archivos .off siempre comienzan con la palabra clave OFF, la línea siguiente se
pone el numero de vértices, caras y aristas en este respectivo orden, el numero
de aristas se puede ignorar y dejarlo como 0 sin preocupación que suceda algún
problema. En las siguientes líneas colocas las coordenadas de los vértices con
x, y, z. Cada coordenada de los vértices debe ser escrita en una línea
diferente, la cantidad de vértices debe ser igual al numero que colocaste al
principio. Luego de la lista de vértices, se enumera la lista de caras, igual
que los vértices es uno por línea, en cada cara debes especificar que numero de
vértices que lo compone, seguido en la misma línea de debe poner los índices de
los vértices teniendo en cuenta que el índice de los vértices de la lista que
se colocó número de índice siempre es -1 al número que esta. Como ejemplo se
puede observar el siguiente cubo que se hizo siguiente el formato

> sample.off
```
OFF
8 6 0
-0.500000 -0.500000 0.500000
0.500000 -0.500000 0.500000
-0.500000 0.500000 0.500000
0.500000 0.500000 0.500000
-0.500000 0.500000 -0.500000
0.500000 0.500000 -0.500000
-0.500000 -0.500000 -0.500000
0.500000 -0.500000 -0.500000
4 0 1 3 2
4 2 3 5 4
4 4 5 7 6
4 6 7 1 0
4 1 7 5 3
4 6 0 2 4
```

