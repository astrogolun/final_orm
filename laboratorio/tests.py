from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio
# Create your tests here.

class LaboratorioTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(nombre="Nombre prueba", ciudad='Ciudad prueba', pais='Pais prueba')

    def test_model_content(self):
        lab = Laboratorio.objects.get(nombre="Nombre prueba")       
        self.assertEqual(lab.nombre, "Nombre prueba")
        self.assertEqual(lab.ciudad, "Ciudad prueba")
        self.assertEqual(lab.pais, "Pais prueba")


    def test_url_exists_at_correct_location(self):       
        response = self.client.get("/mostrar/")
        self.assertEqual(response.status_code, 200)
               
        
    def test_homepage(self):
        response = self.client.get(reverse("mostrar_lab"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mostrar.html")
        self.assertContains(response, "Información de Laboratorios")  



