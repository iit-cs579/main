
# coding: utf-8

# # CS579: Assignment 1
# ## Collecting a political social network
# 
# In this assignment, I've given you a list of Twitter accounts of 10 U.S. Senators. 
# The goal is to use the Twitter API to construct the follower network of these accounts. We will then use the [networkx](http://networkx.github.io/) library to plot these links, as well as print some statistics of the resulting graph.
# 
# 1. Follow the instructions in [Readme.md](Readme.md) to configure your system.
# 2. Copy the files from this directory into the `asg/a1` folder of your private repository.
# 2. Create an account on [twitter.com](http://twitter.com).
# 3. Generate authentication tokens by following the instructions [here](https://dev.twitter.com/docs/auth/tokens-devtwittercom).
# 4. Add your tokens to the `twitter.cfg` file. (API Key == Consumer Key)
# 5. Be sure you've installed the Python modules [networkx](http://networkx.github.io/) and [TwitterAPI](https://github.com/geduldig/TwitterAPI). Assuming you've already installed [pip](http://pip.readthedocs.org/en/latest/installing.html), you can do this with `pip install networkx TwitterAPI`.
# 
# OK, now you're ready to start collecting some data!
# 
# I've provided a partial implementation below. Your job is to complete the code where indicated.
# Your output should match the samples provided below.

# In[1]:

import ConfigParser
import sys
import time

import matplotlib.pyplot as plt
import networkx as nx
from TwitterAPI import TwitterAPI

# This method is done for you.
def get_twitter(config_file):
    """ Read the config_file and construct an instance of TwitterAPI.
    Args:
      config_file ... A config file in ConfigParser format with Twitter credentials
    Returns:
      An instance of TwitterAPI.
    """
    config = ConfigParser.ConfigParser()
    config.read(config_file)
    twitter = TwitterAPI(
                   config.get('twitter', 'consumer_key'),
                   config.get('twitter', 'consumer_secret'),
                   config.get('twitter', 'access_token'),
                   config.get('twitter', 'access_token_secret'))
    return twitter

twitter = get_twitter('twitter.cfg')
print 'Established Twitter connection.'


# In[2]:

def read_senators(filename):
    """ Read a list of usernames for U.S. senators.
    Args:
      filename: The name of the text file containing one senator username per file.
    Returns:
      A list of usernames
    """
    # Complete this method.
    return None

senators = read_senators('senators.txt')
print 'Read', len(senators), 'senators:\n', '\n'.join(senators)


# In[3]:

# Add senators as nodes.
def create_graph(senators):
    """ Create a networkx DiGraph, adding each senator as a node. 
    Args:
      senators: a list of Senator Twitter screen names.
    Returns:
      A networkx DiGraph
    """
    # Complete this method.
    return None

graph = create_graph(senators)
nx.draw(graph)
plt.savefig("senators.png")


# In[7]:

# Now query the Twitter API to add directed edges between all senators X and Y if X follows Y.

# I've provided the method below to handle Twitter's rate limiting.
def robust_request(twitter, resource, params, max_tries=5):
    """ If a Twitter request fails, sleep for 15 minutes.
    Do this at most max_tries times before quitting.
    Args:
      twitter .... A TwitterAPI object.
      resource ... A resource string to request.
      params ..... A parameter dictionary for the request.
      max_tries .. The maximum number of tries to attempt.
    Returns:
      A TwitterResponse object, or None if failed.
    """
    for i in range(max_tries):
        request = twitter.request(resource, params)
        if request.status_code == 200:
            return request
        else:
            print >> sys.stderr, 'Got error:', request.text, '\nsleeping for 15 minutes.'
            sys.stderr.flush()
            time.sleep(60 * 15)
    
    
def get_friends(screen_name, twitter):
    """ Return Twitter screen names for all accounts followed by screen_name. Returns the first 200 users.
    See docs at: https://dev.twitter.com/docs/api/1.1/get/friends/list
    Args:
      screen_name ... The query account.
      twitter ....... The TwitterAPI object.
    Returns:
      A list of Twitter screen names.
    """
    # Complete this method.
    return None

def add_edges(senators, graph, twitter):
    """ Add edges to the graph representing Senator X following Senator Y.
    For each senator, call the get_friends method to get the list of other people s/he follows.
    Then, for each friend that is on the original senator list, add an edge to the graph.
    
    Args:
      senators ... A list of senator screen names.
      graph ...... A networkx graph.
      twitter .... TwitterAPI object.
    """
    # Complete this method.
    return None


add_edges(senators, graph, twitter)
# Draw the new graph and save to file.
# Note that your graph may differ somewhat based on the results of what Twitter returns.
nx.draw(graph)
plt.savefig("senators-edges.png")


# In[9]:

# Now print and plot the degree and betweenness_centrality of each node.
# See the networkx functions `degree` and `betweenness_centrality` at 
# http://networkx.github.io/documentation.html
def get_degrees(graph):
    """
    Args:
      graph ... A networkx graph
    Returns:
      Return a list of (senator, degree) tuples.
    """
    # Complete this method.
    return None

def get_betweenness_centrality(graph):
    """
    Args:
      graph ... A networkx graph
    Returns:
      Return a list of (senator, degree) tuples.
    """
    # Complete this method.
    return None

# No need to modify the code below.
degrees = get_degrees(graph)
betweens = get_betweenness_centrality(graph)
print 'degree'
print '\n'.join([str(d) for d in degrees])
print '\nbetweenness'
print '\n'.join([str(b) for b in betweens])
plt.scatter([d[1] for d in degrees], [b[1] for b in betweens])
plt.xlabel('degree')
plt.ylabel('betweenness')
plt.savefig('degree.png')


# That's it for now! This should give you a simple introduction to some of the key issues we'll cover in this course.
