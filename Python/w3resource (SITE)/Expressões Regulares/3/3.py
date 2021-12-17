import re

string = 'Mais uma noite como todas as anteriores. Pego minha caneca de café cheia, ' \
         'acendo meu ultimo cigarro e corro pra velha janela do quarto. Observo a noite fria e chuvosa, ' \
         'até parece confortável por um momento, se não fossem as dezenas de preocupações que me ' \
         'desmotivam a cada dia. Penso em você, mesmo sabendo o quão longe está de mim, sinto aquele ' \
         'amor que continua a me desgraçar intensameeeente a cada dia, e penso quando enfim poderei te ter comigo. ' \
         'Sei lá, o café chega ao fim e trago a ultima ponta, nada muda. É como se eu fosse passar por isso mais uns' \
         ' longos anos a frente. teem, teeeem, teeeeeeem tem'


def cheque(string):
    if re.match('ab+', string):
        return 'Match!'
    return 'Not a match!'

print(cheque('a'))
