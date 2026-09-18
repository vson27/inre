























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































# Text docs
docs = [
    "machine learning improves medical image analysis"
]


tokenized_docs = [doc.lower().split() for doc in docs]

vocab = []
for tokens in tokenized_docs:
    for word in tokens:
        if word not in vocab:
            vocab.append(word)
vocab.sort()

print(f"{'Term':<15} | D1 D2 D3 D4 D5 D6")
print("-" * 35)

for term in vocab:
    row = [1 if term in tokens else 0 for tokens in tokenized_docs]
    print(f"{term:<15} | {'  '.join(map(str, row))}")


permuterm_index = {}
for term in vocab:
    term_dollar = term + "$"
    for i in range(len(term_dollar)):
        rotated = term_dollar[i:] + term_dollar[:i]
        permuterm_index[rotated] = term

def permuterm_search(wc):
    qd = wc + "$"
    star_idx = qd.index('*')
    srch_pre = qd[star_idx + 1:] + qd[:star_idx]
    
    matched_terms = []
    pre_len = len(srch_pre)
    
    for key, original_term in permuterm_index.items():
        if key[:pre_len] == srch_pre:
            if original_term not in matched_terms:
                matched_terms.append(original_term)
                
    return matched_terms

print("\n--- Permuterm Index Search Example ---")
print("Query 'm*l' matches:", permuterm_search("m*l"))
print("Query 'diag*' matches:", permuterm_search("diag*"))

=================================================================

# inverted index
docs = {
  'D1': '',
  'D2': '',

}

inverted_index = {}
for doc_id, text in docs.items():
    tokens = text.lower().split()
    for token in tokens:
        if token not in inverted_index:
            inverted_index[token] = []
        if doc_id not in inverted_index[token]:
            inverted_index[token].append(doc_id)

vocab = []
for term in inverted_index:
    vocab.append(term)
vocab.sort()

print("Inverted Index & Document Frequency:")
print("-" * 45)
for term in vocab:
    doc_ids = inverted_index[term]
    doc_ids.sort()
    df = len(doc_ids)
    print(f"{term:<15}-> {str(doc_ids):<20} DF = {df}")


==========================================================================

# permuterm indexing
docs = {
    "D1": " ",
    "D2": " ",

}

doc_index = {}
for d_id, text in docs.items():
    for word in text.lower().split():
        if word not in doc_index: doc_index[word] = []
        if d_id not in doc_index[word]: doc_index[word].append(d_id)

perm_index = {}
for word in doc_index:
    w_dollar = word + "$"
    for i in range(len(w_dollar)):
        perm_index[w_dollar[i:] + w_dollar[:i]] = word

for q in ["digital*", "*ing", "comp*al", "docu*ent", "auto*ic"]:
    q_dollar = q + "$"
    star_pos = q_dollar.index('*')
    prefix = q_dollar[star_pos + 1:] + q_dollar[:star_pos]
    
    words = []
    for key, w in perm_index.items():
        if key[:len(prefix)] == prefix and w not in words:
            words.append(w)
            
    matched_docs = []
    for w in words:
        for d in doc_index[w]:
            if d not in matched_docs: matched_docs.append(d)
    matched_docs.sort()
    
    print(f"Query: {q}\nSearch Prefix: {prefix}\nWords: {words}\nDocs: {matched_docs}\n")

====================================================================================================

#Boolean AND

docs = {
    "D1": " ",
    "D2": " "
}

doc_index = {}
for d_id, text in docs.items():
    for word in text.lower().split():
        if word not in doc_index: doc_index[word] = []
        if d_id not in doc_index[word]: doc_index[word].append(d_id)

def boolean_and(word1, word2):
    list1 = doc_index.get(word1, [])
    list2 = doc_index.get(word2, [])
    
    result = []
    p1 = 0
    p2 = 0
    
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] == list2[p2]:
            result.append(list1[p1])
            p1 += 1
            p2 += 1
        elif list1[p1] < list2[p2]:
            p1 += 1
        else:
            p2 += 1
            
    return result

print("Query: digital AND systems")
print("Docs:", boolean_and("digital", "systems"))

print("\nQuery: computational AND analysis")
print("Docs:", boolean_and("computational", "analysis"))

=========================================================================


#Boolean OR and NOT 

docs = {
    "D1": " ",
    "D2": " "

}

doc_index = {}
for d_id, text in docs.items():
    for word in text.lower().split():
        if word not in doc_index: doc_index[word] = []
        if d_id not in doc_index[word]: doc_index[word].append(d_id)

