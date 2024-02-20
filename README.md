# Quantifying Interest of Self-Admitted Technical Debt in Machine Learning Projects
This is the final project for the SOEN-691: Engineering AI-based Software Systems course.

## Abstract
Technical debt (TD) in software development represents the long-term costs incurred from short-term solutions and workarounds. Self-Admitted Technical Debt (SATD) refers to situations where developers acknowledge the creation of TD through source code comments. This research focuses on identifying and quantifying the types of TD in Machine Learning (ML) applications that present greater resolution challenges. We utilize software engineering metrics to evaluate the effort required to resolve SATDs in ML projects, shedding light on prioritization needs in ML development.

## Introduction
The concept of "technical debt" (TD) highlights the trade-offs between expedited completion and software quality. As ML models become integral to various domains, understanding the specific types of ML SATD that require more effort to resolve is crucial for effective ML development.

## Methodology
Our study analyzes a dataset of SATD instances in ML projects, focusing on resolved SATDs to calculate the effort required for their removal. We employ metrics such as commit size, cyclomatic complexity, and fan-in to quantify this effort. Additionally, we use Principal Component Analysis (PCA) and weighted averages to rank the ML SATD types and pipeline stages based on their resolution effort.

## Results
Our findings indicate that Modularity and Data Acquisition are the ML SATD types and pipeline stages, respectively, that demand more effort to resolve. Poor modularity often leads to challenges like circular dependencies, while TDs in the Data Acquisition stage, though quickly addressed, typically involve fewer modifications in terms of lines of code (LOC).

## Discussion and Implications
The results suggest that ML developers should prioritize addressing technical debt related to Modularity and Data Acquisition to enhance the efficiency of ML development. Researchers are encouraged to explore the impact of SATD on ML model metrics and develop guidelines for managing SATD in ML projects.

## Related Work
- OBrien et al. (2022) developed a taxonomy of ML SATDs and analyzed their characteristics and removal efforts.
- Kamei et al. (2016) proposed a method using software product metrics to quantify the interest on SATD.
- Zampetti et al. (2018) conducted an in-depth study on the removal of SATD in Java open-source projects.

## Conclusion
This study highlights the importance of addressing technical debt related to Modularity and Data Acquisition in ML projects. By quantifying the effort required to resolve SATDs, we provide actionable insights for ML developers and researchers to prioritize and manage technical debt effectively.

## Authors
- Mayra Ruiz (m_ruizro@live.concordia.ca) - Concordia University
- Rachna Raj (r_rachna@live.concordia.ca) - Concordia University
- Mohammedhossein Malekpour (mohammadhossein.malekpour@polymtl.ca) - Polytechnique Montreal
- Ajibode Adekunle (ajibode.a@queensu.ca) - Queens University
