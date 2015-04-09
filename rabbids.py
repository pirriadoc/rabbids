#!/usr/bin/env python
#-*- coding: utf-8 -*-

##recibe un numero de meses devuelve las parejas de rabbids que hay en ese mes
def rabbids (meses):
## usaré las variables a y b como los dos valores  iniciales de la 
## secuencia, que son 1 y 1.
	a = 1
	b = 1
## si es 1 o 2 meses hay una pareja
	if meses <= 2:
		res = 1
## si es mas de 2 meses el res será el de la suma de los dos res anteriores
## sumamos a y b (1+1 inicalmente) y sustituimos a por b y b por res
## de manera que tenemos siempre a y b como los dos ultimos resultados.
	else:
## el range debería comenzar en 3 porque el valor 1 y el 2 ya los 
## conozco, lo hago empezar en 2 porque el ultimo valor de un range
## no se incluye, es decir sería lo mismo que poner in range (3,meses+1)
		for n in range (2, meses):
			res = a + b
			a = b
			b = res
	return res
