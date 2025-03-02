# ParC-ReSMNet
Here is the paper we publish "A novel convolutional neural network with global perception for bearing fault diagnosis".
Please refer to the paper for more information. This repo is based on PyTorch.

## Introduction
Aiming at the limitations of convolutional neural networks in global feature extraction and the low accuracy caused by this deficiency in bearing fault diagnosis based on acoustic signals, this paper proposes a novel ConvNet with global perception capabilities called ParC-ReSMNet.

## Network Architecture
<img src="assets/model.jpg">

## Result
Our proposed method achieves better performance on self-made belt conveyor idler dataset and and DCASE 2023 dataset.

ROC curves result plot on self-made dataset
<img src="assets/ROC curves on self-made dataset.png">

PR result plot on DCASE 2023 dataset
<img src="assets/ROC curves on DCASE 2023 dataset.png">

## Cite this article

🔗🔗Paper link：[https://www.tandfonline.com/doi/abs/10.1080/10589759.2024.2408441](https://www.sciencedirect.com/science/article/abs/pii/S0952197624021456)

Li X, Chen Y, Liu Y. A novel convolutional neural network with global perception for bearing fault diagnosis[J]. Engineering Applications of Artificial Intelligence, 2025, 143: 109986.

@article{LI2025109986,
title = {A novel convolutional neural network with global perception for bearing fault diagnosis},
journal = {Engineering Applications of Artificial Intelligence},
volume = {143},
pages = {109986},
year = {2025},
issn = {0952-1976},
doi = {https://doi.org/10.1016/j.engappai.2024.109986},
url = {https://www.sciencedirect.com/science/article/pii/S0952197624021456},
author = {Xianguo Li and Ying Chen and Yi Liu}
}
