
ex1-2
    forgot the unique func

ex 4-1
    not sure why did end+1 at is palindrome func, why needed + 1
    not sure why we check the start>=end  at min cuts func
    forget what to iterate on the min cuts


ex 4-2
    issues at the resolve funct params:
        passed also deps at params
        instead should use only self
        and when itereate at self.deps
        should first check if not in self visited
        then self dfs on pkg
        and return self orders reverse [::-1]
        forget the self param in constructor
        forget to iterate on resolve with for pkg in self.deps

    issues at the dfs func
        forget to add in visiting set the pkg
        not sure how this .get method worlks and what is [] empty list in the get method of dict