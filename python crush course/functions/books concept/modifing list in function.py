#start with some designs that need to be printed.
unprinted_design = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
#  Move each design to completed_models after printing.
while unprinted_design:
    current_design = unprinted_design.pop()
    print(f"Printing model : {current_design}")
    completed_models.append(current_design)
print(f"\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_models)
