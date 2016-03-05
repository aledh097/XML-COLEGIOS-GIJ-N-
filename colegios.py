#!/usr/bin/python
# -*- coding: utf-8 -*-

print "------------------------------------------"
print "A= LISTA EL NOMBRE DE TODOS LOS COLEGIOS "
print "B= CUENTA EL NUMERO DE COLEGIOS QUE CONTIENE EL FICHERO"
print "C= DEVOLVER URL DEL COLEGIO SEGÚN UN NÚMERO DE TELÉFONO"
print "D= DEVOLVER NOMBRE DEL COLEGIO SEGÚN SU DIRECCION"
print "EXIT= PARA SALIR"

print "------------------------------------------"
from lxml import etree
import lxml.html, lxml.etree

doc=etree.parse('colegios.xml')
raiz=doc.getroot()
tecla=str.upper(raw_input("Opcion: "))

while tecla!="EXIT":
	if tecla=="A":
		listado=doc.xpath(u"/directorios/directorio/nombre/text()")	
		for l in listado:
			print l
			
	if tecla=="B":
		listado=doc.xpath(u"/directorios/directorio/nombre/text()")	
		print "El número total de colegios es de: %s" % (len(listado))
	
	if tecla=="C":
		buscador=raw_input("Dime el número de teléfono: ")
		colegios=etree.parse('colegios.xml')
		raiz=colegios.getroot()
		telefonos=raiz.findall("directorio/telefono")
		url=raiz.findall("directorio/url")
		for t,u in zip(telefonos,url):
			if buscador==t.text:
				print u.text
			
	if tecla=="D":
		buscador=raw_input("Dime la dirección: ")
		colegios=etree.parse('colegios.xml')
		raiz=colegios.getroot()
		direcciones=doc.xpath("/directorios/directorio/direccion[2]/text()")
		nombre=raiz.findall("directorio/nombre")
		for d,n in zip(direcciones,nombre):
			if buscador==d:
				print n.text
			
	print "------------------------------------------"
	print "A= LISTA EL NOMBRE DE TODOS LOS COLEGIOS "
	print "B= CUENTA EL NUMERO DE COLEGIOS QUE CONTIENE EL FICHERO"
	print "C= DEVOLVER URL DEL COLEGIO SEGÚN UN NÚMERO DE TELÉFONO"
	print "D= DEVOLVER NOMBRE DEL COLEGIO SEGÚN SU DIRECCION"
	print "EXIT= PARA SALIR"

	print "------------------------------------------"
	tecla=str.upper(raw_input("Opcion: "))
