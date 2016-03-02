#!/usr/bin/python
# -*- coding: utf-8 -*-

print "------------------------------------------"
print "A= LISTA EL NOMBRE DE TODOS LOS COLEGIOS "
print "B= CUENTA EL NUMERO DE COLEGIOS QUE CONTIENE EL FICHERO"
print "EXIT= PARA SALIR"

print "------------------------------------------"
from lxml import etree
doc=etree.parse('/home/usuario/XML-COLEGIOS-GIJ-N-/colegios.xml')
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

	tecla=str.upper(raw_input("Opcion: "))
