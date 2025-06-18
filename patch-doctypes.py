import kdl
import sys

doctypes_path = sys.argv[1]

with open(doctypes_path, mode="r") as f:
    doctypes = kdl.parse(f.read())

with open("./doctypes.kdl", mode="r") as f:
    additional_doctypes = kdl.parse(f.read())

doctypes.nodes = [
    node for node in doctypes.nodes
    if not (node.name == "org" and (
        node.args == ["ecma"] or node.args == ["wintertc"]
    ))
]
doctypes.nodes += additional_doctypes.nodes

with open(doctypes_path, mode="w") as f:
    f.write(doctypes.print())