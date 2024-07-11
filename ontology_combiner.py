import rdflib
import copy

def combine_ontologies(ontology1_path, ontology2_path, output_path):
    g1 = rdflib.Graph()
    g1.parse(ontology1_path, format=rdflib.util.guess_format(ontology1_path))

    g1_copy = copy.deepcopy(g1)

    g2 = rdflib.Graph()
    g2.parse(ontology2_path, format=rdflib.util.guess_format(ontology2_path))

    g2_copy = copy.deepcopy(g2)

    combined_graph = g1_copy + g2_copy

    combined_graph.serialize(destination=output_path, format='turtle')
    print(f"Combined ontology saved to {output_path}")


ontology1_path = 'SENSE v1.0.ttl'
ontology2_path = 'SENSEComments.ttl'
output_path = 'sense.ttl'

combine_ontologies(ontology1_path, ontology2_path, output_path)
