from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS, OWL

def check_missing_rdfs_comments(ttl_file):
    g = Graph()
    g.parse(ttl_file, format='turtle')

    namespaces = {
        'rdf': RDF,
        'rdfs': RDFS,
        'owl': OWL
    }
    for prefix, namespace in g.namespaces():
        namespaces[prefix] = namespace

    # Lists to store entities missing rdfs:comment
    missing_comments = []

    # Query for all classes and properties
    query = """
    SELECT ?entity ?type
    WHERE {
        {
            ?entity a owl:Class .
            BIND("Class" AS ?type)
        }
        UNION
        {
            ?entity a rdf:Property .
            BIND("Property" AS ?type)
        }
    }
    """

    results = g.query(query, initNs=namespaces)

    for row in results:
        entity = row.entity
        entity_type = row.type

        # Check if rdfs:comment exists for the entity
        comments = list(g.objects(entity, RDFS.comment))

        if not comments:
            # Get QName for readability
            qname = g.qname(entity)
            missing_comments.append((qname, entity_type))

    # Report entities missing rdfs:comment
    if missing_comments:
        print("Entities missing rdfs:comment:")
        for entity_qname, entity_type in missing_comments:
            print(f" - [{entity_type}] {entity_qname}")
    else:
        print("All classes and properties have rdfs:comment annotations.")

if __name__ == "__main__":
    ttl_file_root = "sense.ttl"  # Replace with the path to your Turtle file
    check_missing_rdfs_comments(ttl_file_root)
