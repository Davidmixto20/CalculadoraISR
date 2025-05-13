tssPorciento = 0.0591
Bonificaion = 0.10

def CalculoDeMiISR(sueldo_mensual):
    if sueldo_mensual <= 34685:
        return 0
    elif sueldo_mensual <= 52027.42:
        excedente = sueldo_mensual - 34685
        return excedente * 0.15
    elif sueldo_mensual <= 72260.25:
        excedente = sueldo_mensual - 52027.43
        return 2601.34 + (excedente * 0.20)
    else:
        excedente = sueldo_mensual - 72260.25
        return 6648.00 + (excedente * 0.25)

try:
    sueldo_bruto = float(input("Dame tu sueldo bruto mensual: "))
    if sueldo_bruto <= 23223:
        print("El sueldo bruto debe ser un valor positivo.")
        exit()

    otros_descuentos = float(input("Pon otros descuentos aqui (si no hay, ponga 0): "))
    if otros_descuentos < 0:
        print("Los descuentos no pueden ser negativos.")
        exit()

    AplicacionDeLaBonificacion = input("Tienes bonificacion? (s/n): ").lower() == 's'

    descuento_tss = sueldo_bruto * tssPorciento
    isr = CalculoDeMiISR(sueldo_bruto)
    bonificacion = sueldo_bruto * Bonificaion if AplicacionDeLaBonificacion else 0

    sueldo_total = sueldo_bruto - descuento_tss - isr - otros_descuentos + bonificacion

    print("\n===== Detalle del Cálculo de Sueldo =====")
    print(f"Sueldo Bruto: RD${sueldo_bruto:,.2f}")
    print(f"Descuento Seguridad Social (TSS): RD${descuento_tss:,.2f}")
    print(f"Retención ISR: RD${isr:,.2f}")
    print(f"Otros Descuentos: RD${otros_descuentos:,.2f}")
    print(f"Bonificación: RD${bonificacion:,.2f}")
    print(f"➡ Sueldo Neto: RD${sueldo_total:,.2f}")

except ValueError:
    print("Entrada inválida. Por favor ingrese valores numéricos.")
