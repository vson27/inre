import re


D1=" machine learning improves medical image analysis"
D2="deep learning improves medical diagnosis"
D3="machine learning and deep learning are used in diagnosis"
D4="medical image analysis uses convolutional networks"
D5="deep learning models analyze medical images"
D6= " machine learning models improve image classification"

stop_words = {"a", "an", "the", "and", "are", "used", "in", "uses", "as", "is", "it", "on", "of", "or", "for"}


documents = {}

'''for i in ("D1","D2"):
    with open(f"{i}.txt", "r", encoding="utf-8") as file:
        text = file.read()'''
i=1
for text in (D1,D2,D3,D4,D5,D6):
    tokens = re.findall(r'\b[a-zA-Z]+\b', text) #ignores punctuations and extracts words.
    tokens = [token.lower() for token in tokens]
    tokens = [token for token in tokens if token not in stop_words]
    documents[f"D{i}"] = tokens

    print(f"\nD{i} Tokens after preprocessing:")
    print(tokens)
    i+=1


vocabulary = sorted(set(term for doc in documents for term in doc))

print("\nVocabulary:")
print(vocabulary)

matrix = []

for term in vocabulary:
    row = []

    for doc in documents:
        if term in doc:
            row.append(1)
        else:
            row.append(0)

    matrix.append(row)

print("\nTerm-Document Incidence Matrix:")
print(f"{'Term':<20} D1  D2  D3  D4  D5  D6")

for i, term in enumerate(vocabulary):
    print(f"{term:<20} {matrix[i][0]:<3} {matrix[i][1]:<3} {matrix[i][2]:<3} {matrix[i][3]:<3} {matrix[i][4]:<3} {matrix[i][5]:<3}")


inverted_index = {}

for doc_id, tokens in documents.items():
    unique_terms = set(tokens)

    for term in unique_terms:
        if term not in inverted_index:
            inverted_index[term] = []

        inverted_index[term].append(doc_id)

for term in inverted_index:
    inverted_index[term].sort()

print("\nInverted Index")
print(f"{'Term':<20} {'Postings List':<40} {'Doc Freq'}")

for term in sorted(inverted_index):
    postings = inverted_index[term]
    document_frequency = len(postings)

    print(f"{term:<20} {str(postings):<40} {document_frequency}")


def boolean_or(postings1, postings2):
    result = []

    i = 0
    j = 0

    while i < len(postings1) and j < len(postings2):

        if postings1[i] == postings2[j]:
            result.append(postings1[i])
            i += 1
            j += 1

        elif postings1[i] < postings2[j]:
            result.append(postings1[i])
            i += 1

        else:
            result.append(postings2[j])
            j += 1

    while i < len(postings1):
        result.append(postings1[i])
        i += 1

    while j < len(postings2):
        result.append(postings2[j])
        j += 1

    return result

for term in sorted(inverted_index):
    postings = inverted_index[term]
    document_frequency = len(postings)

    print(f"{term:<20} {str(postings):<40} {document_frequency}")

global_postings=[]

terms=input("Enter the terms separated by spaces: ").split()
terms.sort(key=lambda term: len(inverted_index.get(term, [])))

result=[]

for term in terms:
    if term not in inverted_index:
        print(f"\nTerm '{term}' not found in inverted index.")
        
    else:
        postings = inverted_index[term]
        result = boolean_or(postings, global_postings)

        print(f"\nCurrent Postings: {global_postings}")
        print(f"Posting list for '{term}': {postings}")
        global_postings=result


if result:
    print(f"\n\nDocuments containing Union of the terms: {terms} ---> ", result)
else:
    print("No document contains all terms.")


def boolean_and(postings1, postings2):
    result = []

    i = 0
    j = 0

    while i < len(postings1) and j < len(postings2):

        if postings1[i] == postings2[j]:
            result.append(postings1[i])
            i += 1
            j += 1

        elif postings1[i] < postings2[j]:
            i += 1

        else:
            j += 1

    return result

for term in sorted(inverted_index):
    postings = inverted_index[term]
    document_frequency = len(postings)

    print(f"{term:<20} {str(postings):<40} {document_frequency}")

global_postings=['D1','D2','D3','D4','D5','D6']

terms=input("Enter the terms separated by spaces: ").split()
terms.sort(key=lambda term: len(inverted_index.get(term, [])))

