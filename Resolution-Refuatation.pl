loves(santa, reindeer).
loves(X, Y) :- loves(santa, Y), X \= santa.

reindeer(rudolph).
has_red_nose(rudolph).

weird(X) :- has_red_nose(X).
clown(X) :- has_red_nose(X).

not_clown(X) :- \+ clown(X).

scrooge(X) :- X \= child, \+ weird(_), loves(X, rudolph).