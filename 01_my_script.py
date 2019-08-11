# File: 01_my_script.py
# Functie: Sample taken from pyStrich GitHub repository
#          Python script als voorbeeld tbv hoe pyhton script uit te voeren mbv een Docker container
# Doc: zie https://runnable.com/docker/python/dockerize-your-python-application


# https://github.com/mmulqueen/pyStrich
from pystrich.datamatrix import DataMatrixEncoder

encoder = DataMatrixEncoder('This is a DataMatrix.')
encoder.save('./datamatrix_test.png')
print(encoder.get_ascii())
