def estalt(idade,sexo,aj):
    if aj == 0:
        return("Altura não calculada")
    else:    
        if sexo == 'M':
            ae = (64.19 - (0.04 * idade) + (2.02 * aj))
        else:
            ae = (84.88 - (0.24 * idade) + (1.83 * aj))
        ae = ae / 100
    return (ae)