for term in terms:
    if term not in inverted_index:
        print(f"\nTerm '{term}' not found in inverted index.")
        result=[]
        break
        
    else:
        postings = inverted_index[term]
        result = boolean_and(postings, global_postings)

        print(f"\nCurrent Postings: {global_postings}")
        print(f"Posting list for '{term}': {postings}")
        global_postings=result


if result:
    print(f"\n\nDocuments containing the terms: {terms} ---> ", result)
else:
    print("No document contains all terms.")
























def boolean_difference(postings1, postings2):
    result = []

    i = 0
    j = 0

    while i < len(postings1) and j < len(postings2):

        if postings1[i] == postings2[j]:
            i += 1
            j += 1

        elif postings1[i] < postings2[j]:
            result.append(postings1[i])
            i += 1

        else:
            j += 1

    while i < len(postings1):
        result.append(postings1[i])
        i += 1

    return result


while True:
    terms = input("\nEnter the terms separated by spaces: ").split()

    if len(terms) != 2:
        print("Only enter 2 terms\n")
        continue

    break


if terms[0] not in inverted_index:
    print(f"\nTerm '{terms[0]}' not found in inverted index.")
    result = []

elif terms[1] not in inverted_index:
    print(f"\nTerm '{terms[1]}' not found in inverted index.")
    print(f"\nPosting list for '{terms[0]}': {postings1}")
    result = inverted_index[terms[0]]

else:
    postings1 = inverted_index[terms[0]]
    postings2 = inverted_index[terms[1]]

    print(f"\nPosting list for '{terms[0]}': {postings1}")
    print(f"Posting list for '{terms[1]}': {postings2}")

    result = boolean_difference(postings1, postings2)


if result:
    print(f"\n\nDocuments containing {terms[0]} AND NOT {terms[1]} --->", result)
else:
    print("No document matches the condition.")























n = int(input("Enter number of terms: "))

postings = {}

for _ in range(n):
    term = input("\nEnter term: ").lower()

    df = len(inverted_index[term])

    documents = inverted_index[term]

    postings[term] = {
        "df": df,
        "list": documents
    }


terms = sorted(postings, key=lambda term: postings[term]["df"])

print(postings)


print("\nOptimized order:")

for term in terms:
    print(f"{term} -> {postings[term]['df']}")


result = postings[terms[0]]["list"]

print(f"\nInitial result: {result}")

for term in terms[1:]:
    result = boolean_and(result, postings[term]["list"])

    print(f"After AND with {term}: {result}")


print("\nFinal Result:")
print(result)
























import math 

P1 = [2, 4, 8, 16, 32, 64, 128, 256]
P2 = [4, 8, 16, 20, 32, 64, 100, 128, 200, 256]


def standard_intersection(P1, P2):
    result = []

    i = 0
    j = 0
    comparisons = 0

    while i < len(P1) and j < len(P2):

        comparisons += 1

        if P1[i] == P2[j]:
            result.append(P1[i])
            i += 1
            j += 1

        elif P1[i] < P2[j]:
            i += 1

        else:
            j += 1

    return result, comparisons


result, comparisons = standard_intersection(P1, P2)

print("Standard Intersection:")
print("Result:", result)
print("Comparisons:", comparisons)

def skip (P1, P2):
    skip1=int(math.sqrt(len(P1)))
    skip2=int(math.sqrt(len(P2)))
    result = []

    i = 0
    j = 0
    comparisons = 0

    while i < len(P1) and j < len(P2):

        comparisons += 1

        if P1[i] == P2[j]:
            result.append(P1[i])
            i += 1
            j += 1

        elif P1[i] < P2[j]:
            if i+skip1<len(P1) and P1[i+skip1] <=P2[j]:
                i += skip1
            else:
                i+=1

        else:
            if j+skip2<len(P2) and P2[j+skip2] <=P1[i]:
                j += skip2
            else:
                j += 1

    return result, comparisons


result, comparisons = skip(P1, P2)

print("Skip Intersection:")
print("Result:", result)
print("Comparisons:", comparisons)























# Create skip pointers
def create_skips(postings):
    skip_length = int(math.sqrt(len(postings)))
    skips = {}

    for i in range(0, len(postings), skip_length):
        skip_to = i + skip_length

        if skip_to < len(postings):
            skips[i] = skip_to

    return skips


