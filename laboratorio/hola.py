from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

#1.Prueba para verificar que los datos en la base de datos coinciden con los creados en setUpTestData para un laboratorio dado:

class LaboratorioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio=Laboratorio.objects.create(nombre="LabTest", ciudad="CiudadTest", pais="PaisTest")

    def test_datos_coinciden(self):
        # Obtén el laboratorio creado en setUpTestData
        lab = Laboratorio.objects.get(nombre="LabTest")

        # Verifica que los datos coincidan con los valores iniciales
        self.assertEqual(lab.nombre, "LabTest")
        self.assertEqual(lab.ciudad, "CiudadTest")
        self.assertEqual(lab.pais, "PaisTest")

  

#2.Prueba para verificar que la URL para un laboratorio devuelve una respuesta HTTP 200:

class LaboratorioViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crea un laboratorio para las pruebas
        Laboratorio.objects.create(nombre="LabTest", ciudad="CiudadTest", pais="PaisTest")

    def test_url_retorna_200(self):
        # Obtén el laboratorio creado en setUpTestData
        lab = Laboratorio.objects.get(nombre="LabTest")

        # Obtiene la URL para el detalle del laboratorio utilizando reverse
        url = reverse('detalle_laboratorio', args=[lab.id])

        # Realiza una solicitud HTTP GET a la URL
        response = self.client.get(url)

        # Verifica que la respuesta HTTP sea 200
        self.assertEqual(response.status_code, 200)



#3.Prueba para verificar que la página utilizando reverse devuelve una respuesta HTTP 200, usa la plantilla correcta y el contenido HTML coincide con lo esperado:
class LaboratorioViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crea un laboratorio para las pruebas
        Laboratorio.objects.create(nombre="LabTest", ciudad="CiudadTest", pais="PaisTest")

    def test_vista_laboratorio(self):
        # Obtén el laboratorio creado en setUpTestData
        lab = Laboratorio.objects.get(nombre="LabTest")

        # Obtiene la URL para el detalle del laboratorio utilizando reverse
        url = reverse('detalle_laboratorio', args=[lab.id])

        # Realiza una solicitud HTTP GET a la URL
        response = self.client.get(url)

        # Verifica que la respuesta HTTP sea 200
        self.assertEqual(response.status_code, 200)

        # Verifica que se esté utilizando la plantilla correcta
        self.assertTemplateUsed(response, 'detalle_laboratorio.html')

        # Verifica que el contenido HTML coincida con lo esperado
        self.assertContains(response, f"<h1>{lab.nombre}</h1>")
        self.assertContains(response, f"<p>Ciudad: {lab.ciudad}</p>")
        self.assertContains(response, f"<p>País: {lab.pais}</p>")
