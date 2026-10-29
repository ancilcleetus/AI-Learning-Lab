# **NLP Foundations**

Welcome to the **NLP Foundations** module of the AI Learning Lab. This learning track is structured to build a rigorous, production-grade intuition for Natural Language Processing.

This module begins at the foundational vector representation of words, moves systematically through sequence models, and culminates in the structural design of the Transformer architecture and pre-LLM transfer learning models.

## Phase 1: Word Embeddings (Representing Words)

### Word Embeddings ![100%](https://geps.dev/progress/100) [![Open in GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white&style=flat)](Word_Embeddings.ipynb) [![Open in nbviewer](https://img.shields.io/badge/Jupyter%20nbviewer-F37626?logo=jupyter&logoColor=white&style=flat)](https://nbviewer.org/github/ancilcleetus/AI-Learning-Lab/blob/main/NLP/NLP-Foundations/Word_Embeddings.ipynb) [![Open in Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white&style=flat)](https://colab.research.google.com/github/ancilcleetus/AI-Learning-Lab/blob/main/NLP/NLP-Foundations/Word_Embeddings.ipynb)

### Word2Vec ![100%](https://geps.dev/progress/100) [![Open in GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white&style=flat)](Word2Vec.ipynb) [![Open in nbviewer](https://img.shields.io/badge/Jupyter%20nbviewer-F37626?logo=jupyter&logoColor=white&style=flat)](https://nbviewer.org/github/ancilcleetus/AI-Learning-Lab/blob/main/NLP/NLP-Foundations/Word2Vec.ipynb) [![Open in Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white&style=flat)](https://colab.research.google.com/github/ancilcleetus/AI-Learning-Lab/blob/main/NLP/NLP-Foundations/Word2Vec.ipynb)

### Illustrated Word2Vec ![10%](https://geps.dev/progress/10) [![Open in GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white&style=flat)](Illustrated_Word2Vec.ipynb) [![Open in nbviewer](https://img.shields.io/badge/Jupyter%20nbviewer-F37626?logo=jupyter&logoColor=white&style=flat)](https://nbviewer.org/github/ancilcleetus/AI-Learning-Lab/blob/main/NLP/NLP-Foundations/Illustrated_Word2Vec.ipynb) [![Open in Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white&style=flat)](https://colab.research.google.com/github/ancilcleetus/AI-Learning-Lab/blob/main/NLP/NLP-Foundations/Illustrated_Word2Vec.ipynb)

### GloVe ![10%](https://geps.dev/progress/10) [![Open in GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white&style=flat)](GloVe.ipynb) [![Open in nbviewer](https://img.shields.io/badge/Jupyter%20nbviewer-F37626?logo=jupyter&logoColor=white&style=flat)](https://nbviewer.org/github/ancilcleetus/AI-Learning-Lab/blob/main/NLP/NLP-Foundations/GloVe.ipynb) [![Open in Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white&style=flat)](https://colab.research.google.com/github/ancilcleetus/AI-Learning-Lab/blob/main/NLP/NLP-Foundations/GloVe.ipynb)

## 🧭 Syllabus & Core Learning Resources

### Phase 1: Word Embeddings (Representing Words)
Learn how text is mapped into continuous mathematical vector spaces, capturing structural and semantic relationships.

*   **Topic 1: Distributional Semantics & Word Vectors**
    *   *Lena Voita (Core Structure):* [Word Embeddings: Introduction & Distributional Semantics](http://github.io)
*   **Topic 2: Word2Vec Framework (Skip-gram & CBOW)**
    *   *Lena Voita:* [Word Embeddings: Word2Vec (Skip-gram, CBOW, Negative Sampling)](http://github.io)
    *   *Jay Alammar:* [The Illustrated Word2vec (Visualizing Embeddings)](https://jalammar.github.io/illustrated-word2vec/)
*   **Topic 3: Matrix Factorization & Subword Modeling (GloVe & FastText)**
    *   *Lena Voita:* [Word Embeddings: GloVe & FastText](http://github.io)

### Phase 2: Text Classification
Foundational supervised machine learning concepts applied to textual datasets, evaluation methodologies, and baseline classification setups.

*   **Topic 4: Evaluation Metrics & Classic Classification Architectures**
    *   *Lena Voita (Core Structure):* [Text Classification (Metrics, Naive Bayes, MaxEnt, Neural Networks)](http://github.io)

### Phase 3: Language Modeling
Understanding probability distributions over sequences of words to effectively score and generate natural text.

*   **Topic 5: N-Grams, Neural Language Models, & Generation Strategies**
    *   *Lena Voita (Core Structure):* [Language Modeling (Count-based, Neural LMs, Perplexity, Sampling)](http://github.io)

### Phase 4: Sequence Modeling (Recurrent Neural Networks)
Transitioning into time-series architectures engineered to maintain temporal hidden states across variable-length token inputs.

*   **Topic 6: RNNs, GRUs, & Long Short-Term Memory (LSTM) Nets**
    *   *Lena Voita (Core Structure):* [Models: Recurrent Neural Networks](http://github.io)
    *   *Christopher Olah:* [Understanding LSTM Networks](https://github.io)

### Phase 5: Sequence-to-Sequence Models & Attention Mechanics
The architectural bridge to the Transformer era: passing encoded sequence information into decoder networks using dynamic soft alignment.

*   **Topic 7: Classical Seq2Seq and the Attention Breakthrough**
    *   *Lena Voita (Core Structure):* [Seq2Seq and Attention (NMT, Bahdanau/Luong Attention)](http://github.io)
    *   *Jay Alammar:* [Visualizing A Neural Machine Translation Model (Mechanics of Seq2seq Models With Attention)](https://github.io)

### Phase 6: The Transformer Architecture
Removing computational recurrence in favor of mass-parallelized sequence attention steps.

*   **Topic 8: High-Level Core Transformer & Self-Attention Concepts**
    *   *Aqeel Anwar:* [Animation is All You Need – Part 1: A Visual Guide to Understanding Transformers](https://medium.com)
    *   *Jay Alammar:* [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
*   **Topic 9: Granular Mathematical Details & Implementation Logic**
    *   *Lena Voita (Core Structure):* [Models: The Transformer Architecture](http://github.io)
    *   *Harvard NLP Group:* [The Annotated Transformer (PyTorch Code Walkthrough)](https://annotated-transformer.github.io/)

### Phase 7: Transfer Learning & Pre-LLM Token Contextualization
Understanding how the industry shifted from static lookups to dynamic, context-aware embeddings before modern autoregressive scaling took off.

*   **Topic 10: Early Contextualized Embeddings & Masked Architectures (BERT)**
    *   *Lena Voita (Core Structure):* [Transfer Learning (Fine-tuning, BERT, Contextual Embeddings)](http://github.io)
    *   *Jay Alammar:* [The Illustrated BERT, ELMo, and co. (How NLP Cracked Transfer Learning)](https://jalammar.github.io/illustrated-bert/)