# Intersection using skip pointers
def skip_intersection(postings1, postings2):
    result = []

    skips1 = create_skips(postings1)
    skips2 = create_skips(postings2)

    i = 0
    j = 0
    comparisons = 0

    while i < len(postings1) and j < len(postings2):
        comparisons += 1

        if postings1[i] == postings2[j]:
            result.append(postings1[i])
            i += 1
            j += 1

        elif postings1[i] < postings2[j]:

            if i in skips1 and postings1[skips1[i]] <= postings2[j]:
                i = skips1[i]
            else:
                i += 1

        else:

            if j in skips2 and postings2[skips2[j]] <= postings1[i]:
                j = skips2[j]
            else:
                j += 1

    return result, comparisons

# Skip-pointer intersection
result2, comparisons2 = skip_intersection(P1, P2)

print("\nSkip Pointers:")
print("Intersection:", result2)
print("Comparisons:", comparisons2)























documents = {
    "D1": "information retrieval is an important field",
    "D2": "information retrieval system improves search",
    "D3": "retrieval system optimization improves performance",
    "D4": "information system provides efficient retrieval",
    "D5": "information retrieval system optimization"
}


biword_index = {}

for doc_id, text in documents.items():
    words = text.split()

    for i in range(len(words) - 1):
        biword = words[i] + " " + words[i + 1]

        if biword not in biword_index:
            biword_index[biword] = []

        if doc_id not in biword_index[biword]:
            biword_index[biword].append(doc_id)


# Display Biword Index

print("Biword Index:")
for biword in sorted(biword_index):
    print(f"{biword:<40} {biword_index[biword]}")


# 2, 3 and 4. Process Phrase Queries

queries = [
    "information retrieval",
    "retrieval system",
    "system optimization",
    "information retrieval system"
]


for query in queries:

    words = query.split()

    # Convert phrase into biwords
    biwords = []

    for i in range(len(words) - 1):
        biwords.append(words[i] + " " + words[i + 1])

    print(f"\nQuery: \"{query}\"")
    print("Biwords:", biwords)

    # Retrieve postings for each biword
    postings = []

    for biword in biwords:
        if biword in biword_index:
            postings.append(biword_index[biword])
        else:
            postings.append([])

    print("Postings:", postings)

    # Find documents containing all biwords
    if postings:
        matching_documents = set(postings[0])

        for posting in postings[1:]:
            matching_documents = matching_documents.intersection(posting)

        matching_documents = sorted(matching_documents)
    else: 
        matching_documents = []

    print("Matching Documents:", matching_documents)












!pip install nltk












import re
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required NLTK data
nltk.download('wordnet')
nltk.download('omw-1.4')

documents = {
    "D1": "The students are studying information retrieval techniques.",
    "D2": "Students studied different retrieval techniques for searching information.",
    "D3": "The system retrieves relevant documents and provides better results.",
    "D4": "Searching and retrieving documents are important tasks in information retrieval."
}

stop_words = {"the", "are", "is", "and", "for", "in", "of", "to", "a"}

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


def preprocess(text):
    
    # 1. Tokenization
    tokens = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    # 2. Stop-word removal
    filtered_tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    # 3. Stemming
    stemmed_tokens = [
        stemmer.stem(word)
        for word in filtered_tokens
    ]

    # 4. Lemmatization
    lemmatized_tokens = [
        lemmatizer.lemmatize(word)
        for word in filtered_tokens
    ]

    return tokens, filtered_tokens, stemmed_tokens, lemmatized_tokens


# Process each document

for doc_id, text in documents.items():

    tokens, filtered, stemmed, lemmatized = preprocess(text)

    print(f"\n{'=' * 60}")
    print(doc_id)

    print("\nOriginal text:")
    print(text)

    print("\nTokens:")
    print(tokens)

    print("\nTokens after stop-word removal:")
    print(filtered)

    print("\nStemmed tokens:")
    print(stemmed)

    print("\nLemmatized tokens:")
    print(lemmatized)


# Comparison of specific words

words = [
    "studying",
    "studied",
    "searching",
    "retrieves",
    "retrieving",
    "documents"
]

print(f"\n{'=' * 60}")
print("Stemming vs Lemmatization")
print(f"{'Word':<15}{'Stem':<15}{'Lemma':<15}")

for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)

    print(f"{word:<15}{stem:<15}{lemma:<15}")


# User query preprocessing

