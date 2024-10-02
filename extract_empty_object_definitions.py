from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS, OWL

def extract_classes_and_object_properties(ttl_file):
    # Load the Turtle file into an RDF graph
    g = Graph()
    g.parse(ttl_file, format='turtle')

    # List to store owl:class instances
    objects = []

    # Iterate over each triple in the graph
    for subj, pred, obj in g:
        # Check if the triple represents a class
        if pred == RDF.type:
            objects.append(subj)

    # Convert URIs to QNames using defined namespace prefixes
    objects = [g.qname(uri) for uri in objects]

    return sorted(objects)

# Example usage
if __name__ == "__main__":
    ttl_file_root = "./ontology files/SENSE v1.0.ttl"  # Replace with the path to your Turtle file
    objects = extract_classes_and_object_properties(ttl_file_root)

    print("#empty objects:")
    for uri in objects:
        print(uri + " rdfs:comment \"\" .")

    