def boolean_or(word1, word2):
    list1 = doc_index.get(word1, [])
    list2 = doc_index.get(word2, [])
    result = []
    p1, p2 = 0, 0
    
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] == list2[p2]:
            result.append(list1[p1])
            p1 += 1; p2 += 1
        elif list1[p1] < list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
            
    while p1 < len(list1):
        result.append(list1[p1])
        p1 += 1
    while p2 < len(list2):
        result.append(list2[p2])
        p2 += 1
        
    return result

def boolean_and_not(word1, word2):
    list1 = doc_index.get(word1, [])
    list2 = doc_index.get(word2, [])
    result = []
    p1, p2 = 0, 0
    
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] == list2[p2]:
            p1 += 1; p2 += 1
        elif list1[p1] < list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            p2 += 1
            
    while p1 < len(list1):
        result.append(list1[p1])
        p1 += 1
        
    return result

print("Query: digital OR computational")
print("Docs:", boolean_or("digital", "computational"))

print("\nQuery: systems AND NOT digital")
print("Docs:", boolean_and_not("systems", "digital"))

================================================================

#Query Optimization
df = {
    "information": 500, 
    "retrieval": 120, 
    "system": 800, 
    "query": 250, 
    "optimization": 50
}

postings = {
    "information": [10, 20, 30, 40, 50],
    "retrieval": [10, 20, 30],
    "system": [10, 20, 30, 40, 50, 60],
    "query": [20, 30, 40],
    "optimization": [20, 30]
}

def intersect(l1, l2):
    res, p1, p2 = [], 0, 0
    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] == l2[p2]:
            res.append(l1[p1])
            p1 += 1; p2 += 1
        elif l1[p1] < l2[p2]: p1 += 1
        else: p2 += 1
    return res

q = ["information", "retrieval", "system", "query", "optimization"]
q.sort(key=lambda t: df[t])

print("Optimized Order:", q)

res = postings[q[0]]
for i in range(1, len(q)):
    res = intersect(res, postings[q[i]])

print("Matching Docs:", res)

======================================================================

#Skip Pointers

P1 = [2, 4, 8, 16, 32, 64, 128, 256]
P2 = [4, 8, 16, 20, 32, 64, 100, 128, 200, 256]

def standard_and(l1, l2):
    res, comps, p1, p2 = [], 0, 0, 0
    while p1 < len(l1) and p2 < len(l2):
        comps += 1
        if l1[p1] == l2[p2]:
            res.append(l1[p1])
            p1 += 1; p2 += 1
        elif l1[p1] < l2[p2]: p1 += 1
        else: p2 += 1
    return res, comps

def skip_and(l1, l2):
    res, comps, p1, p2 = [], 0, 0, 0
    s1, s2 = int(len(l1)**0.5), int(len(l2)**0.5)
    while p1 < len(l1) and p2 < len(l2):
        comps += 1
        if l1[p1] == l2[p2]:
            res.append(l1[p1])
            p1 += 1; p2 += 1
        elif l1[p1] < l2[p2]:
            skip = (p1 % s1 == 0) and (p1 + s1 < len(l1))
            if skip: comps += 1
            if skip and l1[p1 + s1] <= l2[p2]: p1 += s1
            else: p1 += 1
        else:
            skip = (p2 % s2 == 0) and (p2 + s2 < len(l2))
            if skip: comps += 1
            if skip and l2[p2 + s2] <= l1[p1]: p2 += s2
            else: p2 += 1
    return res, comps

res_std, comp_std = standard_and(P1, P2)
res_skip, comp_skip = skip_and(P1, P2)

print("Standard Intersection:", res_std)
print("Standard Comparisons:", comp_std)
print("Skip Intersection:", res_skip)
print("Skip Comparisons:", comp_skip)



=======================================================================================

#Biword Index

docs = {
    "D1": "information retrieval is an important field",
    "D2": "information retrieval system improves search",
    "D3": "retrieval system optimization improves performance",
    "D4": "information system provides efficient retrieval",
    "D5": "information retrieval system optimization"
}

idx = {}
for d, txt in docs.items():
    t = txt.lower().split()
    for i in range(len(t)-1):
        bw = f"{t[i]} {t[i+1]}"
        if bw not in idx: idx[bw] = []
        if d not in idx[bw]: idx[bw].append(d)

print("--- Biword Index ---")
for b, p in idx.items(): 
    print(f"{b:<25}: {p}")

print("\n--- Query Results ---")
for q in ["information retrieval", "retrieval system", "system optimization", "information retrieval system"]:
    t = q.lower().split()
    bws = [f"{t[i]} {t[i+1]}" for i in range(len(t)-1)]
    
    res = idx.get(bws[0], []) if bws else []
    for b in bws[1:]:
        res = [d for d in res if d in idx.get(b, [])]
        
    print(f"Query: '{q}'\nBiwords: {bws}\nDocs: {res}\n")