def preprocess_query():
    
    query = input("\nEnter your query: ")

    tokens, filtered, stemmed, lemmatized = preprocess(query)

    print("\nOriginal query:")
    print(query)

    print("\nTokens:")
    print(tokens)

    print("\nTokens after stop-word removal:")
    print(filtered)

    print("\nStemmed tokens:")
    print(stemmed)

    print("\nLemmatized tokens:")
    print(lemmatized)


preprocess_query()

























import re

documents = {
    "D1": "Information retrieval is an important field of computer science and helps users find relevant information.",
    "D2": "Information retrieval systems are widely used in modern search engines to retrieve relevant documents.",
    "D3": "Computer science includes machine learning, artificial intelligence, data mining, and database systems.",
    "D4": "Search engines use information retrieval techniques to provide relevant results to users.",
    "D5": "Natural language processing deals with understanding and generating human language.",
    "D6": "Machine learning algorithms can be used for classification and prediction tasks.",
    "D7": "Information retrieval techniques are important for searching large collections of digital documents.",
    "D8": "Computer vision focuses on understanding images and videos using computational techniques.",
    "D9": "Data mining discovers useful patterns and knowledge from large datasets.",
    "D10": "Information retrieval is widely used in search engines, digital libraries, and document management systems."
}


# Construct positional inverted index

positional_index = {}

for doc_id, text in documents.items():

    tokens = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    for position, term in enumerate(tokens, start=1):

        if term not in positional_index:
            positional_index[term] = {}

        if doc_id not in positional_index[term]:
            positional_index[term][doc_id] = []

        positional_index[term][doc_id].append(position)


# Display positional index

print("POSITIONAL INVERTED INDEX\n")

for term in sorted(positional_index):
    print(f"{term:<20} {positional_index[term]}")


# Phrase query

query = "information retrieval"

query_terms = re.findall(r'\b[a-zA-Z]+\b', query.lower())

term1 = query_terms[0]
term2 = query_terms[1]

print(f"\n\nPhrase Query: \"{query}\"")

matching_documents = []

if term1 in positional_index and term2 in positional_index:

    # Documents containing both terms
    common_documents = (
        positional_index[term1].keys()
        & positional_index[term2].keys()
    )

    for doc_id in common_documents:

        positions1 = positional_index[term1][doc_id]
        positions2 = positional_index[term2][doc_id]

        # Check whether term2 occurs immediately after term1
        for position in positions1:

            if position + 1 in positions2:
                matching_documents.append(doc_id)
                break


print("Matching Documents:", matching_documents)
























import re
from bisect import bisect_left


documents = {
    1: "information retrieval systems process large collections of documents",
    2: "information processing techniques are used in computer systems",
    3: "machine learning improves information retrieval",
    4: "computer vision and machine learning are important research areas",
    5: "efficient retrieval systems support fast searching"
}


# =========================================================
# 1. INVERTED INDEX / TERM DICTIONARY
# =========================================================

inverted_index = {}

for doc_id, text in documents.items():

    terms = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    for term in terms:

        if term not in inverted_index:
            inverted_index[term] = []

        if doc_id not in inverted_index[term]:
            inverted_index[term].append(doc_id)


term_dictionary = sorted(inverted_index.keys())

print("TERM DICTIONARY")
print(term_dictionary)


# =========================================================
# 2. PREFIX SEARCH: comp*
# =========================================================

def prefix_search(prefix):

    prefix = prefix.lower()

    start = bisect_left(term_dictionary, prefix)

    matching_terms = []

    for i in range(start, len(term_dictionary)):

        term = term_dictionary[i]

        if term.startswith(prefix):
            matching_terms.append(term)
        else:
            break

    return matching_terms


# =========================================================
# 3. SUFFIX SEARCH: *ing
# =========================================================

def suffix_search(suffix):

    suffix = suffix.lower()

    matching_terms = []

    for term in term_dictionary:

        if term.endswith(suffix):
            matching_terms.append(term)

    return matching_terms


# =========================================================
# 4. PERMUTERM INDEX
# =========================================================

permuterm_index = {}

for term in term_dictionary:

    word = term + "$"

    for i in range(len(word)):

        rotation = word[i:] + word[:i]

        if rotation not in permuterm_index:
            permuterm_index[rotation] = []

        permuterm_index[rotation].append(term)


# =========================================================
# 5. MIDDLE WILDCARD USING PERMUTERM INDEX
# =========================================================

