from CuentaBancaria import CuentaBancaria

cuenta1 = CuentaBancaria(100)
cuenta2 = CuentaBancaria(50)

cuenta1.depósito(100).depósito(100).depósito(200).retiro(10).generar_interés().mostrar_info_cuenta()

cuenta2.depósito(1000).depósito(1000).retiro(250).retiro(250).retiro(100).retiro(150).generar_interés().mostrar_info_cuenta()

CuentaBancaria.print_cuentas()