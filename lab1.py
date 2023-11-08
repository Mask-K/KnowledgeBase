from pyDatalog import pyDatalog


pyDatalog.create_terms('X, Y, Z, _, mother, parent, female, sister, father, '
                       'male, haschild, sibling, grandparent, grandmother, grandfather, '
                       'wife, uncle, brother, daughter, son')


mother(X, Y) <= parent(X, Y) & female(X)
sister(X,Y) <= parent(Z, X) & parent(Z, Y) & female(X) & (X != Y)
father(X, Y) <= parent(X, Y) & male(X)
haschild(X) <= parent(X, _)
sister(X,Y) <= parent(Z, X) & parent(Z, Y) & male(X) & (X != Y)
sibling(X,Y) <= parent(Z, X) & parent(Z, Y) & (X != Y)
grandparent(X, Y) <= parent(X, Z) & parent(Z, Y)
grandmother(X, Y) <= mother(X, Z) & parent(Z, Y)
grandfather(X,Y) <= father(X, Z) & parent(Z, Y)
wife(X, Y) <= parent(X, Z) & female(X) & parent(Y, Z)
uncle(X, Y) <= brother(X, Z) & parent(Z, Y)
daughter(X, Y) <= female(X) & parent(Y, X)
son(X, Y) <= male(X) & parent(Y, X)


