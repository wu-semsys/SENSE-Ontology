import rdflib
import os

def combine_ontologies(ontology1_path, ontology2_paths, output_path):
    combined_graph = rdflib.Graph()

    print(f"Parsing {ontology1_path}")
    with open(ontology1_path, 'r', encoding='utf-8') as f:
        data = f.read()
    combined_graph.parse(data=data, format='turtle')

    for ontology_path in ontology2_paths:
        print(f"Parsing {ontology_path}")
        with open(ontology_path, 'r', encoding='utf-8') as f:
            data = f.read()
        combined_graph.parse(data=data, format='turtle')

    combined_graph.serialize(destination=output_path, format='turtle')
    print(f"Combined ontology saved to {output_path}")

base_dir = os.path.dirname(os.path.abspath(__file__))
ontology_dir = os.path.join(base_dir, 'ontology files')

print(rdflib.__version__)

ontology1_path = os.path.join(ontology_dir, 'SENSE v1.0.ttl')
ontology2_paths = [
    os.path.join(ontology_dir, 'SENSEComments.ttl'),
    os.path.join(ontology_dir, 'SENSE v2.0_chowlk.ttl'),
    os.path.join(ontology_dir, 'SENSE v2.0_inverses.ttl'),
    os.path.join(ontology_dir, 'SENSE v2.0_oopsfixes.ttl')
]

output_path = os.path.join(base_dir, 'sense.ttl')

combine_ontologies(ontology1_path, ontology2_paths, output_path)