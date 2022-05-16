larg = float(input('Digite a largura da parede '))
alt = float(input('Digite a altura da parede'))
área = larg * alt
print('sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, área))
tinta = área/2
print('para essa parede você precisà de {} L de tintas '.format(tinta))