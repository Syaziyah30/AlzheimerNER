#################################### COMPLETE COMMAND  #######################

#### extract the right format of input  ✓
#### extract the right semantic_entity  ✓
#### construct the right format of dataframe from start, end, entity, semantic ✓
#### allow displacy to highlight ✓
#### detect all the entity in the displacy highlight ✓

# load the function
import pandas as pd
import re
import spacy
from spacy.matcher import PhraseMatcher
import json
from spacy import displacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to load entities from CSV files into a dictionary
def load_entities_from_csv(file_paths, categories):
    entities = {}
    for file_path, category in zip(file_paths, categories):
        try:
            df = pd.read_csv(file_path)
            entities[category] = df['entity'].dropna().tolist()  # Assuming column 'entity' exists
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            entities[category] = []
    return entities

# Function to clean text using regular expressions
def clean_text(text):
    text = re.sub(r'~exclusion"\r\n', '', text)  # Remove unwanted parts
    text = re.sub(r'~', ' ', text)
    text = re.sub(r'\u003e', '>', text)
    text = re.sub(r'\\', '', text)  # Remove backslash symbol
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    text = re.sub(r'^\"|\"$', '', text)  # Remove leading and trailing quotation marks
    return text

# Function to remove duplicates using lemmatization
def remove_duplicates(matched_entities):
    unique_entities = {category: [] for category in matched_entities}
    for category, entities in matched_entities.items():
        seen = set()
        filtered_entities = []
        for entity in entities:
            lemmatized = " ".join([token.lemma_ for token in nlp(entity)])
            if lemmatized.lower() not in seen:
                seen.add(lemmatized.lower())
                if not any(lemmatized.lower() in e.lower() for e in filtered_entities):
                    filtered_entities.append(entity)
        unique_entities[category] = filtered_entities
    return unique_entities

# Function to match entities using PhraseMatcher
def match_entities(text, entities):
    doc = nlp(text)
    matched_entities = {category: [] for category in entities}
    for category, entity_list in entities.items():
        matcher = PhraseMatcher(nlp.vocab)
        patterns = [nlp.make_doc(entity) for entity in entity_list]
        matcher.add(category, None, *patterns)

        matches = matcher(doc)
        for _, start, end in matches:
            matched_entities[category].append(doc[start:end].text)
    return remove_duplicates(matched_entities)


# Reset entities and add new ones
def add_custom_entities(doc, matched_entities, cleaned_input):
    doc.set_ents([])  # Reset pre-existing entities
    entities_info = []

    # Collect entity spans and indices
    for category, matched in matched_entities.items():
        for entity in matched:
            start_idx = cleaned_input.find(entity)
            end_idx = start_idx + len(entity)
            entities_info.append((start_idx, end_idx, entity, category))

    # Sort entities by start index
    entities_info.sort(key=lambda x: x[0])

    # Define new spans and prevent overlap
    new_spans = []
    last_end = -1  # To track the end of the previous span

    for start_idx, end_idx, entity, category in entities_info:
        # Ensure no overlap with the previous span
        if start_idx >= last_end:
            span = doc.char_span(start_idx, end_idx, label=category)
            if span:  # Only add valid spans
                new_spans.append(span)
                last_end = end_idx  # Update last_end to the current span's end index

    doc.set_ents(new_spans)  # Update document entities

    # Print added entities
    print("\nAdded Entities:")
    print(f"{'Start':<10} {'End':<10} {'Entity':<50} {'Semantic':<15}")
    for span in new_spans:
        print(f"{span.start_char:<10} {span.end_char:<10} {span.text:<50} {span.label_:<15}")

    return doc

    # Print added entities
    print("\nAdded Entities:")
    print(f"{'Start':<10} {'End':<10} {'Entity':<50} {'Semantic':<15}")
    for span in new_spans:
        print(f"{span.start_char:<10} {span.end_char:<10} {span.text:<50} {span.label_:<15}")
    return doc

# Define file paths and categories
csv_files = [
    "C:/Users/syaziyah.psh/Documents/Alzheimer Project Syaziyah/Inclusion criteria - each semantic/caregiver.csv",
    "C:/Users/syaziyah.psh/Documents/Alzheimer Project Syaziyah/Inclusion criteria - each semantic/condition.csv",
    "C:/Users/syaziyah.psh/Documents/Alzheimer Project Syaziyah/Inclusion criteria - each semantic/demography.csv",
    "C:/Users/syaziyah.psh/Documents/Alzheimer Project Syaziyah/Inclusion criteria - each semantic/drug.csv",
    "C:/Users/syaziyah.psh/Documents/Alzheimer Project Syaziyah/Inclusion criteria - each semantic/measurement.csv",
    "C:/Users/syaziyah.psh/Documents/Alzheimer Project Syaziyah/Inclusion criteria - each semantic/procedure.csv",
    "C:/Users/syaziyah.psh/Documents/Alzheimer Project Syaziyah/Inclusion criteria - each semantic/time.csv",
    "C:/Users/syaziyah.psh/Documents/Alzheimer Project Syaziyah/Inclusion criteria - each semantic/value.csv"
]
semantic_categories = ["caregiver", "condition", "demography", "drug",
                       "measurement", "procedure", "time", "value"]

# Load entities
entities = load_entities_from_csv(csv_files, semantic_categories)

# Load JSON content
json_file = r"C:/Users/syaziyah.psh/Documents/Alzheimer Project Syaziyah/FILES 267/Finalized Files_267/UPDATED/Finalized Files_267/NCT00141661.json"
try:
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)
        input_text = data.get("content", "")
        cleaned_input = clean_text(input_text)

        # Print the content from the JSON file
        print("Content from JSON file:")
        formatted_text = re.sub(r'^\"', '', input_text)  # Removes a leading quotation mark
        formatted_text = re.sub(r'(\.)(\s)', r'.\n',
                                formatted_text)  # Adds a new line after each period followed by a space
        print(formatted_text)  # This will print the "content" field from the JSON with better readability

        # Match entities
        matched_entities = match_entities(cleaned_input, entities)
        doc = nlp(cleaned_input)  # Create spaCy doc

        # Add custom entities and print
        doc = add_custom_entities(doc, matched_entities, cleaned_input)

        # Visualize entities with displacy
        options = {
            "colors": {
                "measurement": "#00BFFF",
                "value": "#FFD700",
                "drug": "#FF6347",
                "condition": "#98FB98",
                "time": "#C8A2C8",
                "demography": "#FFA500",
                "caregiver": "#D2B48C",
                "procedure": "#ADD8E6"
            }
        }
        displacy.serve(doc, style="ent", options=options)

except FileNotFoundError:
    print(f"File not found: {json_file}")
except json.JSONDecodeError:
    print(f"Error decoding JSON: {json_file}")





