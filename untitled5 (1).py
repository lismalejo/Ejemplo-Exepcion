# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mnfmifQ0OIheMvfS-sFx2Co4qKvaiy1l
"""

while True:

  try:
    a = int(input("Ingrese numerador"))
    b = int(input("Ingrese denominador"))

    c= a/ b
    print("El resultado es", c )
    break


  except ZeroDivisionError:
      print('No dividir entre cero')
  except ValueError:
    print("Ingrese un numero valido")