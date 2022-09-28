Identificar y describir en el informe las conversiones de tipos que considera necesarias para el
proyecto del trabajo parcial y final

En el presente trabajo hemos utilizado 3 tipos formatos diferentes para la impresión de 3d, 
estos formatos son .off, .obj y .stl. En las transformaciones hemos preferido transformar 
todo al formato de .stl por la popularidad que tiene con los software de impresion 3D y ventajas 
que nos ofrece para poder utilizarlo. En el ambiente del FabLab en las impresoras 3D tambien se 
nos recomendo utilizar el formato de .stl porque puede contener una mayor cantidad de informacion 
al momento de la impresión.

Con el fin de realizar la converión se ha tenido que leer los archivos, para poder identificar
los vertices y las caras, con esta información se puede transformar a cualquiera de los 3 diferentes
formatos presentados .off, .obj y .stl, ahora para pasarlo de un formato a otro es escribir en
un nuevo archivo siguiendo la estructura que necesite cada formato.

Con las conversiones que hicimos se tuvo algunas necesidades, como lo es el caso .off, que en las caras 
nos daba la información de poligonos pero para transformarlo a otro formato tuvimos que hacer pequeña 
función que pase los polígonos que usa .off a triángulos que usan .stl y .obj, otra necesidad que
tuvimos fue para .stl binario, que con el uso de una librería conseguimos obtener el mesh por lo
que apartir de ahi tuvimos que transformarlo al mismo formato que usabamos.
