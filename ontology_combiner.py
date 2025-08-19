import rdflib
import os

def combine_ontologies(ontology1_path, ontology2_paths, output_path):
    g1 = rdflib.Graph()
    g1.parse(ontology1_path, format=rdflib.util.guess_format(ontology1_path))

    combined_graph = g1

    for ontology_path in ontology2_paths:
        g2 = rdflib.Graph()
        g2.parse(ontology_path, format=rdflib.util.guess_format(ontology_path))
        combined_graph += g2 

    combined_graph.serialize(destination=output_path, format='turtle')
    print(f"Combined ontology saved to {output_path}")

base_dir = os.path.dirname(os.path.abspath(__file__))
ontology_dir = os.path.join(base_dir, 'ontology files')

ontology1_path = os.path.join(ontology_dir, 'SENSE v3.0_chowlk.ttl')
ontology2_paths = [
    os.path.join(ontology_dir, 'SENSEComments.ttl'),
    os.path.join(ontology_dir, 'SENSE v3.0_inverses.ttl'),
    os.path.join(ontology_dir, 'SENSE v3.0_oopsfixes.ttl')
    #os.path.join(ontology_dir, 'SENSEOntologyAlignment.ttl')
]

output_path = os.path.join(ontology_dir, 'SENSE v3.0.ttl')

combine_ontologies(ontology1_path, ontology2_paths, output_path)
