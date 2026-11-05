# **How Transformer LLMs Work**

Instructors: Jay Alammar, Maarten Grootendorst

Co-authors of "**Hands-On Large Language Models**"

## What you'll learn

* Gain an understanding of the key components of transformers, including tokenization, embeddings, self-attention, and transformer blocks, to build a strong technical foundation.

* Understand recent transformer improvements to the attention mechanism such as KV cache, multi-query attention, grouped query attention, and sparse attention.

* Compare tokenization strategies used in modern LLMS and explore transformers in the Hugging Face Transformers library.

## About this course

Introducing “**How Transformer LLMs Work**”, created with Jay Alammar and Maarten Grootendorst, authors of the “*Hands-On Large Language Models*” book. This course offers a deep dive into the main components of the transformer architecture that powers Large Language Models (LLMs).

The transformer architecture revolutionized generative AI. In fact, the “GPT” in ChatGPT stands for “Generative Pre-Trained Transformer.”

Originally introduced in the groundbreaking 2017 paper *Attention Is All You Need*, by Ashish Vaswani and others, transformers were a highly scalable model for machine translation tasks. Variants of this architecture now power today’s LLMs such as those from OpenAI, Google, Meta, Cohere, and Anthropic.

In their book, Jay and Maarten beautifully illustrated the underlying architecture of LLMs through insightful and easy-to-understand explanations.

In this course, you’ll learn how a transformer network architecture that powers LLMs works. You’ll build the intuition of how LLMs process text and work with code examples that illustrate the key components of the transformer architecture.

Key topics covered in this course include:
* The evolution of how language has been represented numerically, from the Bag-of-Words model through Word2Vec embeddings to the transformer architecture that captures word meanings in full context.
* How LLM inputs are broken down into tokens, which represent words or pieces before they are sent to the language model.
* The details of a transformer and the three main stages, consisting of tokenization and embedding, the stack of transformer blocks, and the language model head.
* The details of the transformer block, including attention, which calculates relevance scores followed by the feedforward layer, which incorporates stored information learned in training.
* How cached calculations make transformers faster, how the transformer block has evolved over the years since the original paper was released, and how they continue to be widely used.
* Explore an implementation of recent models in the Hugging Face transformer library.

By the end of this course, you’ll have a deep understanding of how LLMs process language and you’ll be able to read through papers describing models and understand the details that are used to describe these architectures. This intuition will help improve your approach to building LLM applications.

## Who should join?

Anyone interested in understanding the inner workings of transformer architectures that power today’s LLMs.

## Contents

* How Transformer LLMs Work ![10%](https://geps.dev/progress/10) [![Open in GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white&style=flat)](How_Transformer_LLMs_Work.ipynb) [![Open in nbviewer](https://img.shields.io/badge/Jupyter%20nbviewer-F37626?logo=jupyter&logoColor=white&style=flat)](https://nbviewer.org/github/ancilcleetus/AI-Learning-Lab/blob/main/Generative-AI/How-Transformer-LLMs-Work/How_Transformer_LLMs_Work.ipynb) [![Open in Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white&style=flat)](https://colab.research.google.com/github/ancilcleetus/AI-Learning-Lab/blob/main/Generative-AI/How-Transformer-LLMs-Work/How_Transformer_LLMs_Work.ipynb)

## References
* **[DeepLearning.AI: How Transformer LLMs Work Course](https://www.deeplearning.ai/courses/how-transformer-llms-work)**