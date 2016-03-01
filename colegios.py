#!/usr/bin/python
# -*- coding: utf-8 -*-

print "------------------------------------------"
print "A= LISTA EL NOMBRE DE TODOS LOS COLEGIOS "
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
	tecla=str.upper(raw_input("Opcion: "))
