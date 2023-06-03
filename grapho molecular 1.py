import dgl
import torch
import torch.nn as nn

# Definir el grafo molecular como un objeto DGLGraph
g = dgl.graph(([0, 1, 2], [1, 2, 3]))  # Definir aristas

# Definir características de nodos y aristas
g.ndata['h'] = torch.tensor([[0.0], [1.0], [2.0], [3.0]])
g.edata['w'] = torch.tensor([[0.1], [0.2], [0.3]])

# Definir una capa de convolución de grafo
class GraphConv(nn.Module):
    def __init__(self, in_feats, out_feats):
        super(GraphConv, self).__init__()
        self.linear = nn.Linear(in_feats, out_feats)

    def forward(self, g, feature):
        with g.local_scope():
            g.ndata['h'] = feature
            g.update_all(dgl.function.u_mul_e('h', 'w', 'm'),
                         dgl.function.sum('m', 'h'))
            h = self.linear(g.ndata['h'])
            return h

# Crear una instancia de la capa de convolución de grafo
conv = GraphConv(1, 2)

# Aplicar la convolución de grafo al grafo y las características de los nodos
h = conv(g, g.ndata['h'])
print(h)