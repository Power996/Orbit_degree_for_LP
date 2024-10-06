#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx


# In[3]:


M1 = nx.Graph()
M2 = nx.Graph()
M3 = nx.Graph()
M4 = nx.Graph()
M5 = nx.Graph()
M6 = nx.Graph()
M7 = nx.Graph()
M8 = nx.Graph()
M9 = nx.Graph()
M10 = nx.Graph()
M11 = nx.Graph()
M12 = nx.Graph()

M1.add_nodes_from([1, 2, 3])
M1.add_edges_from([(1, 2), (2, 3)])

M2.add_nodes_from([1, 2, 3])
M2.add_edges_from([(1, 2), (2, 3), (3, 1)])

M3.add_nodes_from([1, 2, 3, 4])
M3.add_edges_from([(1, 2), (1, 3), (1, 4)])

M4.add_nodes_from([1, 2, 3, 4])
M4.add_edges_from([(1, 2), (1, 3), (2, 4)])

M5.add_nodes_from([1, 2, 3, 4])
M5.add_edges_from([(1, 2), (1, 3), (3, 4)])

M6.add_nodes_from([1, 2, 3, 4])
M6.add_edges_from([(1, 2), (1, 3), (1, 4), (3, 4)])

M7.add_nodes_from([1, 2, 3, 4])
M7.add_edges_from([(1, 2), (1, 4), (2, 4), (3, 4)])

M8.add_nodes_from([1, 2, 3, 4])
M8.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 4)])

M9.add_nodes_from([1, 2, 3, 4])
M9.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

M10.add_nodes_from([1, 2, 3, 4])
M10.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3), (2, 4)])

M11.add_nodes_from([1, 2, 3, 4])
M11.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 4), (3, 4)])

M12.add_nodes_from([1, 2, 3, 4])
M12.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])

# 点模体度有15种
N1 = nx.Graph()
N2 = nx.Graph()
N3 = nx.Graph()
N4 = nx.Graph()
N5 = nx.Graph()
N6 = nx.Graph()
N7 = nx.Graph()
N8 = nx.Graph()
N9 = nx.Graph()
N10 = nx.Graph()
N11 = nx.Graph()
N12 = nx.Graph()
N13 = nx.Graph()
N14 = nx.Graph()
N15 = nx.Graph()

N1.add_nodes_from([1, 2])
N1.add_edges_from([(1, 2)])

N2.add_nodes_from([1, 2, 3])
N2.add_edges_from([(1, 2), (1, 3)])

N3.add_nodes_from([1, 2, 3])
N3.add_edges_from([(1, 2), (2, 3)])

N4.add_nodes_from([1, 2, 3])
N4.add_edges_from([(1, 2), (1, 3), (2, 3)])

N5.add_nodes_from([1, 2, 3, 4])
N5.add_edges_from([(1, 2), (1, 3), (1, 4)])

N6.add_nodes_from([1, 2, 3, 4])
N6.add_edges_from([(1, 2), (2, 3), (2, 4)])

N7.add_nodes_from([1, 2, 3, 4])
N7.add_edges_from([(1, 2), (2, 3), (3, 4)])

N8.add_nodes_from([1, 2, 3, 4])
N8.add_edges_from([(1, 2), (1, 3), (3, 4)])

N9.add_nodes_from([1, 2, 3, 4])
N9.add_edges_from([(1, 2), (2, 3), (2, 4), (3, 4)])

N10.add_nodes_from([1, 2, 3, 4])
N10.add_edges_from([(1, 2), (1, 3), (1, 4), (3, 4)])

N11.add_nodes_from([1, 2, 3, 4])
N11.add_edges_from([(1, 3), (1, 4), (2, 3), (3, 4)])

N12.add_nodes_from([1, 2, 3, 4])
N12.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 4)])

N13.add_nodes_from([1, 2, 3, 4])
N13.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 4), (1, 3)])

N14.add_nodes_from([1, 2, 3, 4])
N14.add_edges_from([(1, 2), (2, 3), (3, 4), (2, 4), (1, 3)])

N15.add_nodes_from([1, 2, 3, 4])
N15.add_edges_from([(1, 2), (2, 3), (1, 4), (3, 4), (1, 3), (2, 4)])


# In[ ]:




