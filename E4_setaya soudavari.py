Rooz = int(input(' Rooz ra vared konid: '))
Mah = int(input(' Mah ra vared konid: '))
Sal = int(input(' Sal ra vared konid: '))
Roozha = [31,28,31,30,31,30,31,31,30,31,30,31]
Tedad_Roozha = sum(Roozha[0:(Mah - 1)]) + Rooz

if Sal % 400 == 0:
    if Mah > 2:
        print("Tedad Roozhaye Gozashte:", Tedad_Roozha + 1)
    else: print("Tedad Roozhaye Gozashte:", Tedad_Roozha)
elif Sal % 4 == 0 and Sal % 100 != 0:
    if Mah > 2:
        print("Tedad Roozhaye Gozashte:", Tedad_Roozha + 1)
    else:
        print("Tedad Roozhaye Gozashte:", Tedad_Roozha)
else:
    print("Tedad Roozhaye Gozashte:", Tedad_Roozha)
