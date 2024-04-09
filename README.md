# SENSE Ontology

The SENSE Ontology is created as part of the SENSE project. It is located at the following namespace: http://w3id.org/explainability/sense#


- **SENSE v1.0.drawio**: Visual notation of the SENSE Ontology
- **SENSE v1.0.drawio.xml**: XML Export of the drawio file to be uploaded to CHOWLK converter
- **SENSE v1.0.ttl**: Turtle file of the SENSE Ontology as converted by the CHOWLK converter https://catalogue.fair-impact.eu/resources/chowlk
- **SENSEComments.ttl**: Turtle file, which contains additional metadata information, which is not included in the CHOWLK.converted file. This metadata has to be updated manually, if new classes and properties are added to the drawio concept of the Ontology.
- **ISSUES.md**: currently a local, manual list of issues to address in the future.

## Workflow
To enforce any changes to the SENSE Ontology, the following steps should be executed:
1. Export drawio of the Ontology as an XML File ``SENSE v1.0.drawio.xml``
2. Convert the XML file to ttl using the chowlk converter
3. add missing descriptions of classes and properties in the ``SENSEComments.ttl`` file (to check which objects miss a description, execute ``extract_empty_object_definitions.py``)
4. if needed, update Abstract, Introduction, Description, References below to be added to the widoco page of the ontology. 
5. [TODO Gregor] add steps to get to Widoco website

## Abstract
This ontology is created to support Semantics-based Explanation of Cyber-physical Systems in the course of the SENSE Project.

## Introduction
The SENSE Ontology aims to provide a framework to enable explanations of events and states in cyber-physical systems. It extends the sosa ontology with explainability- and event-specific classes and properties to be able to represent events, states and causal relations between these. THe SENSE Ontology can be extended with domain-specific ontologies depending on the use case.

## SENSE: Description
TODO: add diagram of the ontology.

## References
[owl-time] Time Ontology in OWL. Simon Cox; Chris Little. W3C. 19 October 2017. W3C Recommendation. URL: https://www.w3.org/TR/owl-time/

[SSNO] The SSN ontology of the W3C semantic sensor network incubator group. Michael Compton; Payam Barnaghi; Luis Bermudez; Raúl García-Castro; Oscar Corcho; Simon Cox; John Graybeal; Manfred Hauswirth; Cory Henson; Arthur Herzog; Vincent Huang; Krzysztof Janowicz; W. David Kelsey; Danh Le Phuoc; Laurent Lefort; Myriam Leggieri; Holger Neuhaus; Andriy Nikolov; Kevin Page; Alexandre Passant; Amit Sheth; Kerry Taylor. Web Semantics: Science, Services and Agents on the World Wide Web, 17:25-32 . December 2012. URL: http://www.sciencedirect.com/science/article/pii/S1570826812000571

[SOSA] SOSA: A lightweight ontology for sensors, observations, samples, and actuators. Janowicz, K., Haller, A., Cox, S. J., Le Phuoc, D., & Lefrançois, M. Journal of Web Semantics, 56, 1-10.(2019).