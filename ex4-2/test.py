
class DependencyResolver:

    def __init__(self,deps):
        self.deps=deps
        self.visited=set()
        self.visiting=set()
        self.order=[]


    # visits every package (running DFS on each unvisited one) 
        # and returns the reversed build-up order as the final result
    def resolve(self):
        for pkg in self.deps:
            if pkg not in self.visited:
                self._dfs(pkg)
        return self.order[::-1]


    # It recursively processes a package by first:  
        # handling all its dependencies, 
        # detecting cycles along the way, 
        # then marking it done 
        # and adding it to the order.
    def _dfs(self, pkg):
        if pkg in self.visiting:
            raise ValueError(f"Cyclic dependency detected involving '{pkg}'")

        if pkg in self.visited:
            return

        self.visiting.add(pkg)

        for dep in self.deps.get(pkg, []):
            self._dfs(dep)

        self.visiting.remove(pkg)   # no longer exploring this - remove an item from the set
        self.visited.add(pkg)       # this is now finished - add an item to the set
        self.order.append(pkg)      # add pkg to the end of the list

# The mental model — the two sets are like a status flag:
# not in either set  → haven't touched it yet
# in visiting        → currently exploring it (mid-recursion)
# in visited         → completely finished

def resolve_dependencies(deps: dict[str, list[str]]) -> list[str]:
    return DependencyResolver(deps).resolve()


print(resolve_dependencies({'app': ['lib1', 'lib2'], 'lib1': ['core'], 'lib2': ['core'], 'core': []}))  # ['app', 'lib2', 'lib1', 'core']
print(resolve_dependencies({'a': ['b'], 'b': ['c'], 'c': []}))                                          # ['a', 'b', 'c']
print(resolve_dependencies({'a': []}))                                                                  # ['a']


# SETUP (when object is created):
#     deps     = the dependency dictionary
#     visited  = empty set   (packages fully done)
#     visiting = empty set   (packages being explored right now — for cycle detection)
#     order    = empty list  (result, built up as packages finish)

# resolve():                          # the driver
#     for each package in deps:
#         if package not already visited:
#             dfs(package)
#     return order reversed

# dfs(package):                       # the recursive worker
#     if package is in visiting:      # reached one we're still exploring
#         raise error (cycle!)        # -> impossible loop
#     if package is already visited:
#         return                      # nothing to do

#     mark package as visiting

#     for each dependency of package:
#         dfs(dependency)             # finish dependencies FIRST (recursion)

#     unmark package from visiting
#     mark package as visited
#     add package to order            # recorded AFTER its dependencies



# deps = {
#     'app':  ['lib1', 'lib2'],   # 'app' depends on lib1 and lib2
#     'lib1': ['core'],           # 'lib1' depends on core
#     'lib2': ['core'],           # 'lib2' depends on core
#     'core': []                  # 'core' depends on nothing
# }
# pkg = 'app'     # then later 'lib1', 'lib2', 'core', ...