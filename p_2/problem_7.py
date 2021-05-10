class RouteTrie:
    def __init__(self, root):
        self.root = RouteTrieNode(root)

    def insert(self, path_arr, handler):
        root = self.root

        for path in path_arr:
            root.insert(path)
            root = root.children[path]

        root.handler = handler

    def find(self, path_arr):
        node = self.root

        for path in path_arr:
            if path in node.children:
                node = node.children[path]

            else:
                return None

        return node.handler


class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = {}
        self.handler = handler

    def insert(self, path):
        if path not in self.children:
            self.children[path] = RouteTrieNode()


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path_str, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_str = self.split_path(path_str)

        self.route_trie.insert(path_str, handler)

    def lookup(self, path_str=None):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if not path_str:
            return "invalid path"

        splitted_path = self.split_path(path_str)

        if len(splitted_path) == 0:
            return self.route_trie.root.handler

        result = self.route_trie.find(splitted_path)

        if result != None:
            return result

        return self.not_found_handler

    def split_path(self, path_str):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path_str:
            splitted_path = path_str.split(sep="/")

            return [element for element in splitted_path if element != ""]
        else:
            return []


# create the router and add a route
router = Router(
    "root handler", "not found handler"
)  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(
    router.lookup("/home")
)  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(
    router.lookup("/home/about/")
)  # should print 'about handler' or None if you did not handle trailing slashes
print(
    router.lookup("/home/about/me")
)  # should print 'not found handler' or None if you did not implement one
print(router.lookup())  # should print 'invalid path'
