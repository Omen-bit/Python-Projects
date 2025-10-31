from prettytable import PrettyTable
from reflex_chakra import center

table=PrettyTable()

table.field_names=["Pokemon Name","Type"]
table.add_rows(
    [
        ["Pikachu","Electric"],
        ["Bulbasaur","Grass"],
        ["Charmander","Fire"],
    ]
)
print(table)

able=PrettyTable()
able.add_column("Pokemon Name",["Pikachu","balbasaur","charmandar"],"l")
print(able)