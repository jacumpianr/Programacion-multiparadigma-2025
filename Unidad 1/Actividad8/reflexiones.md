## Parte 1: Identificar y analizar

Una funcion `Pura` es predecible: siempre da el mismo resultado con los mismos datos de entrada y **no toca** nada fuera de ella.

Una funcion `Impura` es impredecible (usa cosas que cambian como la hora o el azar) o tiene **efectos secundarios** (cambia variables globales o los datos originales que recibe).

---

### Analisis funcion por funcion

### Funcion A: `calcular_promedio`

* Pura
* Porque? Dados los mismos números, siempre devuelve el mismo promedio. No modifica nada.

### Funcion B: `siguiente_id`

* Impura
* Porque? Modifica la variable global `contador`. Esto significa que su resultado depende y altera un estado externo al propio codigo.
* Solucion: Para hacerla pura, la funcion debe recibir el `contador` actual como argumento y devolver el nuevo valor, sin usar `global`.

### Funcion C: `agregar_fecha`

* Impura
* Porque? Usa `datetime.now()`, que es un valor externo que cambia constantemente.
* tambien modifica el diccionario `registro`.
* Solucion: La fecha actual debe ser pasada como argumento, y la funcion debe devolver una copia del registro, no el original.

### Funcion D: `filtrar_positivos`

* Pura
* Porque? Siempre filtra los positivos de la misma manera y devuelve una nueva lista sin modificar la lista de entrada.

### Función E: `mezclar_lista`

* Impura
* Porque? Usa aleatoriedad, lo que la hace impredecible.
* tambien utiliza `random.shuffle(lista)`, que modifica la lista original.
* Solucion: Debe trabajar sobre una copia de la lista para evitar alterar el argumento original.