import core




def setup():
        print("Setup START---------")
        core.fps = 60
        core.WINDOW_SIZE = [800, 600]


        core.memory("avatar",Avatar())

        core.memory("listcreep", [])
        core.memory("nbrbrique", 100)
        for c in range(0, core.memory("nbrbrique")):
            core.memory("listbrique").append(brique(800,600))





        print("Setup END-----------")

def run():
    core.cleanScreen()
    for creep in core.memory("listbrique"):
        creep.show(core.screen)
    core.memory("avatar").show(core.screen)




    core.printMemory()



core.main(setup, run)
