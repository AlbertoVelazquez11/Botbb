#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Diccionario_Saludos
import Diccionario_Despedidas
import Diccionario_InformacionBasica
import Diccionario_Historias
import Diccionario_Relaciones
import Diccionario_Sin_Entender
from random import randint

# Recuperamos el nombre del bot
nombreBot = Diccionario_InformacionBasica.InformacionBasica["nombre"][0] + " => "

''' Saludo '''
def saludo ( ) : # Selecciona un saludo random == Hacer que se seleccione el tipo de trato ==
	listaOpciones = Diccionario_Saludos.Saludos [ "informal" ]
	eleccion = ( randint ( 0 , len ( listaOpciones ) - 1 ) )
	print nombreBot + listaOpciones [ eleccion ]
	
''' Despedida '''
def despedida ( ) : # Selecciona una despedida random == Hacer que se seleccione el tipo de trato ==
	listaOpciones = Diccionario_Despedidas.Despedidas [ "informal" ]
	eleccion = ( randint ( 0 , len ( listaOpciones ) - 1 ) )
	print nombreBot + listaOpciones [ eleccion ]
	
''' Información básica '''
def informacion_basica ( ) : # == Sin establecer ==
	listaOpciones = Diccionario_InformacionBasica.InformacionBasica [ "informal" ]
	eleccion = ( randint ( 0 , len ( listaOpciones ) - 1 ) )
	print nombreBot + listaOpciones [ eleccion ]
	
''' Historias '''
def historias ( ) : # Selecciona una historia random == Hacer que se seleccione el tipo de historia y ampliar la seleccion de historias por tipo==
	listaEtiquetas = []
	for etiqueta in Diccionario_Historias.Historias :
		listaEtiquetas.append ( etiqueta )
	eleccion = ( randint ( 0 , len ( listaEtiquetas ) - 1 ) )
	opcion = Diccionario_Historias.Historias [ listaEtiquetas [ eleccion ] ]
	print nombreBot + opcion
	
''' Sin entender '''
def sin_entender ( ) : # Selecciona un comentario random indicando que no comprendio
	listaOpciones = Diccionario_Sin_Entender.Sin_Entender [ "informal" ]
	eleccion = ( randint ( 0 , len ( listaOpciones ) - 1 ) )
	print nombreBot + listaOpciones [ eleccion ]