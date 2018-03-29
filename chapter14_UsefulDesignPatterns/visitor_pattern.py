class VisitableList(list):
    def show(self, visitor):
        visitor.show_list(self)

class StrangeVisitor(object):
    def show_list(self, list_visited):
        print("I'm strange visitor, I only see the first element of the list:")
        print(list_visited[0])

vl = VisitableList([99, 1, 2, 2])
vl.show(StrangeVisitor())


