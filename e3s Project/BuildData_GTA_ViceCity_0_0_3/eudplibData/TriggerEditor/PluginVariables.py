from eudplib import *


VChatIndex = EUDArray(8)
VKeyPress_SHIFT = EUDArray(8)
VKeyDown_F = EUDArray(8)
VKeyDown_W = EUDArray(8)
VKeyDown_A = EUDArray(8)
VKeyDown_S = EUDArray(8)
VKeyDown_D = EUDArray(8)
VKeyDown_Q = EUDArray(8)
VKeyDown_TAB = EUDArray(8)
VMousePress_R = EUDArray(8)

def Reg():
    print('... TERegVar ...')
    EUDRegisterObjectToNamespace("VKeyPress_SHIFT", VKeyPress_SHIFT)
    EUDRegisterObjectToNamespace("VKeyDown_F", VKeyDown_F)
    EUDRegisterObjectToNamespace("VKeyDown_W", VKeyDown_W)
    EUDRegisterObjectToNamespace("VKeyDown_A", VKeyDown_A)
    EUDRegisterObjectToNamespace("VKeyDown_S", VKeyDown_S)
    EUDRegisterObjectToNamespace("VKeyDown_D", VKeyDown_D)
    EUDRegisterObjectToNamespace("VKeyDown_Q", VKeyDown_Q)
    EUDRegisterObjectToNamespace("VKeyDown_TAB", VKeyDown_TAB)
    EUDRegisterObjectToNamespace("VMousePress_R", VMousePress_R)
    EUDRegisterObjectToNamespace("VChatIndex", VChatIndex)
EUDOnStart(Reg)
