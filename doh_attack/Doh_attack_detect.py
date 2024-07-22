# Model structure

import math
import torch
import torch.nn as nn

import torch.optim



class TransformerClassifier(nn.Module):

    def __init__(self, ninp, nhead, nhid, nlayers, dropout=0.5):
        super(TransformerClassifier, self).__init__()
        from torch.nn import TransformerEncoder, TransformerEncoderLayer
        self.model_type = 'Transformer'
        encoder_layers = TransformerEncoderLayer(ninp, nhead, nhid, dropout)
        self.transformer_encoder = TransformerEncoder(encoder_layers, nlayers)
        self.ninp = ninp
        self.dropout = nn.Dropout(0.3)
        self.convs = nn.ModuleList([nn.Conv2d(1, 100, (K, ninp)) for K in [3, 4, 5]])
        self.classifier = nn.Linear(ninp, 2)
        self.fc1 = nn.Linear(len([3, 4, 5]) * 100, 2)
        self.init_weights()

    def generate_square_subsequent_mask(self, sz):
        mask = (torch.triu(torch.ones(sz, sz)) == 1).transpose(0, 1)
        mask = mask.float().masked_fill(mask == 0, float('-inf')).masked_fill(mask == 1, float(0.0))
        return mask

    def init_weights(self):
        initrange = 0.1
        self.classifier.bias.data.zero_()
        self.classifier.weight.data.uniform_(-initrange, initrange)

    def forward2(self, src):
        # Transformer Layer
        src = src * math.sqrt(self.ninp)
        x = self.transformer_encoder(src)
        # Conv Layer
        x = x.unsqueeze(1)  # (N, Ci, W, D)
        x = [torch.relu(conv(x)).squeeze(3) for conv in self.convs]  # [(N, Co, W), ...] * len(Ks)
        # Pooling Layer
        x = [torch.max_pool1d(i, i.size(2)).squeeze(2) for i in x]  # [(N, Co), ...] * len(Ks)
        x = torch.cat(x, 1)
        # Fully Connected Layer
        x = self.dropout(x)  # (N, len(Ks)*Co)
        logit = self.fc1(x)  # (N, C)
        return logit

    def forward(self, src):

        # Non-conv Approch
        src = src * math.sqrt(self.ninp)
        output = self.transformer_encoder(src)

        # Average Pooling Layer
        output = output.permute(0, 2, 1)
        output = torch.mean(output, -1)
        output = self.dropout(output)
        # output = torch.relu(self.dense(output))
        output = torch.relu(output)
        output = self.dropout(output)
        output = self.classifier(output)
        return output

    def predict(self, x):

        # Apply sigmoid to output.
        pred = torch.sigmoid(self.forward2(x))
        ans = []

        # Pick the class with maximum weight
        for t in pred:
            if t[0] > t[1]:
                ans.append(t[0])
            else:
                ans.append(t[0])
        return torch.tensor(ans)

model = TransformerClassifier(30, 5, 1024, 3)
#Define loss criterion
criterion = nn.CrossEntropyLoss()
#Define the optimizer
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)


# from your_model_definition_file import TransformerClassifier

# 假设您的模型和数据结构已定义并且df是DataFrame

# 1. 创建模型实例
model = TransformerClassifier(30, 5, 1024, 3)

# 2. 加载模型状态字典
state_dict = torch.load('model_5_20.pth')

# 3. 应用状态字典到模型
model.load_state_dict(state_dict)