
def CMB(cb, dct):
    if cb == 0 or dct == 0:
        cmb = "Calculo Indisponivel"
    else:    
        cmb = float(cb - (0.314 * dct))
    return cmb

def AdeqCMB(cmb):
    adeqCMB = (cmb*100) / (cmb) 
    return adeqCMB