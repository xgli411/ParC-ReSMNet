import time
import torch
from torchvision import transforms
from torch.utils.data import DataLoader
from my_dataset import MyDataSet
from torchvision import datasets

from my_utils import read_split_trainData,read_split_testData
from thop import profile

import torchvision.models as tm
import warnings
from sklearn.exceptions import UndefinedMetricWarning
from model.ParC_ResMNet import parc_resnet, Bottleneck, BasicBlock

warnings.filterwarnings("ignore", category=UndefinedMetricWarning)


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

model = parc_resnet(BasicBlock, [2, 2, 2, 2], [1, 1, 1, 1]).to(device)
model_loc = './weight/best_model.pth'
model.load_state_dict(torch.load(model_loc))

train_path = "./self_stft_data/train"
test_path = "./self_stft_data/test"

train_images_path, train_images_label = read_split_trainData(train_path)
test_images_path, test_images_label = read_split_testData(test_path)


img_size = 224
batch_size = 32

data_transform = {
    "train": transforms.Compose([transforms.RandomResizedCrop(img_size),
                                 transforms.RandomHorizontalFlip(),
                                 transforms.ToTensor(),
                                 transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])]),
    "test": transforms.Compose([transforms.Resize(int(img_size * 1.143)),
                                transforms.CenterCrop(img_size),
                                transforms.ToTensor(),
                                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])}

trainDataset = datasets.ImageFolder(train_path, data_transform['train'])
testDataset = datasets.ImageFolder(test_path, data_transform['test'])
class_names = trainDataset.classes
n_class = len(class_names)
trainDataset.class_to_idx
idx_to_labels = {y: x for x, y in trainDataset.class_to_idx.items()}

train_dataset = MyDataSet(images_path=train_images_path,
                          images_class=train_images_label,
                          transform=data_transform["train"])
test_dataset = MyDataSet(images_path=test_images_path,
                         images_class=test_images_label,
                         transform=data_transform["test"])

train_loader = DataLoader(train_dataset, shuffle=True, batch_size=batch_size,
                          num_workers=8, pin_memory=True, drop_last=True)
test_loader = DataLoader(test_dataset, shuffle=False, batch_size=batch_size,
                         num_workers=8, pin_memory=True, drop_last=True)

class_correct = torch.zeros(18)
class_total = torch.zeros(18)

preds = []
targets = []

model.eval()

test_time = time.time()

with torch.no_grad():
    epoch_acc = 0.0

    for step, data in enumerate(test_loader):
        images, labels = data
        pred = model(images.to(device))
        pred_labels = pred.argmax(dim=1)
        _, predicted = torch.max(pred, 1)
        accu_num = torch.eq(pred_labels, labels.to(device)).sum()

flops, params = profile(model, inputs=(input_tensor,))
print("Number of parameters:{}Mb".format(num_params / (1024*1024)))
print("FLOPs:{}".format(flops) + "  " + "Parameters:{} Mb".format(params/ (1000**2)))

end_time = time.time()
num_samples = len(test_dataset)
print("cost:{:3f}ms".format(1000 * (end_time - test_time) / num_samples))

avg_acc = epoch_acc / num_samples
input_tensor = torch.randn(32, 3, 224, 224).cuda()
Acc = "{:.5g}%".format(avg_acc * 100)
print("acc:", Acc)
