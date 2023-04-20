import pytholog as pl

new_kb = pl.KnowledgeBase("pytholog_1")

new_kb([
    "likes(shyam, mango)",
    "girl(seema)",
    "red(rose)",
    "likes(bill, cindy)",
    "owns(john, gold)"
    ])
    
new_kb.query(pl.Expr("likes(shyam, What)"))