def permuterm_search(query):

    query = query.lower()

    # Split query around *
    left, right = query.split("*")

    # Convert:
    # comp*er
    #
    # into:
    # er$comp*

    rotated_query = right + "$" + left + "*"

    matching_terms = set()

    for rotation, terms in permuterm_index.items():

        if rotation.startswith(rotated_query[:-1]):
            matching_terms.update(terms)

    return sorted(matching_terms)


# =========================================================
# 6. GET DOCUMENTS FOR MATCHING TERMS
# =========================================================

def get_documents(matching_terms):

    result = set()

    for term in matching_terms:

        result.update(inverted_index[term])

    return sorted(result)


# =========================================================
# 7. TEST QUERIES
# =========================================================

print("\nPREFIX QUERY")
query = "comp*"

terms = prefix_search(query[:-1])

print("Query:", query)
print("Matching terms:", terms)
print("Documents:", get_documents(terms))


print("\nSUFFIX QUERY")
query = "*ing"

terms = suffix_search(query[1:])

print("Query:", query)
print("Matching terms:", terms)
print("Documents:", get_documents(terms))


print("\nMIDDLE WILDCARD QUERY")
query = "comp*er"

terms = permuterm_search(query)

print("Query:", query)
print("Matching terms:", terms)
print("Documents:", get_documents(terms))
























# ==========================================
# Q1: Construct an Inverted Index
# ==========================================

documents = {
    "D1": "information retrieval is useful",
    "D2": "information retrieval uses an index",
    "D3": "retrieval systems are useful"
}

# Inverted index: term -> list of document IDs
inverted_index = {}

for doc_id, text in documents.items():

    # Tokenization and case folding
    terms = text.lower().split()

    for term in terms:
        if term not in inverted_index:
            inverted_index[term] = []

        # Avoid duplicate document IDs
        if doc_id not in inverted_index[term]:
            inverted_index[term].append(doc_id)

# Display term, postings list and DF
for term in sorted(inverted_index):
    print(f"{term:<12} -> {inverted_index[term]}    DF = {len(inverted_index[term])}")
























# ==========================================
# Q2: Permuterm Index
# ==========================================

documents = {
    "D1": "digital libraries provide efficient access to research resources",
    "D2": "researchers use computational methods for analyzing large datasets",
    "D3": "digital systems support automatic document processing",
    "D4": "computational evidence improves information analysis",
    "D5": "library management systems organize digital documents"
}


# ==========================================
# 1. Construct vocabulary
# ==========================================

vocabulary = []

for text in documents.values():
    for word in text.lower().split():

        if word not in vocabulary:
            vocabulary.append(word)

vocabulary.sort()


# ==========================================
# 3. Construct Permuterm Index
# ==========================================

permuterm_index = []

for term in vocabulary:

    word = term + "$"

    for i in range(len(word)):

        rotation = word[i:] + word[:i]

        permuterm_index.append((rotation, term))


# Sort the Permuterm Index
permuterm_index.sort()


# Display index
for rotation, term in permuterm_index:
    print(f"{rotation:<25} -> {term}")


























# ==========================================
# Q2: Permuterm Wildcard Query Processing
# ==========================================

documents = {
    "D1": "digital libraries provide efficient access to research resources",
    "D2": "researchers use computational methods for analyzing large datasets",
    "D3": "digital systems support automatic document processing",
    "D4": "computational evidence improves information analysis",
    "D5": "library management systems organize digital documents"
}


# ==========================================
# 1. Construct Vocabulary
# ==========================================

vocabulary = []

for text in documents.values():

    terms = text.lower().split()

    for term in terms:

        if term not in vocabulary:
            vocabulary.append(term)

vocabulary.sort()


# ==========================================
# 2. Construct Inverted Index
# ==========================================

inverted_index = {}

for doc_id, text in documents.items():

    terms = text.lower().split()

    for term in terms:

        if term not in inverted_index:
            inverted_index[term] = []

        if doc_id not in inverted_index[term]:
            inverted_index[term].append(doc_id)


# ==========================================
# 3. Construct Permuterm Index
# ==========================================

permuterm_index = []

for term in vocabulary:

    word = term + "$"

    for i in range(len(word)):

        rotation = word[i:] + word[:i]

        permuterm_index.append((rotation, term))


# Sort rotations
permuterm_index.sort()


# ==========================================
# 4. Transform Wildcard Query
# ==========================================

