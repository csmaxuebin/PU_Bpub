# # This code is the source code implementation for the paper "PU_Bpub: High-Dimensional Data Release Mechanism based on Spectral Clustering with Local Differential Privacy"


## Abstract

Although the release and analysis of high-dimensional data bring tremendous value to people, it causes great hidden danger to participants’ privacy in the meantime. Various privacy protection methods based on differential privacy have been proposed at present. However, most of them cannot simultaneously solve the problems of high computational overhead and privacy threats from untrusted servers caused by the curse of high dimensionality. Therefore, we propose a safer and more effective high-dimensional data release algorithm based on local differential privacy,  which is referred to as PU Bpub. It effectively preserves the dimensional correlation of the original high-dimensional data and reduces the communication overhead of synthetic data. Extensive experiments on real-world datasets demonstrate that our solution substantially outperforms the state-of-the-art techniques in terms of computational overhead, and the synthetic dataset has high utility.
论文链接：[PU_Bpub: High-Dimensional Data Release Mechanism Based on Spectral Clustering with Local Differential Privacy | SpringerLink](https://link.springer.com/chapter/10.1007/978-3-031-19214-2_48)
  

# Experimental Environment

- Python 2.7 (Anaconda Python recommended)

- itertools

- csv

- time

- pandas

- graph

- random

- JunctionTree

- collections

- Evaluation_SVM

- scikit-learn

- hashlib

- json

## Datasets

‘Adult，Retail，TPC-E’

## Experimental Setup

**Hyperparameters:**
 All algorithms and experiments were implemented using Python 2.7, running on a Windows 10 PC with Intel Coreli5-8250 CPU 1.8GHz and 8 GB RAM.


 
**Evaluation Metrics:**

 **Average Variation Distance (AVD)**: Used to quantify the difference between the joint probability distributions of the synthetic datasets and the original datasets. It measures how well the privacy mechanism preserves the statistical characteristics of the original data.
**Calinski-Harabasz Index**: Although not explicitly mentioned as a privacy metric, this index helps in determining the optimal number of clusters, which indirectly contributes to preserving data privacy by optimizing the data partitioning process.
**SVM and RF Classifications**: The average accuracy of SVM and Random Forest (RF) classification models is used to evaluate the data utility of the synthetic datasets. The decrease in classification accuracy with increased privacy parameter (f) reflects the impact of privacy protection on data utility.
**Running Time**: The time complexity of the proposed scheme is compared to previous algorithms, demonstrating the efficiency of the new approach, especially when processing high-dimensional data.
  
## Python Files
**Tut_BNET_maxsum.py**:

-   This script likely contains code to implement or demonstrate the max-sum algorithm on a Bayesian Network. The max-sum algorithm is a message-passing algorithm used in probabilistic graphical models for inference tasks, suggesting this script might be used for educational or demonstration purposes related to Bayesian inference.

**Tut_BNET_sumproduct.py**:

-   Similar to the max-sum script, this file is expected to demonstrate the sum-product algorithm, another fundamental algorithm used for inference in Bayesian Networks. The sum-product algorithm calculates marginal distributions of nodes in the network, which could be part of a tutorial or a utility function in a larger project focusing on Bayesian Networks.

**Tut_BNET_EM.py**:

-   This script likely contains an implementation of the Expectation-Maximization (EM) algorithm for a Bayesian Network setting. The EM algorithm is used for finding maximum likelihood estimates of parameters in probabilistic models, particularly when the data are incomplete or have missing values. This script might be used in educational contexts to explain how EM works in the context of Bayesian Networks.

**batch_mrf_image_denoising.py**:

-   The naming suggests this script is used for batch processing of image denoising tasks using Markov Random Fields (MRFs). Image denoising is a common application of MRFs where the goal is to remove noise while preserving important image details. This script likely processes multiple images or iteratively applies the MRF-based denoising process across a set of images.
...
## Experimental Results
These graphs and tables summarize the effectiveness of different federated learning strategies under various attack vectors, focusing on how different privacy-preserving methods hold up against advanced adversarial techniques. Each plot and metric offers insight into the trade-offs between model accuracy, loss, and privacy protection.

![输入图片说明](https://github.com/csmaxuebin/PU_Bpub/blob/main/images/fig1.png)
![输入图片说明](https://github.com/csmaxuebin/PU_Bpub/blob/main/images/fig2.png?raw=true).
![输入图片说明](https://github.com/csmaxuebin/PU_Bpub/blob/main/images/fig3.png?raw=true).
![输入图片说明](https://github.com/csmaxuebin/PU_Bpub/blob/main/images/fig4.png?raw=true).

![输入图片说明](https://github.com/csmaxuebin/PU_Bpub/blob/main/images/fig5.png?raw=true).


##  Update log  

- {24.06.17} Uploaded overall framework code and readme file


