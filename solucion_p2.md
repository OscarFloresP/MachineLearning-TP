El formato STL (Estereolitografía) es formato de archivo para guardar modelos 3D que
fue inventado en el año 1987 y tiene 2 formas de representación: ASCII y Binario.

Ambos representaciones poseen información sobre las coordenadas de los vertices de
los triángulos y del vector normal de dichos triángulos. El formato de archivo es
ampliamente popular entre los software de modelado e impresión 3D además de los usuarios
de estos productos. Sin embargo, la representación más usada es la binaria por las
ventajas que se describen más adelante.

## ASCII:
  
+ Ventajas:
  + Legible para el humano
  
+ Estructura:
```
solid modelname
facet normal ni nj nk
    outer loop
        vertex v1x v1y v1z
        vertex v2x v2y v2z
        vertex v3x v3y v3z
    endloop
endfacet
endsolid modelname
```

## Binario

+ Ventajas:
  + Menos peso de archivo que su contraparte en ASCII
  + Posibilidad de añadir información de COLOR (no es parte del Standard)
  + Posibilidad de añadir UNIDAD DE MEDIDA (no es parte del Standard)


+ Desventajas:
  + No es legible por el humano.

+ Estructura:
```
UINT8[80]    – Header                 -     80 bytes
UINT32       – Number of triangles    -      4 bytes

foreach triangle                      -     50 bytes:
    REAL32[3] – Normal vector             - 12 bytes
    REAL32[3] – Vertex 1                  - 12 bytes
    REAL32[3] – Vertex 2                  - 12 bytes
    REAL32[3] – Vertex 3                  - 12 bytes
    UINT16    – Attribute byte count      -  2 bytes
end
```
