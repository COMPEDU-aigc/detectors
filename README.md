# AIGC Detection in Educational Contexts  
**Resources and Implementation Details**

This repository provides the **resources and implementation details** supporting the following study:

> **Title:** *Reliability and Limitations of AIGC Detectors in Educational Contexts*  
> **Abstract:**  
> Recent advances in generative artificial intelligence have led to widespread adoption of AIGC tools in educational settings, raising concerns about the reliability of existing detection systems. This study presents a systematic evaluation of current AIGC detectors across diverse educational tasks, including short-answer questions, academic essays, and programming assignments. Through controlled analyses of task difficulty, rhetorical function, and structural complexity, we reveal that detector performance degrades substantially when confronted with outputs requiring higher-order reasoning, reflective writing, or complex code structures. Our findings indicate that most detectors rely on shallow statistical and structural cues rather than deep semantic understanding, fundamentally limiting their effectiveness in authentic educational scenarios.
> *This repository corresponds to the experiments reported in Sections 4.1–4.3 of the paper.*

The repository is designed to facilitate **transparency, reproducibility, and extensibility**, enabling other researchers to apply the same experimental pipeline to their own datasets.

---

## 🌟 Overview

The repository contains the complete implementation used in the paper, including:

- The **evaluation pipeline** for benchmarking AIGC detection tools  
- The **construction of AI-generated responses** using ChatGPT under controlled prompting conditions  
- The **invocation and configuration scripts** for 13 AIGC detectors (open-source and commercial, where permitted)  

> ⚠️ **Note on Data Availability**  
> The datasets used in the paper (e.g., StuTask, StuThesis, DataCode) are derived from authentic student coursework and theses and **cannot be publicly released due to institutional and ethical constraints**.  
> This repository therefore focuses on **methodological reproducibility**, allowing researchers to run the same pipeline on their own data.

---

## 🔁 Evaluation Pipeline

The evaluation pipeline implements a **generator–detector–analysis** framework designed to systematically benchmark AIGC detection tools under realistic educational scenarios.  
It ensures **fair comparison, controlled variability, and reproducible analysis** across heterogeneous tasks and detectors.

### Step 1: Task and Input Preparation
Educational tasks are organized into multiple categories reflecting authentic student work, including:
- Short-answer and problem-solving questions
- Academic essay writing with distinct rhetorical sections (e.g., Methodology, Discussion)
- Programming assignments with varying code lengths and structural complexity

All inputs are formatted according to a unified schema to ensure compatibility with different detectors.

---

### Step 2: AI-Generated Response Construction
For each task, AI-generated responses are produced using **ChatGPT** under controlled prompting conditions:
- Prompt templates are standardized to mirror instructional settings
- Generation parameters (e.g., temperature, maximum tokens) are fixed and documented
- Multiple generations are supported to account for stochasticity

This step yields a paired set of **human-written and AI-generated outputs** for downstream evaluation.

---

### Step 3: Detector Invocation
Each detection tool is invoked through a unified interface to ensure comparability:
- Both open-source and commercial detectors are supported
- Detector-specific preprocessing and configuration are handled via standardized wrappers
- Sentence-level and document-level detectors are evaluated according to their native capabilities

All raw detector scores and intermediate outputs are logged for traceability.

---

### Step 4: Performance Evaluation
Detector outputs are evaluated using standard and widely adopted metrics:
- Area Under the ROC Curve (AUC)
- False Positive Rate (FPR)
- False Negative Rate (FNR)

Performance is analyzed not only globally, but also **stratified by task characteristics**, such as:
- Cognitive difficulty
- Rhetorical function (e.g., procedural vs. reflective writing)
- Structural complexity (e.g., short vs. long code)

---

### Step 5: Aggregation and Statistical Analysis
Results are aggregated across multiple runs and samples:
- Metrics are averaged to reduce variance
- Comparative analyses highlight performance trends and failure modes
- Controlled variable analysis is used to isolate the effect of individual factors

---

### Step 6: Interpretability and Mechanistic Analysis
To move beyond black-box evaluation, the pipeline optionally supports **post-hoc interpretability analysis**:
- Integrated Gradients is applied to selected detectors
- Token-level attributions are aggregated into interpretable cue categories
- Analyses reveal whether detectors rely on surface-level structural cues or deeper semantic signals

---

### Output
All outputs are saved in structured formats to facilitate inspection and reuse.

---
