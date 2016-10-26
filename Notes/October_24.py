#October 24, 2016

"""
Methods for tree:
add_root(data)
#add_child(position,data) nope because it's a binary tree
add_left(data)
add_right(data)
attach(position,Tree1,Tree2)
#Tree1 and Tree2 should become empty afterwards
delete(position)
#should delete leaves or things with just one child
replace(position,data)

binary tree with operations from a formula:
put them on a stack and every time there is are closed parentheses, pop until open parenthesis into a tree
Then append them back onto the tree and continue
"""
