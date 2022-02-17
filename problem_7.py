# A RouteTrie will store our routes and their associated handlers
class RouteTrieNode:
    def __init__(self, handler=None):
        self.next = {}
        self.handler = handler
        # Initialize the node with children as before, plus a handler

    def insert(self, items):
        if not self.next.get(items):
            self.next[items] = RouteTrieNode()
        # Insert the node as before

class RouteTrie:
    def __init__(self,handler=None):
        self.root = RouteTrieNode(handler)
        self.handler = handler
        # Initialize the trie with an root node and a handler, this is the root items or home page node

    def insert(self,items,handler):
        node = self.root
        for i in items:
            node.insert(i)
            node = node.next[i]
        node.handler = handler
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this items

    def find(self, items):
        node = self.root
        for i in items:
            if not node.next.get(i):
                return None
            node = node.next[i]
        return node.handler
                
        # Starting at the root, navigate the Trie to find a match for this items
        # Return the handler for a match, or None for no match
class Router:
    def __init__(self, handler,n_handler):
        self.RouteTrie = RouteTrie(handler)
        self.n_handler = n_handler
    def insert(self, path, handler):
        items = self.split_path(path)
        self.RouteTrie.insert(items, handler)
    def lookup(self, path):
        items = self.split_path(path)
        handler = self.RouteTrie.find(items)
        if handler is None:
            return self.n_handler
        else:
            return handler
    def split_path(self,path):
        if path == '/' or path == '':
            return []
        return path.strip('/').split('/')
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.



# create the router and add a route
router = Router("root handler", "not found handler") 
print('\nAdd a route \"/home/about\" with a handler \"about handler\"')
router.insert("/home/about", "about handler")  # add a route
        
# test case 1
print('\nTest case 1: lookup of "/". Answer is root handler.')
print(router.lookup('/'))

# test case 2
print('\nTest case 2: lookup of "/home/". Answer is not found handler.')
print(router.lookup('/home/'))

# test case 3
print('\nTest case 3: lookup of "/home/about". Answer is about handler.')
print(router.lookup('/home/about'))

# test case 4
print('\n\nTest case 4: lookup of "/home/about/". Answer is about handler.')
print(router.lookup('/home/about/'))

# test case 5
print('\nTest case 5: lookup of "/home/about/me". Answer is not found handler.')
print(router.lookup('/home/about/me'))

# test case 6
print('\nTest case 6: lookup of "123456". Answer is not found handler.')
print(router.lookup('123456'))

# test case 7
print('\nTest case 7: lookup of "". Answer is root handler.')
print(router.lookup(''))

# test case 8
print('\nTest case 8: lookup of "/////". Answer is not found handler.')
print(router.lookup('/////'))
