
# from graph import Grap
# ALGORITHMS_SHORTEST_PATH = { "dfs"  : Graph().depth_first_search,
# 			   				   "bfs"  : Graph().breadth_first_search }
# ALGORITHMS_GENERATION = {"binary" : }


MESSAGES = {"step1" : "✅ 𝘀𝘁𝗲𝗽 𝟭 : Constructing (1) Grid (2) Graph",
			"step2" : "✅ 𝘀𝘁𝗲𝗽 𝟮 : Find shortest path (undirected, unweighted)",
			"step3" : "✅ 𝘀𝘁𝗲𝗽 𝟯 : Visualize shortest path if existing"}


data_dir = "labyrinth/data/"



#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#
#          UTILITY FUNCTIONS         #
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#

def pprint(message) :


	msg_size = len(message)
	box_size = int((msg_size + 10)/2)
	box      = "*-" * box_size + "*"

	print(box)
	print("|    {}    |".format(message))
	print(box)


def pprint_list(ll) :
	print('\n'.join(' '.join('%2s' % x for x in l) for l in ll))



