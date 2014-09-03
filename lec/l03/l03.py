
# coding: utf-8

# # CS579: Lecture 03  
# **Representing Graphs**
# 
# *[Dr. Aron Culotta](http://cs.iit.edu/~culotta)*  
# *[Illinois Institute of Technology](http://iit.edu)*
# 
# (Slides inspired in part by [Jure Leskovec](http://web.stanford.edu/class/cs224w/slides/02-gnp.pdf) and [Easley & Kleinberg](https://github.com/iit-cs579/main/blob/master/read/ek-02.pdf))

# #Terminology
# 
# - **Graph:** A way to represent objects and their relations
#   - **Node:** represents an object
#   - **Edge:** represents a relation between two nodes. 
#   - **Neighbor:** Two nodes are *neighbors* if they are connected by an edge.
# - **Directed Graph:** Represents asymmetric (one-way) relationships
# - **Undirected Graph:** Represents symmetric relationships
# 
# ![graph.pdf](graph.pdf)
# 
# [Source](https://github.com/iit-cs579/main/blob/master/read/ek-02.pdf)
# 
# Examples of **directed** and **undirected** graphs?

# **Path:** A sequence of nodes in which each consecutive pair are neighbors
# - E.g., $A,B,C$ in Figure 2.1(a)
# 
# **Cycle:** A path of at least 3 edges, with first and last nodes the same.
# - E.g., $B,C,D$ in Figure 2.1(a)

# **Connected:** A graph is *connected* if there exists a path between each pair of nodes.
#   - Example of a graph that is *not* connected?

# **Connected Component:** A maximal subset of nodes such that each pair of nodes is connected 
# 
# ![components](components.png)
# [Source](https://github.com/iit-cs579/main/blob/master/read/ek-02.pdf)

# - Is the global friendship network connected?

# # Giant Connected Components
# 
# ![giant](giant.png)

# **Node Degree:** Number of neighbors of a node.
#   - For directed graphs, distinguish between **in-degree** and **out-degree**
#   
# ![graph.pdf](graph.pdf)
# 
# [Source](https://github.com/iit-cs579/main/blob/master/read/ek-02.pdf)
# 

# # Number of edges
# 
# If there are $N$ nodes, what is the maximum number of edges?

# # Number of edges
# 
# If there are $N$ nodes, what is the maximum number of edges?
# 
# $\frac{N(N-1)}{2}$

# In[14]:

import matplotlib.pyplot as plt

sizes = range(10000)
plt.plot(sizes, [s*(s-1)/2.0 for s in sizes])


# Luckily, most real-world graphs are extremely sparse.
# 
# - E.g., you are probably not friends with over 1,000 people.

# # Measuring Graphs
# 
# - How can we summarize a graph?
#   - Besides number of edges and number of nodes.

# # Degree distribution
# 
# - Probability that a randomly chosen node has degree $k$
# - $N_k$: number of nodes with degree $k$
# - $P(k) = \frac{N_k}{N}$
# 

# In[15]:

# See Karate Club network: http://vlado.fmf.uni-lj.si/pub/networks/data/Ucinet/UciData.htm#zachary
# First, we print the degree for each of the 34 nodes.
import networkx as nx
G=nx.karate_club_graph()
print "Node\tDegree"
for v in G:
    print('%s\t%s' % (v, G.degree(v)))


# In[16]:

# Now, let's plot the bar graph for the distribution of P(k)
from collections import Counter
degree_counts = Counter()
for v in G:
    degree_counts.update([G.degree(v)])
p_k = [(degree, 1. * count / len(G.nodes())) for degree, count in degree_counts.iteritems()]
p_k = sorted(p_k)  # To sort in descending order of P(k): key=lambda x: x[1], reverse=True)
print p_k
ks = [x[0] for x in p_k]  # Get the first element of each tuple (the degree)
# Plot the bar chart.
plt.bar(y_pos, [x[1] for x in p_k], align='center', alpha=0.4)
# Label the x ticks.
x_pos = range(len(ks))
plt.xticks(x_pos, ks)
# Label axes and title.
plt.xlabel('$k$')
plt.ylabel('$P(k)$')
mean = 1. * sum([G.degree(v) for v in G]) / len(G.nodes())
plt.title("Degree Distribution for Karate Network (mean=%.2f)" % mean)


# A [Long Tail](http://en.wikipedia.org/wiki/Long_tail)
# - We'll see a lot of these.
# - The mean value of a long-tailed distribution is often misleading.

# **Diameter:** The maximum shortest-path between any pair of nodes.
# 
# **Average path length:** The average shortest-path between any pair of nodes (in one component).

# **Clustering coefficient:** The fraction of a node's neighbors that are neighbors.
# 
# $$C_i = \frac{2e_i}{k_i(k_i - 1)}$$
# 
# - $e_i$: number of edges between neighbors of node $i$
# - $k_i$: degree of node $i$
# 
# **Average Clustering Coefficient:**
# 
# $$C = \frac{1}{N}\sum_i C_i  $$
# 
# ![cluster](cluster.png)
# 
# $$C_i = \frac{2e_i}{k_i(k_i - 1)}$$
# 
# [Source](http://web.stanford.edu/class/cs224w/slides/02-gnp.pdf)
# 

# $k_B=2, e_B=1, C_B=2/2 = 1$
# 
# $k_D=4, e_D=2, C_D=4/12 = 1/3$
