from Calculos.DCT import DCTCalpercentil
from Calculos.IMC import imcV
from Calculos.CB import Calpercentil
from Calculos.IMC import imc
from PySimpleGUI import PySimpleGUI as sg
# from RCQ import ResRCQ
from Calculos.pesoIdeal import pesoI
from Calculos.PE import calpe
from Calculos.AE import estalt
from Calculos.CMB import CMB
from img.imgBase64 import base64
#===============TELA DA NUTRICIONISTA==============================

        # Janela princial
def janelaPrinc():
        # Temas do layout 
        if __name__ == '__main__':
         enviar = base64.enviar()
        sg.theme_background_color('#98D7C2')
        
        sg.theme_text_element_background_color('#98D7C2')
        sg.theme_button_color('#742e2b')
        sg.theme_text_color('Black')
        sg.theme_element_background_color('#fdefc5')
        
        layout = [
            [
                sg.Column([
                    [sg.Image(filename='img\png\planoFundo.png', background_color='#98D7C2')]
                ]),
                sg.Column([
                    [sg.Image(filename='img\png\TextBox.png', background_color='#98D7C2', pad=(20, 20))],
                    [sg.Column([
                    [sg.Text('Nome do paciente:', size=(0, 0), font=('Roboto', 12, 'bold'))],
                    [sg.Image(filename='img\png\InputL.png',background_color='#98D7C2',pad=((5,0),(0,0))),sg.Input(size=(25,0), key='nome',border_width=0, pad=((0,0),(0,0)),background_color="#FFFFFF"),sg.Image(filename='img\png\InputR.png',background_color='#98D7C2',pad=(0,0))],
                    [sg.Text('Gênero de biológico:', pad=((10,0),(15,0)),font=('Roboto', 12, 'bold'))],
                    [sg.Column([
                     [sg.Radio("", "gender", key='M',background_color='#98D7C2',circle_color='#007AA2', visible=False, pad=((0, 0), (0, 0))),sg.Image(filename='img\png\M_False.png',background_color='#98D7C2',enable_events=True,key='masc' ,pad=((0, 0), (0, 0)))],
                    ]),sg.Column([
                     [sg.Radio("","gender", key='F',background_color='#98D7C2',circle_color='#007AA2',visible=False,pad=((0, 0), (0, 0))),sg.Image(filename='img\png\F_False.png', background_color='#98D7C2',enable_events=True,key='fem' ,pad=((0, 0), (0, 0)))]
                    ])
                    ], 
                    [sg.Text('Cor da pele:', pad=((10,0),(0,0)),font=('Roboto', 12, 'bold'))],
                    [sg.Column([
                     [sg.Radio("","race", key='B',background_color='#98D7C2',visible=False, pad=((0, 0), (0, 0))),
                      sg.Image(filename='img\png\B_False.png',background_color='#98D7C2',enable_events=True,key='branc' ,pad=((0, 0), (0, 0)))],
                
                    ]),sg.Column([
                       [sg.Radio("","race", key='N',background_color='#98D7C2',visible=False,pad=((0, 0), (0, 0))),sg.Image(filename='img\png\P_False.png', background_color='#98D7C2',enable_events=True,key='ne' ,pad=((0, 0), (0, 0)))]
                    ])
                    ],
                    [sg.Text('Idade:', size=(7, 0), font=('Roboto', 12, 'bold')),sg.Text('Altura:', size=(7, 0), font=('Roboto', 12, 'bold')),sg.Text('Peso:', size=(10, 0), font=('Roboto', 12, 'bold'))],
                    [
                     sg.Image(filename='img\png\InputL.png',background_color='#98D7C2',pad=(0,0)),sg.Input(size=(7, 0), key='idade',pad=(0,0),border_width=0,background_color="#FFFFFF"),sg.Image(filename='img\png\InputR.png',background_color='#98D7C2',pad=((0,10),(0,0))),
                     sg.Image(filename='img\png\InputL.png',background_color='#98D7C2',pad=(0,0)),sg.Input(size=(7, 0), key='altura',pad=(0,0),border_width=0,background_color="#FFFFFF"),sg.Image(filename='img\png\InputR.png',background_color='#98D7C2',pad=((0,10),(0,0))),
                     sg.Image(filename='img\png\InputL.png',background_color='#98D7C2',pad=(0,0)),sg.Input(size=(7, 0), key='peso',pad=(0,0),border_width=0,background_color="#FFFFFF"),sg.Image(filename='img\png\InputR.png',background_color='#98D7C2',pad=((0,10),(0,0))),
                     ],
                    [sg.Text('CB (Circunferência do braço):',pad=((0,0),(15,0)), size=(30, 0), font=('Roboto', 12, 'bold'))],
                    [sg.Image(filename='img\png\InputL.png',background_color='#98D7C2',pad=(0,0)),sg.Input(size=(25, 0), key='cb',pad=(0,0),border_width=0,background_color="#FFFFFF"),sg.Image(filename='img\png\InputR.png',background_color='#98D7C2',pad=(0,0))],
                    [sg.Text('DCT (Dobra cutânea tricipital):',pad=((0,0),(15,0)), size=(35, 0), font=('Roboto', 12, 'bold'))],
                    [sg.Image(filename='img\png\InputL.png',background_color='#98D7C2',pad=(0,0)),sg.Input(size=(25, 0), key='dct',pad=(0,0),border_width=0,background_color="#FFFFFF"),sg.Image(filename='img\png\InputR.png',background_color='#98D7C2',pad=(0,0))],
                    [sg.Text('AJ (Altura do joelho):',pad=((0,0),(15,0)), size=(30, 0), font=('Roboto', 12, 'bold'))],
                    [sg.Image(filename='img\png\InputL.png',background_color='#98D7C2',pad=(0,0)),sg.Input(size=(25, 0), key='aj',pad=(0,0),border_width=0,background_color="#FFFFFF"),sg.Image(filename='img\png\InputR.png',background_color='#98D7C2',pad=(0,0))],
                    [sg.Text('CC (Circunferência de cintura):',pad=((0,0),(15,0)), size=(35, 0), font=('Roboto', 12, 'bold'))],
                    [sg.Image(filename='img\png\InputL.png',background_color='#98D7C2',pad=(0,0)),sg.Input(size=(25, 0), key='cc',pad=(0,0),border_width=0,background_color="#FFFFFF"),sg.Image(filename='img\png\InputR.png',background_color='#98D7C2',pad=(0,0))],
                    [sg.Text('CQ (Circunferência do quadril):',pad=((0,0),(15,0)), size=(35, 0), font=('Roboto', 12, 'bold'))],
                    [sg.Image(filename='img\png\InputL.png',background_color='#98D7C2',pad=(0,0)),sg.Input(size=(25, 0), key='cq',pad=(0,0),border_width=0,background_color="#FFFFFF"),sg.Image(filename='img\png\InputR.png',background_color='#98D7C2',pad=(0,0))],
                    ],scrollable=True, vertical_scroll_only=True,size=(340,500),sbar_arrow_color='',sbar_frame_color='#007AA2',sbar_background_color='#007AA2',sbar_trough_color='#98D7C2',sbar_width=5,sbar_relief=sg.RELIEF_FLAT)],
                    [sg.Column([[sg.Button(key='Enviar Dados', image_data=enviar, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, pad=(None, 20))]], justification='center')]
               ],),
            ],
          
        ]

        return sg.Window('Dados do paciente', layout = layout ,finalize=True,)
