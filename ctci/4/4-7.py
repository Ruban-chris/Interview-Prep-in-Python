class DirectedGraphNode:
    def __init__(self, obj):
        self.data = obj
        self.incoming = []
        self.outgoing = []
    def setData(self, obj):
        self.data = obj
    def setIncoming(self, directedGraphNode):
        self.incoming.append(directedGraphNode)
    def setOutgoing(self, directedGraphNode):
        self.outgoing.append(directedGraphNode)

# returns the first instance of the node that has the obj as its data property
# otherwise returns None
def findNodeByData(arrayOfNodes, obj):
    for node in arrayOfNodes:
        if node.data is obj:
            return node
    return None

def doDuplicatesExist(array):
    return len(array) != len(set(array))

projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
dependencies = [['f', 'c'],['f', 'b'], ['f', 'a'], ['c', 'a'], ['b', 'a'], ['a', 'e'], ['b', 'e'], ['d', 'g']]

def findBuildOrder(projects, dependencies):
    # guard case
    if len(projects) is 0 or len(dependencies) is 0:
        return projects
    # guard case check that projects doesn't have any duplicates
    if doDuplicatesExist(projects):
        return False

    # create the nodes
    for i, project in enumerate(projects):
        projects[i] = DirectedGraphNode(project)
    
    # make the directed relationships
    for i, dependency in enumerate(dependencies):
        project = findNodeByData(projects, dependency[0])
        dependentProject = findNodeByData(projects, dependency[1])
        
        if dependentProject is not None and project is not None:
            dependentProject.setIncoming(project)
            project.setOutgoing(dependentProject)
        else:
            raise Exception('project not found')
    
    orderedProjects = []
    while len(projects) > 0:
        # there exists at least one project in projects that has an empty incoming array
        # find all the nodes that don't have incoming nodes
        numOfProjectsThatCanBeStarted = 0
        for i, project in enumerate(projects):
            if len(project.incoming) is 0:
                orderedProjects.append(project)
                numOfProjectsThatCanBeStarted += 1
                projects.pop(i)
        if numOfProjectsThatCanBeStarted is 0:
            return
        # remove the orderedProjects from each project's incoming array
        for project in projects:
            for orderedProject in orderedProjects:
                project.incoming[:] = [x for x in project.incoming if x != orderedProject]
    
    if len(projects) > 0:
        return False
    else:
        return orderedProjects

orderedProjects = findBuildOrder(projects, dependencies)
for orderedProject in orderedProjects:
    print(orderedProject.data)