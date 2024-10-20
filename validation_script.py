from pyshacl import validate
import rdflib

def validate_ontology(ontology_file, shacl_file):
    data_graph = rdflib.Graph()
    data_graph.parse(ontology_file, format="turtle")

    shacl_graph = rdflib.Graph()
    shacl_graph.parse(shacl_file, format="turtle")

    conforms, results_graph, results_text = validate(
        data_graph,
        shacl_graph=shacl_graph,
        ont_graph=None,  
        inference='rdfs',  
        abort_on_first=False,  
        meta_shacl=False,  
        advanced=True,  
        js=False,  
    )

    print("Conforms:", conforms)
    print("Results Graph:")
    print(results_graph.serialize(format="turtle"))
    print("Results Text:")
    print(results_text)

    return conforms, results_graph, results_text


ontology_file = "system-data.ttl"
shacl_file = "sense-validation v1.0.shacl"

conforms, results_graph, results_text = validate_ontology(ontology_file, shacl_file)