def transform_query(query):

    query = query.lower()

    # Add $
    query = query + "$"

    # Find position of *
    star_position = query.index("*")

    # Rotate until * is at the end
    transformed = query[star_position + 1:] + query[:star_position]

    # Remove * from the end
    transformed = transformed[:-1]

    return transformed


# ==========================================
# 5. Search Permuterm Index
# ==========================================

def wildcard_search(query):

    transformed = transform_query(query)

    matching_terms = []

    # Search through sorted Permuterm Index
    for rotation, term in permuterm_index:

        # Compare prefix manually
        if rotation[:len(transformed)] == transformed:

            if term not in matching_terms:
                matching_terms.append(term)

    return transformed, matching_terms


# ==========================================
# 6. Display Results
# ==========================================

queries = [
    "digital*",
    "*ing",
    "comp*al",
    "docu*ent",
    "auto*ic"
]

for query in queries:

    transformed, terms = wildcard_search(query)

    print("\nQuery:", query)
    print("Transformed Permuterm query:", transformed)

    if len(terms) == 0:

        print("Matching vocabulary terms: No matching term")
        print("Corresponding document IDs: None")

    else:

        print("Matching vocabulary terms:", terms)

        doc_ids = []

        for term in terms:

            for doc_id in inverted_index[term]:

                if doc_id not in doc_ids:
                    doc_ids.append(doc_id)

        print("Corresponding document IDs:", doc_ids)


















import re
from bisect import bisect_left
import math


# ============================================================
# DOCUMENT COLLECTION
# ============================================================

documents = {
    "D1": "computer computing computation complete running learning processing retrieving",
    "D2": "compiler compter learning processing",
    "D3": "computer networks retrieving documents",
    "D4": "machine learning improves computer vision",
    "D5": "document processing running applications"
}


# ============================================================
# 1. BUILD INVERTED INDEX
#    term -> list of document IDs
# ============================================================

inverted_index = {}

for doc_id, text in documents.items():

    # Tokenization + lowercase
    terms = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    for term in terms:

        if term not in inverted_index:
            inverted_index[term] = []

        # Avoid duplicate document IDs
        if doc_id not in inverted_index[term]:
            inverted_index[term].append(doc_id)


# ============================================================
# 2. B-TREE IMPLEMENTATION
# ============================================================

class BTreeNode:

    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []


class BTree:

    def __init__(self, minimum_degree=2):
        self.t = minimum_degree
        self.root = BTreeNode(leaf=True)


    # --------------------------------------------------------
    # Search for a key
    # --------------------------------------------------------

    def search(self, key, node=None):

        if node is None:
            node = self.root

        i = 0

        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return node

        if node.leaf:
            return None

        return self.search(key, node.children[i])


    # --------------------------------------------------------
    # Insert a new key
    # --------------------------------------------------------

    def insert(self, key):

        # Don't insert duplicates
        if self.search(key) is not None:
            return

        root = self.root

        # If root is full, split it
        if len(root.keys) == 2 * self.t - 1:

            new_root = BTreeNode(leaf=False)
            new_root.children.append(root)

            self.root = new_root

            self.split_child(new_root, 0)

            self.insert_non_full(new_root, key)

        else:
            self.insert_non_full(root, key)


    # --------------------------------------------------------
    # Split a full child
    # --------------------------------------------------------

    def split_child(self, parent, index):

        t = self.t

        full_child = parent.children[index]

        new_child = BTreeNode(leaf=full_child.leaf)

        # Middle key moves to parent
        middle_key = full_child.keys[t - 1]

        # Keys after middle go to new child
        new_child.keys = full_child.keys[t:]

        # Keys before middle stay in old child
        full_child.keys = full_child.keys[:t - 1]

        # If not leaf, split children too
        if not full_child.leaf:

            new_child.children = full_child.children[t:]

            full_child.children = full_child.children[:t]

        parent.children.insert(index + 1, new_child)

        parent.keys.insert(index, middle_key)


    # --------------------------------------------------------
    # Insert into a node that is not full
    # --------------------------------------------------------

    def insert_non_full(self, node, key):

        i = len(node.keys) - 1

        # If leaf, insert directly
        if node.leaf:

            node.keys.append(None)

            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1

            node.keys[i + 1] = key

        else:

            # Find correct child
            while i >= 0 and key < node.keys[i]:
                i -= 1

            i += 1

            # If child is full, split it
            if len(node.children[i].keys) == 2 * self.t - 1:

                self.split_child(node, i)

                if key > node.keys[i]:
                    i += 1

            self.insert_non_full(node.children[i], key)


    # --------------------------------------------------------
    # In-order traversal
    # Returns all terms in sorted order
    # --------------------------------------------------------

    def inorder(self, node=None, result=None):

        if result is None:
            result = []

        if node is None:
            node = self.root

        if node.leaf:

            result.extend(node.keys)

        else:

            for i, key in enumerate(node.keys):

                self.inorder(node.children[i], result)

                result.append(key)

            self.inorder(node.children[-1], result)

        return result


