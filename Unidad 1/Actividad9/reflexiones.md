# Reflexiones sobre Programacion Funcional

### ¿Qué significa que una función sea "pura"? Explícalo con tus propias palabras y da un ejemplo de tu vida cotidiana que ilustre el concepto (no de programación).

Una función es pura si cumple dos reglas clave: Siempre produce la misma salida con la misma entrada y no cambia nada fuera de ella.

**Ejemplo** Hacer hielo, si uno agrega x cantidad de agua en el molde sera lo mismo que en hielo.

### En la Parte 3, ¿por qué `crear_transformador` retorna una función en lugar de aplicar directamente la transformación? ¿Qué ventaja ofrece este diseño?

Retornar una funcin permite definir el comportamiento una vez y luego aplicarlo multiples veces a diferentes listas en distintos momentos. Esta tecnica facilita la composicion de funciones y la creacion de herramientas flexibles, lo cual es central en la programacioon funcional.

### ¿Qué dificultades encontraste al convertir el código imperativo a funcional en la Parte 2? ¿Qué parte fue más difícil y cómo la resolviste?

La principal dificultad fue evitar la mutacion de datos, ya que en lo imperativo es comun actualizar variables o listas. Lo resolvi aplicando una regla estricta: cada funcion debe recibir datos y devolver datos nuevos.

### Si tuvieras que explicar la diferencia entre programación imperativa y funcional a alguien que no programa, ¿qué analogía usarías?

La programacion imperativa es como darle a un amigo una receta con instrucciones detalladas y secuenciales. En cambio, la programacion funcional es como pedir un menu, confiando en que el sistema (las funciones puras) ya sabe cómo producir el resultado final sin que importen los pasos internos ni el estado de la cocina.