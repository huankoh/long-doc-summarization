# An Empirical Survey on Long Document Summarization



![Stars](https://img.shields.io/github/stars/huankoh/long-doc-summarization?color=yellow)

A collection of papers and resources across three principal components of long document summarization: Datasets, Models and Metrics.

**<u>To-do List :running: : <u>**

- [x] Y22 Dataset
- [x] Y22 Models (ACL and NAACL updated)
- [ ] Y22 Metrics (Will be updated before: 20/07/22)
- [ ] Other Settings (Ongoing)

## Contents


- [Fundamentals](#fundamentals)
- [Papers](#papers)
  - [Datasets](#datasets)
  - [Models](#models)
	  - [Abstractive Summarization](#abs-summ)
	  - [Extractive Summarization](#ext-summ)
	  - [Hybrid Summarization](#hybrid-summ)
	  - [Unsupervised Abstractive Summarization](#uns-abs-summ)
	  - [Unsupervised Extractive Summarization](#uns-abs-summ)
  - [Metrics](#metrics) 
  	  - [Relevance](#rel)
	  - [Factual Consistency](#fact)
  - [Insightful Discussions](#insights)
- [Our Survey](#survey)


<a name="fundamentals" />

## Fundamentals
### Long Document Summarization 
1. **An Empirical Survey on Long Document Summarization: Datasets, Models and Metrics.** *Huan Yee Koh, Jiaxin Ju, Ming Liu, Shirui Pan.* 2022. `ACM Comput. Surv.`  [paper](https://dl.acm.org/doi/10.1145/3545176)
2.  **Automatic summarization of scientific articles: A survey** *Nouf Ibrahim Altmami, Mohamed El Bachir Menai.* 2020. `Journal of King Saud University - Computer and Information Sciences` [[paper]](https://www.sciencedirect.com/science/article/pii/S1319157820303554)

### General Automatic Summarization 
1. **From Standard Summarization to New Tasks and Beyond: Summarization with Manifold Information** *Shen Gao, Xiuying Chen, Zhaochun Ren, Dongyan Zhao, Rui Yan.* 2020. `IJCAI` [[paper]](https://arxiv.org/abs/2005.04684)
2. **Neural Abstractive Text Summarization with Sequence-to-Sequence Models** *Tian Shi, Yaser Keneshloo, Naren Ramakrishnan, Chandan K. Reddy.* 2019. `ACM/IMS Transactions on Data Science` [[paper]](https://arxiv.org/abs/1812.02303)
3. **Neural Text Summarization: A Critical Evaluation**  *Wojciech Kryściński, Nitish Shirish Keskar, Bryan McCann, Caiming Xiong, Richard Socher.* 2019. `EMNLP` [[paper]](https://arxiv.org/abs/1908.08960)
4. **Text Summarization Techniques: A Brief Survey** *Mehdi Allahyari, Seyedamin Pouriyeh, Mehdi Assefi, Saeid Safaei, Elizabeth D. Trippe, Juan B. Gutierrez, Krys Kochut.* 2017. `IJACSA`[[paper]](https://arxiv.org/abs/1707.02268)
5. **Recent automatic text summarization techniques: a survey** *Mahak Gambhir, Vishal Gupta.* 2017. `Artif Intell Rev` [[paper]](https://link.springer.com/article/10.1007/s10462-016-9475-9)

<a name="papers" />


<a name="datasets" />

## Datasets 
|  **Dataset**  | **Year** | **Title**                                       |                          **tl;dr**                           |
| :--------: |:---- | :----------------------------------------------------------- | :----------------------------------------------------------: |
|  **arXiv**  | 2018 | A Discourse-Aware Attention Model for Abstractive Summarization of Long Documents `NAACL` [[Paper]](https://arxiv.org/abs/1804.05685) | Scientific |
|  **PubMed**  | 2018| A Discourse-Aware Attention Model for Abstractive Summarization of Long Documents `NAACL` [[Paper]](https://arxiv.org/abs/1804.05685)| Scientific |
| **BigPatent** | 2019 | BIGPATENT: A Large-Scale Dataset for Abstractive and Coherent Summarization `ACL` [[Paper]](https://arxiv.org/abs/1906.03741) | Business/Legal |
| **BillSum** | 2019 | BillSum: A Corpus for Automatic Summarization of US Legislation [[Paper]](https://arxiv.org/abs/1910.00523) | Legislative |
| **TLDR** | 2020 | TLDR: Extreme Summarization of Scientific Documents `ACL Findings` [[Paper]](https://arxiv.org/abs/2004.15011) | Scientific | 
| **CORD-19** | 2020 | CORD-19: The Covid-19 Open Research Dataset `ACL NLP-COVID Workshop` [[Paper]](https://arxiv.org/abs/2004.10706)  | Scientific |
| **FacetSum** | 2021 | Bringing Structure into Summaries: a Faceted Summarization Dataset for Long Scientific Documents [[Paper]](https://arxiv.org/abs/2106.00130) | Scientific | 
| **GovReport** | 2021 | Efficient Attentions for Long Document Summarization `NAACL` [[Paper]](https://arxiv.org/abs/2104.02112) | Legislative |
| **BookSum** | 2021 |  BookSum: A Collection of Datasets for Long-form Narrative Summarization [[Paper]](https://arxiv.org/abs/2105.08209) | General Literature |
| **SCROLLS** | 2022 | SCROLLS: Standardized CompaRison Over Long Language Sequences [[Paper]](https://arxiv.org/abs/2201.03533) | [Leaderboard](https://www.scrolls-benchmark.com/) | 

<a name="models" />

## Models

<a name="abs-summ" />

### Abstractive Summarization 

|  **Model**  | **Year** | **Title**                                       |                          **tl;dr**                           |
| :--------: |:---- | :----------------------------------------------------------- | :----------------------------------------------------------: |
|  **Discourse-RNN**  | 2018 |A Discourse-Aware Attention Model for Abstractive Summarization of Long Documents `NAACL` [[Paper]](https://arxiv.org/abs/1804.05685) | Hierarchical RNN + Sectional Bias |
|  **Longformer**  | 2020 | Longformer: The Long-Document Transformer [[Paper]](https://arxiv.org/abs/2004.05150) | Transformer + Efficient Attention | 
| **BigBird** | 2020 | Big Bird: Transformers for Longer Sequences `NeurIPS` [[Paper]](https://arxiv.org/abs/2007.14062) | Transformer + Efficient Attention |
| **FacetSum** | 2021 | Bringing Structure into Summaries: a Faceted Summarization Dataset for Long Scientific Documents [[Paper]](https://arxiv.org/abs/2106.00130) | Transformer + Prompt Engineering | 
| **GSUM** | 2021 | GSum: A General Framework for Guided Neural Abstractive Summarization [[Paper]](https://arxiv.org/abs/2010.08014) | Transformer + Signal Guidance |
|  **CRTLSum**  | 2021 | CTRLsum: Towards Generic Controllable Text Summarization [[Paper]](https://arxiv.org/abs/2012.04281) | Transformer + Prompt Engineering |
|  **HAT-BART**  | 2021 | Hierarchical Learning for Generation with Long Source Sequences [[Paper]](https://arxiv.org/abs/2104.07545) | Transformer + Hierarchical Attention |
|  **HEPOS**   | 2021 | Efficient Attentions for Long Document Summarization `NAACL` [[Paper]](https://arxiv.org/abs/2104.02112) | Transformer + Efficient Attention | 
| **DeepPyramidion** | 2022 | Sparsifying Transformer Models with Trainable Representation Pooling `ACL` [[Paper]](https://arxiv.org/abs/2009.05169) | Transformer + Efficient Attention | 
| **PRIMERA**| 2022 | PRIMERA: Pyramid-based Masked Sentence Pre-training for Multi-document Summarization `ACL` [[Paper]]() | Transformer + Multi-document Pre-training + Efficient Attention
| **HIBRIDS** | 2022 | HIBRIDS: Attention with Hierarchical Biases for Structure-aware Long Document Summarization `ACL` [[Paper]](https://arxiv.org/pdf/2203.10741.pdf) | Transformer + Discourse Bias Attention |  
| **LongT5** | 2022 | LongT5: Efficient Text-To-Text Transformer for Long Sequences `NAACL` [[Paper]](https://arxiv.org/abs/2112.07916) | Transformer + Long Document Pre-training + Efficient Attention |  
| **ECC** | 2022 | Improving the Faithfulness of Abstractive Summarization via Entity Coverage Control `NAACL Findings` [[Paper]](https://arxiv.org/abs/2207.02263) | Transformer + Factuality-Aware Fine-tuning | 

<a name="ext-summ" />

### Extractive Summarization 

|  **Model**  | **Year** | **Title**                                       |                          **tl;dr**                           |
| :--------: |:---- | :----------------------------------------------------------- | :----------------------------------------------------------: |
|  **GL-LSTM**  | 2019 | Extractive Summarization of Long Documents by Combining Global and Local Context `EMNLP-IJCNLP` [[Paper]](https://arxiv.org/abs/1909.08089) | Hierarchical RNN + Sectional Bias |
|  **Sent-CLF/PTR**  | 2019 | On extractive and abstractive neural document summarization with transformer language models `EMNLP` [[Paper]](https://arxiv.org/abs/1909.03186) | Hierarchical RNN | 
| **Topic-GraphSum** | 2020 | Enhancing Extractive Text Summarization with Topic-Aware Graph Neural Networks `COLING` [[Paper]](https://arxiv.org/abs/2007.14062) | Graph Attention Network + Topic Modelling |
| **SSN-DM** | 2021 |  Sliding Selector Network with Dynamic Memory for Extractive Summarization of Long Documents `NAACL` [[Paper]](https://aclanthology.org/2021.naacl-main.470/) | Memory Network |
| **MemSum** | 2022 | MemSum: Extractive Summarization of Long Documents Using Multi-Step Episodic Markov Decision Processes `ACL` [[Paper]](https://arxiv.org/abs/2107.08929) | RL-based extractor via Multi-step Episodic MDP | 
| **HiStruct+**| 2022 | HiStruct+: Improving Extractive Text Summarization with Hierarchical Structure Information `ACL Findings` [[Paper]](https://arxiv.org/abs/2203.09629) | Transformer + Discourse Bias Embeddings | 
| **TSTR** | 2022 | TSTR: Too Short to Represent, Summarize with Details! Intro-Guided Extended Summary Generation `NAACL` [[Paper]](https://arxiv.org/abs/2206.00847) | Transformer + Signal Guidance | 


<a name="hybrid-summ" />

### Hybrid Summarization 
|  **Model**  | **Year** | **Title**                                       |                          **tl;dr**                           |
| :--------: |:---- | :----------------------------------------------------------- | :----------------------------------------------------------: |
|  **TLM+Ext**  | 2019 | Extractive Summarization of Long Documents by Combining Global and Local Context `EMNLP-IJCNLP` [[Paper]](https://arxiv.org/abs/1909.08089) | Extract-then-Summarize |
|  **DANCER**  | 2019 | A Divide-and-Conquer Approach to the Summarization of Long Documents `IEEE/ACM Transactions on Audio, Speech, and Language Processing` [[Paper]](https://arxiv.org/abs/2004.06190) | Summarize-then-Combine | 
| **SEAL** | 2020 | SEAL: Segment-wise Extractive-Abstractive Long-form Text Summarization [[Paper]](https://arxiv.org/abs/2006.10213) | Extract-then-Summarize |
| **LoBART** | 2021 |  Long-Span Summarization via Local Attention and Content Selection `ACL` [[Paper]](https://arxiv.org/abs/2105.03801) | Extract-then-Summarize |
| **DYLE** | 2022 | DYLE: Dynamic Latent Extraction for Abstractive Long-Input Summarization `ACL` [[Paper]](https://arxiv.org/abs/2110.08168) | Extract-then-Summarize | 
| **Summ^N** | 2022 | Summ^N: A Multi-Stage Summarization Framework for Long Input Dialogues and Documents `ACL` [[Paper]](https://aclanthology.org/2022.acl-long.112.pdf) | Summarize-then-Summarize | 

<a name="uns-abs-summ" />

### Unsupervised Abstractive Summarization 
|  **Model**  | **Year** | **Title**                                       |                          **tl;dr**                           |
| :--------: |:---- | :----------------------------------------------------------- | :----------------------------------------------------------: |
|  **SciSummPip**  | 2020 | Monash-Summ@LongSumm 20 SciSummPip: An Unsupervised Scientific Paper Summarization Pipeline `Proceedings of the First Workshop on Scholarly Document Processing` [[Paper]](https://aclanthology.org/2020.sdp-1.37/) | Multi-sentence Compression |

<a name="uns-ext-summ" />

### Unsupervised Extractive Summarization 
|  **Model**  | **Year** | **Title**                                       |                          **tl;dr**                           |
| :--------: |:---- | :----------------------------------------------------------- | :----------------------------------------------------------: |
|  **PacSum**  | 2019 | Sentence Centrality Revisited for Unsupervised Summarization `ACL` [[Paper]](https://arxiv.org/abs/1906.03508) | Graph Centrality Scoring |
|  **HipoRank**  | 2020 | Discourse-Aware Unsupervised Summarization of Long Scientific Documents `EACL` [[Paper]](https://arxiv.org/abs/2005.00513) | Graph Centrality Scoring | 
| **FAR** | 2021 | Facet-Aware Evaluation for Extractive Summarization `ACL-IJCNLP Findings` [[Paper]](https://aclanthology.org/2021.findings-acl.147/) | Graph Centrality Scoring |
| **IBsumm** | 2021 | Leveraging Information Bottleneck for Scientific Document Summarization `EMNLP Findings` [[Paper]](https://arxiv.org/abs/2110.01280) | Pipeline Approach |
| **OTExtSum** | 2022 | OTExtSum: Extractive Text Summarisation with Optimal Transport `NAACL Findings` [[Paper]](https://arxiv.org/abs/2204.10086) | Optimal Transport Extraction |

<a name="metrics" />

## Metrics

Metrics listed below are not specific to long document summarization (most summarization metrics are studied under a short/normal summarization setting).

<a name="rel" />

### Relevance
|  **Metric**  | **Year** | **Title**                                       |                          **tl;dr**                           |
| :--------: |:---- | :----------------------------------------------------------- | :----------------------------------------------------------: |
|  **ROUGE**  | 2004 | ROUGE: A Package for Automatic Evaluation of Summaries `ACL` [[Paper]](https://aclanthology.org/W04-1013/) | Hard Lexical Matching |
|  **BERTScore**  | 2019 | BERTScore: Evaluating Text Generation with BERT `ICLR` [[Paper]](https://arxiv.org/abs/1904.09675?context=cs) | Soft Lexical Matching | 
| **BARTScore** | 2021 | BARTScore: Evaluating Generated Text as Text Generation `NeurIPS` [[Paper]](https://arxiv.org/abs/2106.11520) | Conditional Text Generation |

<a name="fact" />

### Factual Consistency 
|  **Metric**  | **Year** | **Title**                                       |                          **tl;dr**                           |
| :--------: |:---- | :----------------------------------------------------------- | :----------------------------------------------------------: |
| **OpenIE** | 2019 | Assessing The Factual Accuracy of Generated Text `KDD` [[Paper]](https://arxiv.org/abs/1905.13322) | Semantic Matching |
|  **FactCC**  | 2019 | Evaluating the Factual Consistency of Abstractive Text Summarization `EMNLP` [[Paper]](https://arxiv.org/abs/1910.12840) | Data Augmentation + Textual Entailment |
| **DAE** | 2020 | Evaluating Factuality in Generation with Dependency-level Entailment `EMNLP Findings` [[Paper]](https://arxiv.org/abs/2010.05478) | Textual Entailment | 
| **FEQA** | 2020 | FEQA: A Question Answering Evaluation Framework for Faithfulness Assessment in Abstractive Summarization `ACL` [[Paper]](https://arxiv.org/abs/2005.03754) | Question-Answering | 
|  **QAGS**  | 2020 | Asking and Answering Questions to Evaluate the Factual Consistency of Summaries `ACL` [[Paper]](https://arxiv.org/abs/2004.04228) | Question-Answering | 
| **TE-MNLI** | 2020 | On Faithfulness and Factuality in Abstractive Summarization `ACL` [[Paper]](https://arxiv.org/abs/2005.00661) | Textual Entailment | 
| **BARTScore** | 2021 | BARTScore: Evaluating Generated Text as Text Generation `NeurIPS` [[Paper]](https://arxiv.org/abs/2106.11520) | Conditional Text Generation |
|  **CoCo** | 2021 | Factual Consistency Evaluation for Text Summarization via Counterfactual Estimation `EMNLP Findings` [[Paper]](https://arxiv.org/abs/2108.13134) | Causal Inference |
| **Q^2** | 2021 | Q2: Evaluating Factual Consistency in Knowledge-Grounded Dialogues via Question Generation and Question Answering `EMNLP` [[Paper]](https://aclanthology.org/2021.emnlp-main.619/) | Question-Answering | 
| **QUAL** | 2021 | Improving Factual Consistency of Abstractive Summarization via Question Answering `ACL-IJCNLP` [[Paper]](https://arxiv.org/abs/2105.04623) | Question-Answering |
| **SummaC** | 2021 | SummaC: Re-Visiting NLI-based Models for Inconsistency Detection in Summarization `TACL` [[Paper]](https://arxiv.org/abs/2111.09525) | Textual Entailment | 
| **FactGraph** | 2022 | FactGraph: Evaluating Factuality in Summarization with Semantic Graph Representations `NAACL` [[Paper]](https://arxiv.org/pdf/2204.06508.pdf) | Knowledge Graph | 
| **FalseSum** | 2022 | Falsesum: Generating Document-level NLI Examples for Recognizing Factual Inconsistency in Summarization `NAACL` [[Paper]](https://arxiv.org/abs/2205.06009) | Data Augmentation + Textual Entailment | 
| **QAFactEval** | 2022 | QAFactEval: Improved QA-Based Factual Consistency Evaluation for Summarization `NAACL` [[Paper]](https://arxiv.org/pdf/2112.08542.pdf) | Question-Answering | 
| **MFMA** | 2022 | Masked Summarization to Generate Factually Inconsistent Summaries for Improved Factual Consistency Checking `NAACL Findings` [[Paper]](https://arxiv.org/abs/2205.02035) | Data Augmentation + Textual Entailment |


<a name="insights" />

## Insightful Discussion

Papers that provide insightful discussions related to long document summarization. 

### Summarization
|  **Topic**  | **Year** | **Title**                                       |                          **tl;dr**                           |
| :--------: |:---- | :----------------------------------------------------------- | :----------------------------------------------------------: |
|  **Metrics**  | 2020 | Re-evaluating Evaluation in Text Summarization `EMNLP` [[Paper]](https://arxiv.org/pdf/2010.07100.pdf) | On Effectiveness of Summarization Models and Metrics |
| **Models** | 2022 | DYLE: Dynamic Latent Extraction for Abstractive Long-Input Summarization `ACL` [[Paper]](https://arxiv.org/abs/2110.08168) | Insighful Approach+Discussion into Extract-then-Summarize Models | 
| **Models** | 2022 | Faithful or Extractive? On Mitigating the Faithfulness-Abstractiveness Trade-off in Abstractive Summarization `ACL` [[Paper]](https://arxiv.org/abs/2108.13684) | Findings of abstractiveness v.s. factuality of abstractive models | 
| **Models** | 2022 | Hallucinated but Factual! Inspecting the Factuality of Hallucinations in Abstractive Summarization `ACL` [[Paper]](https://arxiv.org/abs/2109.09784) | Hallucinated texts (i.e., facts not in doc) often factual | 
| **Models** | 2022 | Training Dynamics for Text Summarization Models `ACL` [[Paper]](https://arxiv.org/abs/2110.08370) | Fine-tuning affects generation strategies |
| **Models** | 2022 | Training Data is More Valuable than You Think: A Simple and Effective Method by Retrieving from Training Data `ACL` [[Paper]](https://arxiv.org/abs/2203.08773) | REtrieving from the traINing datA (REINA) leads to Performance Gain | 
| **Models** | 2022 | Characterizing the Efficiency vs. Accuracy Trade-off for Long-Context NLP Models `ACL` [[Paper]]() | Model Efficiency (Training Cost; Train/Inference Speed) vs. Performance | 
| **Models** | 2022 | FactPEGASUS: Factuality-Aware Pre-training and Fine-tuning for Abstractive Summarization `NAACL` [[Paper]](https://arxiv.org/abs/2205.07830) | Factuality-Aware PEGASUS Pre-training | 
| **Dataset** | 2022 | SQuALITY: Building a Long-Document Summarization Dataset the Hard Way [[Paper]](https://arxiv.org/pdf/2205.11465.pdf) | On Summarization Dataset Creation | 

### General 
|  **Topic**  | **Year** | **Title**                                       |                          **tl;dr**                           |
| :--------: |:---- | :----------------------------------------------------------- | :----------------------------------------------------------: |
|  **Efficient Attention**  | 2020 | Efficient Transformer: A Survey `ACM Comput. Surv.` [[Paper]](https://arxiv.org/pdf/2009.06732.pdf) | Practicality of Efficient Attention (section 4.4) |
| **Fine-tuning** | 2022 | A Closer Look at How Fine-tuning Changes BERT `ACL` [[Paper]](https://aclanthology.org/2022.acl-long.75/) | How Representation Changes after Fine-tuning | 
|  **Text Generation**  | 2022 | Language modeling via stochastic processes `ICLR` [[Paper]](https://arxiv.org/abs/2203.11370) | Text Generation via Latent Stochastic Process | 
| **Efficient Attention** | 2022 | Simple Local Attentions Remain Competitive for Long-Context Tasks `NAACL` [[Paper]](https://arxiv.org/abs/2112.07210) | Local Window Attention remains Competitive |
| **Scaling Language Model** | 2022 | Improving language models by retrieving from trillions of tokens `ICML` [[Paper]](https://arxiv.org/abs/2112.04426) | Retrieve from Two Trillion Tokens Database, then Generate (See REINA above) | 

<a name="survey" />

## An Empirical Survey on Long Document Summarization
Our survey work has been accepted by ACM Computing Surveys. For more information, please visit [An Empirical Survey on Long Document Summarization: Datasets, Models and Metrics](https://dl.acm.org/doi/10.1145/3545176). 

Folders for metrics used to analyze intrinsic characteristics of dataset, metrics used to analyze model outputs and arXiv human annotated data are available. Will be uploaded soon. Please do not hesitate to contact me.

```
@article{10.1145/3545176,
author = {Koh, Huan Yee and Ju, Jiaxin and Liu, Ming and Pan, Shirui},
title = {An Empirical Survey on Long Document Summarization: Datasets, Models and Metrics},
year = {2022},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
issn = {0360-0300},
url = {https://doi.org/10.1145/3545176},
doi = {10.1145/3545176},
note = {Just Accepted},
journal = {ACM Comput. Surv.},
month = {jun},
keywords = {datasets, neural networks, document summarization, language models, Transformer}
}
```

