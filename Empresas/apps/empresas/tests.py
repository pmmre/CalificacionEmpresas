from django.test import TestCase
from .models import Empresa
from .views import registrar
 

# Create your tests here.
import unittest


class TestStringMethods(unittest.TestCase):
	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_Modelo(self):
		emp = Empresa(nombre="Maracena",calificacion="-1")
		emp.save()

		emp2 = Empresa.objects.get(nombre="Maracena")
		#self.assertEqual(emp,Empresa.objects.filter(nombre="Maracena"))
		self.assertEqual(emp.nombre,emp2.nombre)
		self.assertEqual(int(emp.calificacion),int(emp2.calificacion))

	def test_registrar_Post(self):
		request.POST['nombre']="Mercadona"
		#Registrar.post()



#  def test_Modelo(Empresa):
#      emp = Empresa(nombre="Mercadona",calificacion="-1")
#	  emp.save()

#	  self.assertEqual(emp == Empresa.object.filter(nombre="Mercadona"))

if __name__ == '__main__':
	unittest.main()


#class TestStringMethods(unittest.TestCase):

#	def test_upper(self):
#     	self.assertEqual('foo'.upper(), 'FOO')

#  	def Modelo(self):
#  		emp = Empresa(nombre="Mercadona",calificacion="-1")
#		emp.save()

#		self.assertEqual(emp == Empresa.object.filter(nombre="Mercadona"))





#if __name__ == '__main__':
#    unittest.main()