#==============================================================

#================= RELATORIO DO PACIENTE=======================  
#  USAR DATA DO ATENDIMENTO COMO BUSCA
#  GUARDAR RELATORIOS, TAG = NOME DO PACIENTE
#  TENTAR FAZER UMA PLANILHA INTELIGENTE, DEPENDENDO DE VALORES, UM TIPO DE RELATORIO APARECE UTILIZAR O IF
#    
def janelaResult():
    # Temas do layout 
    sg.theme_background_color('#98D7C2')
    sg.theme_text_element_background_color('#98D7C2')
    sg.theme_button_color('#742e2b')
    sg.theme_text_color('Black')
    sg.theme_element_background_color('#fdefc5')
    #Resolver BO de Tamanho do layout

    layout = [
            [sg.Image(filename=("img\png\planoFundo2.png" ),background_color='#98D7C2')],
            [sg.Column((
            [sg.Text("Nome: %s" %nome,size=(25,0)), sg.Text('Idade: %s'%idade,size=(20,0)) , sg.Text('Gênero: %s'%sexoS,size=(23,0))],
            [sg.Text('Peso: %s'%peso,size=(25,0)),sg.Text('Altura: %s'%altura,size=(20,0)), sg.Text('Cor da pele: %s'%etniaClas,size=(23,0))],
            [sg.Text('IMC: {:.2f}'.format(resultN) ,size=(35,0)),sg.Text('Classificação IMC:%s' % resultC,size=(35,0))],
            [sg.Text('Adequação CB: {:.2f}'.format(resultCB),size=(35,0)), sg.Text('Classificação CB: %s' % ClassCB,size=(35,0))],
            [sg.Text('Peso Ideal: {}'.format(pesoid_text), size=(35, 0)), sg.Text('Peso Máximo: %4.2f'%pesoMax,size=(35,0))],
            [sg.Text('Adequação DCT:%4.2f'%resultDCT,size=(35,0)), sg.Text('Classificação DCT: %s'%ClassDCT,size=(35,0))],
            [sg.Text('PE (Estimativa de Peso): %s'%pe,size=(35,0)),sg.Text('AE (Estimativa de Altura): %s' %ae,size=(35,0))],
            [sg.Text('CMB (Circunferência muscular do braço): {}'.format(cmb_text) ,size=(72,0))],
            ),background_color='#007AA2')],
            [sg.Button('Voltar')]
            ]
        
    
        
    return sg.Window('Resultado do paciente', layout = layout, finalize=True)

