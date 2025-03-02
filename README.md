# ParC-ReSMNet
Here is the paper we publish "A novel convolutional neural network with global perception for bearing fault diagnosis".
Please refer to the paper for more information. This repo is based on PyTorch.

## Introduction
Aiming at the limitations of convolutional neural networks in global feature extraction and the low accuracy caused by this deficiency in bearing fault diagnosis based on acoustic signals, this paper proposes a novel ConvNet with global perception capabilities called ParC-ReSMNet.

## Network Architecture
<img src="assets/ParC-ResMNet.png">

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
author = {Xianguo Li and Ying Chen and Yi Liu},
keywords = {Bearing fault diagnosis, Global perception, Spatial pyramid mask attention, Position-aware circular},
abstract = {Bearings are key support components in rotating machinery, and their stability is crucial to the reliability of the entire mechanical system. To address the limitations of existing Transformer architectures in edge-side optimization and convolutional neural networks in global feature extraction, especially the resulting poor real-time performance and low accuracy in bearing fault diagnosis based on acoustic signals, this paper proposes a novel global-aware convolutional neural network based on residual masking and position-aware strategies (ParC-ReSMNet). Firstly, the network is based on the residual network (ResNet-18) and designed with a residual mask block combined with an improved spatial pyramid mask attention mechanism, which effectively removes redundant spatial information and focuses on critical fault features, thereby enhancing the robustness and generalization of the network. Secondly, a position-aware circular module is introduced to replace specific residual blocks in the original network, achieving an effective fusion of positional and global information, thereby augmenting the modeling capability of the convolutional neural network. Experiments are conducted on a self-made belt conveyor idler dataset and the Detection and Classification of Acoustic Scenes and Events (DCASE) 2023 Task2 bearing dataset, with results showing that ParC-ReSMNet achieves 95.49% and 96.67% accuracy, respectively. Compared to seven state-of-the-art models, it has the highest precision and recall, along with good real-time performance, which demonstrates great application value for fault monitoring of belt conveyors used in coal mines, power plants, ports, and other rotating machinery. The code library is available at: https://github.com/xgli411/Parc-ResMNet.}
}
