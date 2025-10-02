# Analyzing the runtime of different algorithms for measuring document similarity 

# The Brief  

We investigate the running time of different algorithms for measuring similarities between pairs of documents in a collection. Our work focuses on five key questions, explored and documented within a single Jupyter Notebook that includes a brief introduction, analysis, and closing discussion.  

The dataset is a **word-frequency matrix** extracted from Herman Melville’s *Moby Dick*, where:  
- **Columns** represent documents  
- **Rows** represent words  
- **Entries** indicate the frequency of each word in each document  

To evaluate how algorithm run-times scale with data size, we experiment with:  
- Subsets of the data matrix (removing rows/columns)  
- Replicating columns to create larger datasets  

---

# Questions  

1. **Cosine Similarity**  
   - Present an analysis of the theoretical running time of the cosine similarity measure applied to a pair of documents.  
   - Test this empirically by timing and plotting calculations on your computer.  
   - Estimate the key constant in the run-time formula for your implementation.  
   - Compare the dot product in NumPy with a custom implementation.  

2. **Jaccard Similarity**  
   - Present an analysis of the theoretical running time of Jaccard’s similarity measure applied to a pair of documents.  
   - Test empirically with timing and plotting.  
   - Estimate the key constant in the run-time formula.  

3. **All-Pairs Similarity**  
   - Analyze the theoretical worst-case running time for computing all-pairs similarities on the data matrix.  
   - Discuss whether the similarity measure (Jaccard vs. Cosine) makes a difference.  
   - Estimate the key constants for both Jaccard and Cosine similarity.  

4. **Parallel Computing**  
   - Implement all-pairs similarities for one similarity measure using parallel computing.  
   - Analyze theoretically and empirically the achievable speed-up on your computer.  

5. **Strassen’s Method**  
   - Investigate the efficiency of computing all-pairs cosine similarities using Strassen’s method for matrix multiplication.  
   - Test empirically and discuss findings in relation to theory.  

---