janela1, janela2, janela3, janela4 = janelaPrinc(),None,None,None
#====================================================

#============DECLARAÇÃO DE VALORES===================
while True:
    
    window,event,values = sg.read_all_windows()
    
    if event == 'masc':
        window['M'].update(value=True)
        window['masc'].update(filename='img\png\M_True.png')
        window['fem'].update(filename='img\png\F_False.png')
    if event == 'fem':
        window['F'].update(value=True)
        window['masc'].update(filename='img\png\M_False.png')
        window['fem'].update(filename='img\png\F_True.png')
    if event == 'branc':
        window['B'].update(value=True)
        window['branc'].update(filename='img\png\B_True.png')
        window['ne'].update(filename='img\png\P_False.png')
    if event == 'ne':
        window['N'].update(value=True)
        window['branc'].update(filename='img\png\B_False.png')
        window['ne'].update(filename='img\png\P_True.png')
        
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1 = janelaPrinc()
    if window == janela2 and event == sg.WIN_CLOSED:
        break
      
    if  event == 'Enviar Dados':
        nome = str(values['nome'])
        idade = (values['idade'])
        altura = (values['altura'])
        aj =  (values['aj'])
        cb = (values['cb'])  
        dct = (values['dct'])
        peso = (values['peso'])
        cc = (values['cc'])
        cq = (values['cq'])
    
    
    
        if values['B'] == True:
            etnia = 'B'
            etniaClas = "Branco(a)"
        elif values['N'] == True:
            etnia = 'N'
            etniaClas = "Negro(a)"
        else:
            etnia = ''
            etniaClas = "Não informado"

        if values['M'] == True:
            sexo = 'M'
            sexoS = 'Masculino'
        elif values['F'] == True:
            sexo = 'F'
            sexoS = 'Feminino'
        else:
            sexo = ''
            sexoS = "Não informado"
            
    #=================================================
        
    #=========== Valores Vazios ======================
    

        if idade == '':
            idade = int(0)
        else:
            idade = int(values['idade'])
        if peso == '':
            peso = float(0)
        else:
            peso = float(values['peso'])
        if altura == '':
            altura = float(0)
        else:
            altura = float(values['altura'])
            
        if aj == '':
            aj = float(0)
        else:
            aj = float(values['aj'])

        if cb == '':
            cb = float(0)
        else:
            cb = float(values['cb'])

        if dct == '':
            dct = float(0)
        else:
            dct = float(values['dct'])

        if cc == '':
            cc = float(0)
        else:
            cc = float(values['cc'])

        if cq == '':
            cq = float(0)
        else:
            cq = float(values['cq'])

        if nome == '':
            nome = "Nome não informado"
    #=========================================================


    #============= CALCULOS E FUNÇÕES=========================  
        pe = calpe(aj, cb, sexo, etnia, idade )
        ae = estalt(idade,sexo,aj)
        cmb = CMB(cb,dct)
        resultCB = Calpercentil.CbPercentil(cb,idade,sexo)
        ClassCB = Calpercentil.NameAdq(resultCB)
    
        if idade == 0 or peso == 0 or altura == 0:
            resultN = 0
            resultC = 'IMC Indisponivél'
        else:       
            resultN = imcV(idade,altura,peso)
            resultC = str(imc(idade,altura,peso))  
        
        resultDCT = DCTCalpercentil.DCTPercentil(dct,idade,sexo)
        ClassDCT = DCTCalpercentil.NameAdq(resultDCT)
        pesoid = pesoI(sexo,altura,idade)
        pesoMax = 25 * (altura ** 2)

        if isinstance(pesoid, str):
            pesoid_text = 'Peso Ideal não calculado'
        else:
            pesoid_text = '{:.2f}'.format(float(pesoid))

        if isinstance(cmb, str):
            cmb_text = 'Calculo Indisponivel'
        else:
            cmb_text = '{:.2f}'.format(float(cmb))
        
        if cc == 0 or cq == 0:
            ResultRCQ = "Dados não informados"
        else:
            ResultRCQ = ResultRCQ(cc,cq)

        if peso == 0:
                peso = 'Peso não informado' 
        if altura == 0:
            altura = 'Altura não informada'

         


    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Enviar Dados':
        janela2 = janelaResult()
        janela1.hide()
    

   # if window == janela2 and event == 'Calcular CB':
       # janela2 = janelaResult()