# ============================================================
# 3. BUILD B-TREE TERM DICTIONARY
# ============================================================

btree = BTree()

for term in inverted_index:
    btree.insert(term)


# Get sorted dictionary from B-tree
term_dictionary = btree.inorder()


print("\n==============================")
print("TERM DICTIONARY")
print("==============================")

for term in term_dictionary:
    print(term)


# ============================================================
# 4. PREFIX SEARCH
#    Example: comp*
# ============================================================

def prefix_search(prefix):

    prefix = prefix.lower()

    # Find first possible position
    start = bisect_left(term_dictionary, prefix)

    matching_terms = []

    for i in range(start, len(term_dictionary)):

        term = term_dictionary[i]

        if term.startswith(prefix):
            matching_terms.append(term)

        else:
            # Since dictionary is sorted,
            # no later term can start with prefix
            break

    return matching_terms


# ============================================================
# 5. SUFFIX SEARCH
#    Example: *ing
# ============================================================

def suffix_search(suffix):

    suffix = suffix.lower()

    matching_terms = []

    for term in term_dictionary:

        if term.endswith(suffix):
            matching_terms.append(term)

    return matching_terms


# ============================================================
# 6. BUILD PERMUTERM INDEX
# ============================================================

permuterm_index = {}

for term in term_dictionary:

    # Add end-of-word symbol
    word = term + "$"

    # Generate every rotation
    for i in range(len(word)):

        rotation = word[i:] + word[:i]

        if rotation not in permuterm_index:
            permuterm_index[rotation] = []

        permuterm_index[rotation].append(term)


# ============================================================
# 7. PERMUTERM SEARCH
#    Example: comp*er
# ============================================================

def permuterm_search(query):

    query = query.lower()

    # Only one wildcard is supported
    if query.count("*") != 1:
        raise ValueError("Query must contain exactly one *")

    # Middle wildcard only
    if query.startswith("*") or query.endswith("*"):
        raise ValueError(
            "Permuterm search here is for a wildcard in the middle"
        )

    # Split query around *
    left, right = query.split("*")

    # Example:
    # comp*er
    #
    # left  = comp
    # right = er
    #
    # transformed = er$comp

    transformed = right + "$" + left

    matching_terms = set()

    # Search rotations
    for rotation, terms in permuterm_index.items():

        if rotation.startswith(transformed):

            matching_terms.update(terms)

    return transformed, sorted(matching_terms)


# ============================================================
# 8. GET DOCUMENT IDs FOR MATCHING TERMS
# ============================================================

def get_documents(matching_terms):

    result = set()

    for term in matching_terms:

        result.update(inverted_index[term])

    return sorted(result)


# ============================================================
# 9. TEST PREFIX QUERY
# ============================================================

print("\n==============================")
print("PREFIX SEARCH")
print("==============================")

query = "comp*"

prefix = query[:-1]

matching_terms = prefix_search(prefix)

print("Query:", query)
print("Matching terms:", matching_terms)
print("Document IDs:", get_documents(matching_terms))


# ============================================================
# 10. TEST SUFFIX QUERY
# ============================================================

print("\n==============================")
print("SUFFIX SEARCH")
print("==============================")

query = "*ing"

suffix = query[1:]

matching_terms = suffix_search(suffix)

print("Query:", query)
print("Matching terms:", matching_terms)
print("Document IDs:", get_documents(matching_terms))


# ============================================================
# 11. TEST MIDDLE WILDCARD
# ============================================================

print("\n==============================")
print("PERMUTERM SEARCH")
print("==============================")

query = "comp*er"

transformed, matching_terms = permuterm_search(query)

print("Query:", query)
print("Transformed query:", transformed)
print("Matching terms:", matching_terms)
print("Document IDs:", get_documents(matching_terms))
