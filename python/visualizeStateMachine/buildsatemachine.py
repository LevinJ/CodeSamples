from lxml import etree


class BuildSateMachine:
    def __init__(self):
        root = etree.Element('root')
        self.tree = etree.ElementTree(root)
        self.cur_stack = [root]
        return
    def buildMachineinXML(self, direction, node, machine=None):
        if (direction == 'exit'):
            ele = self.cur_stack.pop()
            if (ele.tag != node):
                raise Exception("Unexpected state wrapping, expect {}, actual {}".format(ele.tag, node))
            return
        if (direction != 'entry'):
            raise Exception("invalid input, direction =" + direction)
        newElement = etree.Element(node)
        if not (machine is None):
            newElement.text = machine
        self.cur_stack[-1].append(newElement)
        self.cur_stack.append(newElement)
        return
    def saveOutput(self):
        print etree.tostring(self.tree, pretty_print=True) 
        self.tree.write('output.xml')
        return
    def test(self):
        # create XML 
        root = etree.Element('root')
        c1 = etree.Element('child')
        root.append(c1)
        c2 = etree.Element('embdedchild')
        c1.append(c2)
        c2.append(etree.Element('e111mbdedchild'))
        # another child with text
        child = etree.Element('child')
        child.text = 'some text'
        root.append(child)
        
        
        
        # pretty string
        s = etree.tostring(root, pretty_print=True)
        print s
        return
    def run(self):
        self.buildMachineinXML('entry', 'child')
        self.buildMachineinXML('entry', 'embdedchild')
#         self.buildMachineinXML('ok', 'e111mbdedchild')
        self.buildMachineinXML('entry', 'e111mbdedchild', "this is the machine")
        self.buildMachineinXML('exit', 'e111mbdedchild')
        self.buildMachineinXML('exit', 'embdedchild')
        self.buildMachineinXML('entry', 'child', "this is the machine")
        print etree.tostring(self.tree, pretty_print=True)
        
        self.tree.write('output.xml')
#         self.test()
        return


    





if __name__ == "__main__":   
    obj= BuildSateMachine()
    obj.run()