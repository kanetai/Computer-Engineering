from matplotlib_venn import venn3_unweighted
import matplotlib.pyplot as plt
from functools import reduce
def elements_text(a: list) -> str:
    return reduce(lambda x, y: f"{x}{y}\n", a, "")
def venn2_elements(A: set, B: set, U: set, subset_areas=(1, 1, 1, 0.05, 0.00000001, 0.00000001, 0.00000001)):
    diagram = venn3_unweighted(subsets=(A, B, U), set_labels=("A", "B", "U"), subset_areas=subset_areas)
    diagram.get_label_by_id("100").set_text(elements_text(A - B))
    diagram.get_label_by_id("010").set_text(elements_text(B - A))
    diagram.get_label_by_id("110").set_text(elements_text(A & B))
    diagram.get_label_by_id("001").set_text(elements_text(U - A - B))
    diagram.get_patch_by_id("001").set_color("white")
    diagram.get_label_by_id("101").set_text(None)
    diagram.get_label_by_id("011").set_text(None)
    diagram.get_label_by_id("111").set_text(None)

A = set([4, 10, 12, 18])
B = set([2, 4, 6, 12, 16])
U = set([2, 4, 6, 8, 12, 14, 16, 18])
venn2_elements(A, B, U)

plt.savefig('venn2_elements.svg')
plt.show()
