i = 1
total = 0
while True:
    produk = float(input(f'Produk ke-{i} = '))
    if produk != 0:
        total += produk
        i += 1
    else:
        print(f'Total sebelum diskon: Rp {total}')
        print(f'Diskon 10%: Rp {total * 0.1}')
        print(f'Total setelah diskon: Rp {total - (total * 0.1)}')
        break
