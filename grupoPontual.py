# coding:utf-8
# Online Python - IDE, Editor, Compiler, Interpreter
#!/usr/bin/python
answer = input('A molécula é linear? s ou n?')
if answer == 's':
    answer = input('A molécula possui algum centro de inversão i? s ou n?')
    if answer == 's':
        print('Sua molécula é D_inf h')
    else:
        print('Sua molécula é C_inf v')
else:
    answer = input('A molécula possui 2 ou mais C_n com n > 2 ? s ou n?')
    if answer == 's':
        answer = input('A molécula possui algum centro de inversão i? s ou n?')
        if answer == 's':
            answer = input('A molécula é C_5? s ou n?')
            if answer == 's':
                print('Sua molécula é I_h')
            else:
                print('Sua molécula é O_h')
    else:
        answer = input('Um ou mais eixos C_n, onde n é de ordem máxima e n > 1? s ou n?')
        if answer == 's':
            answer = input('Observe o valor de n e determine o eixo principal. Existem n eixos C2 perpendiculares ao eixo principal Cn? s ou n?')
            if answer == 's':
                answer = input('A molécula possui um plano de reflexão horizontal (sigma_h)? Lembre-se sigma_h é um plano perpendicular ao eixo de rotação principal. s ou n?')
                if answer == 's':
                    print('A molécula é D_nh')
                else:
                    answer = input('A molécula possui n sigma_d (plano de simetria diedral)? s ou n?')
                    if answer == 's':
                        print('Sua molécula é D_nd')
                    else:
                        print('Sua molécula é D_n')
            else:
                answer = input('A molécula possui algum sigma_h (plano de simetria horizontal perpendicular ao eixo principal)? s ou n?')
                if answer == 's':
                    print('Sua molécula é C_nh')
                else:
                    answer = input('A molécula possui algum n sigma_v (plano de simetria vertical que inclui o eixo principal? s ou n?')
                    if answer == 's':
                        print('A molécula é C_nv')
                    else:
                        answer = input('A molécula possui S_2n (a roto-reflexão, S, é um C_n seguido de um sigma_h)? s ou n?')
                        if answer =='s':
                            print('A molécula é S_2n')
                        else:
                            print('A molécula é C_n')
        else:
            answer = input('A molécula possui plano de reflexão sigma? s ou n?')
            if answer == 's':
                print('A molécula é C_s')
            else:
                answer = input('A molécula possui algum centro de inversão i? s ou n?')
                if answer == 's':
                    print('A molécula é C_i')
                else:
                    print('A molécula é c_1')
