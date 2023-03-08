from os import system
import platform
from datetime import date
autor="Sol"

so=platform.system()
if so=="Linux":
	s="clear"
else:
	s="cls"

hoy=date.today()
dia=hoy.day
mes=hoy.month
anio=hoy.year

system(s)
print(" Autor: "+f" {autor}".rjust(80,"-"))
print(" Fecha: "+f" {dia}/{mes}/{anio}".rjust(80,"-"))


def Suma():
 a=int(input("Ingrese el 1° numero: "))
 b=int(input("Ingrese el 2° numero: "))
 print (f"El resultado de la Suma {a} y {b} es: {a+b}")
 input("...")

def Resta():
 a=int(input("Ingrese el 1° numero: "))
 b=int(input("Ingrese el 2° numero: "))
 print (f"El resultado de la Resta {a} y {b} es: {a-b}")
 input("...")

def Producto():
 a=int(input("Ingrese el 1° numero: "))
 b=int(input("Ingrese el 2° numero: "))
 print (f"El resultado del Producto {a} y {b} es: {a*b}")
 input("...")

def Cociente():
 a=int(input("Ingrese el 1° numero: "))
 b=int(input("Ingrese el 2° numero: "))
 print (f"El resultado del Cociente {a} y {b} es: {a/b}")
 input("...")


while True:
	
	print("Calculadora")
	print("\t+...Suma")
	print("\t-...Resta")
	print("\t*...Producto")
	print("\t/...Cociente")
	print("\tS...Salir")

	if (op:=input("Ingresar operación: "))=="+":
		print("Suma")
		Suma()

	elif op=="-":
		print("Resta")
		Resta()

	elif op=="*":
		print("Producto")
		Producto()

	elif op=="/":
		print("Cociente")
		Cociente()

	elif op.upper=="S":
		exit()				
