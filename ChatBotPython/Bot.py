#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Importamos los metodos y diccionarios necesarios '''
import Metodos
import Diccionario_Relaciones
''' Inicializamos variables locales '''
termina = 0
contador = 0
mayorRelacionNombre = "Nada"
mayorRelacion = 0
diccRelaciones = Diccionario_Relaciones.Relaciones
contadores = { "Saludos" : 0 ,
			   "Despedidas" : 0 ,
			   "InformacionBasica" : 0 ,
			   "Historias" : 0 }
# Iniciamos con el saludo del bot
print "bot => Soy un poco timida, saludame..." 
raw_input ( "Tu => " )
Metodos.saludo ( ) # Responemos con un saludo random (informal por default)
''' Aquí se inicia el ciclo principal, un WHILE que va iterar hasta que
	el usuario indique una despedida y el bot lo comprenda'''
while termina == 0 : # Ciclo principal
	frase = raw_input ( "Tu => " ).split( ' ' ) # La entrada del usuario
	for palabra in frase : # Ciclo para analizar cada palabra introducida por el usuario
		for etiqueta in diccRelaciones : # Ciclo para buscar las palabras claves e identificar el tema de conversación
			contador = 0
			while contador < len ( diccRelaciones [ etiqueta ] ) : # Ciclo para contar las coincidencias de palabras claves
				if palabra in diccRelaciones [ etiqueta ][ contador ] : # Condición para conocer si la palabra existe y sumar en caso de ser verdadero
					contadores [ etiqueta ] = contadores [ etiqueta ] + 1
				contador = contador + 1
	for nombre in contadores : # Ciclo para determinar que tema tiene mas coincidencias
		if contadores [ nombre ] > mayorRelacion : # Condición para conocer que tema tiene mayor coincidencias
			mayorRelacionNombre = nombre
			mayorRelacion = contadores [ nombre ]
	if mayorRelacionNombre == "Despedidas" : # DESPEDIDA
		termina = 1
	elif mayorRelacionNombre == "InformacionBasica" : # INFORMACION BASICA
		Metodos.informacion_basica ( )
	elif mayorRelacionNombre == "Historias" : # HISTORIAS
		Metodos.historias ( )
	elif mayorRelacion == 0 : # NO ENTENDIO
		Metodos.sin_entender ( )
	mayorRelacion = 0
	mayorRelacionNombre = "Nada"
	contadores = { "Saludos" : 0 ,
				   "Despedidas" : 0 ,
				   "InformacionBasica" : 0 ,
				   "Historias" : 0 }
''' FIN_WHILE - Aquí termina el While principal '''
Metodos.despedida ( )