# -*- coding: utf-8 -*-
"""Task05.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12By4H6NcTiH2LrD8ij_V0HlNjDOw1zCm

**Task 05: Reading and writing ontologies**
"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

"""Read the RDF file and manage prefix in the graph with namespace_manager"""

from rdflib import Graph, Namespace, Literal,RDFS
g = Graph()
g.namespace_manager.bind('vcard-rdf',Namespace("http://www.w3.org/2001/vcard-rdf/3.0/"),override=False)
g.parse(github_storage+"/resources/example4.rdf", format="xml")

"""Now we can get some of the triples from RDFS (the model, not the data)"""

print("Show all the RDFS Class of the model")
for s,p,o in g.triples((None, None, RDFS.Class)):
  print(s,p,o)

print("\n\nShow all the properties where RDFS range is defined in the model")
for s,p,o in g.triples((None, RDFS.range, None)):
  print(s,p,o)

print("\n\nShow all the subClassOf relations of the model")
for s,p,o in g.triples((None, RDFS.subClassOf, None)):
  print(s,p,o)

"""The entire graph, the instances and the RDFS triples are now shown"""

for s,p,o in g:
  print(s,p,o)