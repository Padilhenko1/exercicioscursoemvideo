cores={'azul':'blue','vermelho':'red','amarelo':'yellow','verde':'green'}
cor=str(input('Qual cor você quer traduzir: ')).lower()
tradução=cores.get(cor,'Essa cor não esta cadastrada.')
print(tradução)
