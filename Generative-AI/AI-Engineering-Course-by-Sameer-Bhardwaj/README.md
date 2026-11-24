# **AI Engineering Course by Sameer Bhardwaj**

## What you'll learn

Learn to build production AI applications with Large Language Models; prompting, retrieval, agents, evals, security and cost.

## What you'll be able to do

Build AI features that hold up in production. One running project: a support assistant for Nimbus, an imaginary payments platform. Each step adds a capability, from how models work to agents and deployment.

1. **Reason about cost and speed**: Estimate what a request costs and why it's slow, from tokens, context windows and prompt caching.
2. **Get output your code can rely on**: Write prompts that hold up, and enforce structured output with JSON schemas instead of hoping for it.
3. **Answer from your own documents**: Build retrieval end to end: chunking, vector search and grounding, so answers come from your docs.
4. **Measure retrieval instead of guessing**: Build an eval set, compare setups with recall@k, and combine keyword and vector search with RRF and reranking.
5. **Judge answers and find what failed**: Score answers with LLM-as-a-judge, trace a request stage by stage, and catch confident wrong answers.
6. **Build agents you can control**: Decide when you need an agent, keep its loop bounded, manage its memory, and evaluate whole trajectories.
7. **Ship it**: Secure tools against prompt injection, see where the money goes, pick models from your own evals, and deploy.

## Who this course is for

Software developers who want to build AI features that work in production.

## Contents

* [Module 01: Foundations](Module-01-Foundations)
    * Tokens ![10%](https://geps.dev/progress/10) [![Open in GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white&style=flat)](Module-01-Foundations/01_Tokens.ipynb) [![Open in nbviewer](https://img.shields.io/badge/Jupyter%20nbviewer-F37626?logo=jupyter&logoColor=white&style=flat)](https://nbviewer.org/github/ancilcleetus/AI-Learning-Lab/blob/main/Generative-AI/AI-Engineering-Course-by-Sameer-Bhardwaj/Module-01-Foundations/01_Tokens.ipynb) [![Open in Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white&style=flat)](https://colab.research.google.com/github/ancilcleetus/AI-Learning-Lab/blob/main/Generative-AI/AI-Engineering-Course-by-Sameer-Bhardwaj/Module-01-Foundations/01_Tokens.ipynb)
    * Context Windows ![10%](https://geps.dev/progress/10) [![Open in GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white&style=flat)](Module-01-Foundations/02_Context_Windows.ipynb) [![Open in nbviewer](https://img.shields.io/badge/Jupyter%20nbviewer-F37626?logo=jupyter&logoColor=white&style=flat)](https://nbviewer.org/github/ancilcleetus/AI-Learning-Lab/blob/main/Generative-AI/AI-Engineering-Course-by-Sameer-Bhardwaj/Module-01-Foundations/02_Context_Windows.ipynb) [![Open in Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white&style=flat)](https://colab.research.google.com/github/ancilcleetus/AI-Learning-Lab/blob/main/Generative-AI/AI-Engineering-Course-by-Sameer-Bhardwaj/Module-01-Foundations/02_Context_Windows.ipynb)
    * Vector Embeddings ![10%](https://geps.dev/progress/10) [![Open in GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white&style=flat)](Module-01-Foundations/03_Vector_Embeddings.ipynb) [![Open in nbviewer](https://img.shields.io/badge/Jupyter%20nbviewer-F37626?logo=jupyter&logoColor=white&style=flat)](https://nbviewer.org/github/ancilcleetus/AI-Learning-Lab/blob/main/Generative-AI/AI-Engineering-Course-by-Sameer-Bhardwaj/Module-01-Foundations/03_Vector_Embeddings.ipynb) [![Open in Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white&style=flat)](https://colab.research.google.com/github/ancilcleetus/AI-Learning-Lab/blob/main/Generative-AI/AI-Engineering-Course-by-Sameer-Bhardwaj/Module-01-Foundations/03_Vector_Embeddings.ipynb)
    * Transformer Architecture ![10%](https://geps.dev/progress/10) [![Open in GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white&style=flat)](Module-01-Foundations/04_Transformer_Architecture.ipynb) [![Open in nbviewer](https://img.shields.io/badge/Jupyter%20nbviewer-F37626?logo=jupyter&logoColor=white&style=flat)](https://nbviewer.org/github/ancilcleetus/AI-Learning-Lab/blob/main/Generative-AI/AI-Engineering-Course-by-Sameer-Bhardwaj/Module-01-Foundations/04_Transformer_Architecture.ipynb) [![Open in Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white&style=flat)](https://colab.research.google.com/github/ancilcleetus/AI-Learning-Lab/blob/main/Generative-AI/AI-Engineering-Course-by-Sameer-Bhardwaj/Module-01-Foundations/04_Transformer_Architecture.ipynb)
    * Prompt Caching ![10%](https://geps.dev/progress/10) [![Open in GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white&style=flat)](Module-01-Foundations/05_Prompt_Caching.ipynb) [![Open in nbviewer](https://img.shields.io/badge/Jupyter%20nbviewer-F37626?logo=jupyter&logoColor=white&style=flat)](https://nbviewer.org/github/ancilcleetus/AI-Learning-Lab/blob/main/Generative-AI/AI-Engineering-Course-by-Sameer-Bhardwaj/Module-01-Foundations/05_Prompt_Caching.ipynb) [![Open in Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white&style=flat)](https://colab.research.google.com/github/ancilcleetus/AI-Learning-Lab/blob/main/Generative-AI/AI-Engineering-Course-by-Sameer-Bhardwaj/Module-01-Foundations/05_Prompt_Caching.ipynb)
    * How LLMs are Trained ![10%](https://geps.dev/progress/10) [![Open in GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white&style=flat)](Module-01-Foundations/06_How_LLMs_are_Trained.ipynb) [![Open in nbviewer](https://img.shields.io/badge/Jupyter%20nbviewer-F37626?logo=jupyter&logoColor=white&style=flat)](https://nbviewer.org/github/ancilcleetus/AI-Learning-Lab/blob/main/Generative-AI/AI-Engineering-Course-by-Sameer-Bhardwaj/Module-01-Foundations/06_How_LLMs_are_Trained.ipynb) [![Open in Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white&style=flat)](https://colab.research.google.com/github/ancilcleetus/AI-Learning-Lab/blob/main/Generative-AI/AI-Engineering-Course-by-Sameer-Bhardwaj/Module-01-Foundations/06_How_LLMs_are_Trained.ipynb)
* [Module 02: Prompting-and-Retrieval](Module-02-Prompting-and-Retrieval)
* [Module 03: Measuring-and-Improving](Module-03-Measuring-and-Improving)
* [Module 04: Agents](Module-04-Agents)
* [Module 05: Production](Module-05-Production)

## References
* **[TopEngineer: AI Engineering Course by Sameer Bhardwaj](https://www.topengineer.dev/)**
