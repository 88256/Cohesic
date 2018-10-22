
# Cohesic Junior Software Developer Application Exercise
# Created by: Michael N. Briscoe
# Last Updated: October 22, 2018
# Tested using Python 3.6 on Windows 10 (64-bit)


# Imports.
import tkinter.tix as Tix

class View(object):

    # Initialization.
    def __init__(self, root):
        self.root = root
        self.makeCheckList()

    # Checklist creation.
    def makeCheckList(self):
        self.cl = Tix.CheckList(self.root, browsecmd=self.selectItem)
        # The window size was chosen manually for this exercise; in code for actual use, something like this could (should) be automated
        #   depending on the size of the checklist.
        self.cl.configure(width=190,height=220)
        self.cl.pack()
        
        # The following checklist contents were created manually for this exercise. In a world where multiple checklists would need to be
        #   generated for a wide variety of anatomy, I would automate this process to take some sort of input (say a list of all items
        #   and their respective hierarchical tier) and generate these commands accordingly.
        self.cl.hlist.add('item0', text='Chest')
        self.cl.setstatus('item0', 'off')
        
        self.cl.hlist.add('item0.1', text='Lungs')
        self.cl.setstatus('item0.1', 'off')

        self.cl.hlist.add('item0.1.1', text='Right Lung')
        self.cl.setstatus('item0.1.1', 'off')

        self.cl.hlist.add('item0.1.1.1', text='Superior Lobe')
        self.cl.setstatus('item0.1.1.1', 'off')
        self.cl.hlist.add('item0.1.1.2', text='Middle Lobe')
        self.cl.setstatus('item0.1.1.2', 'off')
        self.cl.hlist.add('item0.1.1.3', text='Inferior Lobe')
        self.cl.setstatus('item0.1.1.3', 'off')

        self.cl.hlist.add('item0.1.2', text='Left Lung')
        self.cl.setstatus('item0.1.2', 'off')

        self.cl.hlist.add('item0.1.2.1', text='Superior Lobe')
        self.cl.setstatus('item0.1.2.1', 'off')
        self.cl.hlist.add('item0.1.2.3', text='Inferior Lobe')
        self.cl.setstatus('item0.1.2.3', 'off') 

        self.cl.hlist.add('item0.2', text='Heart')
        self.cl.setstatus('item0.2', 'off')

        self.cl.hlist.add('item0.2.1', text='Left Ventricle')
        self.cl.setstatus('item0.2.1', 'off')  
        self.cl.hlist.add('item0.2.2', text='Right Ventricle')
        self.cl.setstatus('item0.2.2', 'off')    
        self.cl.hlist.add('item0.2.3', text='Left Aorta')
        self.cl.setstatus('item0.2.3', 'off')    
        self.cl.hlist.add('item0.2.4', text='Right Aorta')
        self.cl.setstatus('item0.2.4', 'off')    
        self.cl.hlist.add('item0.2.5', text='Septum')
        self.cl.setstatus('item0.2.5', 'off')                       

        self.cl.autosetmode()

    # Automatic selection as per exercise instructions.
    def autoCheck(self, item):
        # Automatically select parents when an item is selected.
        if self.cl.getstatus(item) == 'on':
            if self.cl.hlist.info_parent(item):
                parent = self.cl.hlist.info_parent(item)
                self.cl.setstatus(parent, 'on')
                self.autoCheck(parent)
        # Automatically deselect children when an item is deselected.
        elif self.cl.getstatus(item) == 'off':
            if self.cl.hlist.info_children(item):
                for child in self.cl.hlist.info_children(item):
                    self.cl.setstatus(child, 'off')
                    self.autoCheck(child)

    # Commands to execute when an item is selected or deselected can go here.
    def selectItem(self, item):
        self.autoCheck(item)

# Main call.
def main():
    root = Tix.Tk()
    View(root)
    root.update()
    root.mainloop()

# Continuous running until widget is closed.
if __name__ == '__main__':
    main()