=====================================================================

# Text Preprocessing using Stemming, Lemmatization and Stop-word Removal

docs = {
    "D1": "The students are studying information retrieval techniques.",
    "D2": "Students studied different retrieval techniques for searching information.",
    "D3": "The system retrieves relevant documents and provides better results.",
    "D4": "Searching and retrieving documents are important tasks in information retrieval."
}

stops = {"the", "are", "is", "and", "for", "in", "of", "to", "a"}

def stem(w):
    for suffix, replacement in [('ying', 'i'), ('ied', 'i'), ('ing', ''), ('es', ''), ('s', '')]:
        if w.endswith(suffix) and len(w) > 4:
            return w[:-len(suffix)] + replacement
    return w

lemma_dict = {
    "students": "student", "studying": "study", "techniques": "technique",
    "studied": "study", "searching": "search", "retrieves": "retrieve",
    "documents": "document", "provides": "provide", "results": "result",
    "retrieving": "retrieve", "tasks": "task"
}
def lem(w): return lemma_dict.get(w, w)

def process(txt):
    t = txt.lower().replace('.', '').split()
    ns = [w for w in t if w not in stops]
    return txt, t, ns, [stem(w) for w in ns], [lem(w) for w in ns]

for d, txt in docs.items():
    o, t, ns, s, l = process(txt)
    print(f"{d}\nOrig: {o}\nToks: {t}\nNoStop: {ns}\nStem: {s}\nLem: {l}\n")

print("--- Comparison ---")
for w in ["studying", "studied", "searching", "retrieves", "retrieving", "documents"]:
    print(f"{w:<12} Stem: {stem(w):<12} Lem: {lem(w)}")

def user_query(q):
    o, t, ns, s, l = process(q)
    print(f"\nUser Query: {o}\nToks: {t}\nNoStop: {ns}\nStem: {s}\nLem: {l}")

user_query("The students are retrieving documents for the system.")

========================================================================================

# Phrase Queries Using Positional Index

docs = {
    "D1": " ",
    "D2": " ",

}

pos_idx = {}
for d, txt in docs.items():
    toks = txt.lower().replace('.', '').replace(',', '').split()
    for i, w in enumerate(toks):
        if w not in pos_idx: pos_idx[w] = {}
        if d not in pos_idx[w]: pos_idx[w][d] = []
        pos_idx[w][d].append(i)

q = "information retrieval".lower().split()
res = []

if q[0] in pos_idx and q[1] in pos_idx:
    for d, p1_list in pos_idx[q[0]].items():
        if d in pos_idx[q[1]]:
            p2_list = pos_idx[q[1]][d]
            match = False
            for p1 in p1_list:
                for p2 in p2_list:
                    if p2 == p1 + 1:
                        match = True
            if match and d not in res:
                res.append(d)

print("Positional Index for 'information':")
print(pos_idx["information"])
print("\nPositional Index for 'retrieval':")
print(pos_idx["retrieval"])

print("\nQuery: 'information retrieval'")
print("Matched Docs:", res)


=====================================================================================================

# wildcard query processing

docs = {
    1: " ",
    2: " ",
}

idx = {}
for d, txt in docs.items():
    for w in txt.lower().split():
        if w not in idx: idx[w] = []
        if d not in idx[w]: idx[w].append(d)

vocab = []
for w in idx: vocab.append(w)
vocab.sort()

perm = {}
for w in vocab:
    w_dollar = w + "$"
    for i in range(len(w_dollar)):
        perm[w_dollar[i:] + w_dollar[:i]] = w

def wildcard_search(q):
    trms = []
    
    if q[-1] == '*': 
        pfx = q[:-1]
        for w in vocab:
            if w[:len(pfx)] == pfx and w not in trms: 
                trms.append(w)
                
    elif q[0] == '*': 
        sfx = q[1:]
        for w in vocab:
            if len(w) >= len(sfx) and w[-len(sfx):] == sfx and w not in trms: 
                trms.append(w)
                
    else: 
        q_dollar = q + "$"
        star = q_dollar.index('*')
        pfx = q_dollar[star + 1:] + q_dollar[:star]
        for k, v in perm.items():
            if k[:len(pfx)] == pfx and v not in trms: 
                trms.append(v)
                
    dids = []
    for t in trms:
        for d in idx[t]:
            if d not in dids: dids.append(d)
    dids.sort()
    
    return trms, dids

queries = ["comp*", "*ing", "comp*er", "infor*tion", "learn*ng"]

for q in queries:
    t, d = wildcard_search(q)
    print(f"Query: {q}\nTerms: {t}\nDocs: {d}\n")
