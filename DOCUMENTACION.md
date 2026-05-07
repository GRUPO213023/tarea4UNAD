# Documentacion del Codigo - Software FJ

Este documento explica la estructura interna del proyecto y como cada archivo aporta al sistema integral de gestion de clientes, servicios y reservas.

## 1. `exceptions.py`

Contiene las excepciones personalizadas del sistema.

La idea es no depender solamente de errores generales de Python, sino crear errores propios del dominio del proyecto.

Excepciones principales:

- `SistemaGestionError`: clase base para errores controlados.
- `DatosInvalidosError`: datos incorrectos, incompletos o duplicados.
- `ServicioNoDisponibleError`: servicio desactivado o no disponible.
- `ReservaError`: errores durante el procesamiento de reservas.
- `OperacionNoPermitidaError`: acciones no validas segun el estado de la reserva.
- `CalculoCostoError`: fallos al calcular costos.

## 2. `logger_config.py`

Configura el archivo de logs del sistema.

Cuando el programa se ejecuta, crea automaticamente la carpeta `logs` y el archivo `software_fj.log`.

En este archivo se registran:

- Operaciones iniciadas.
- Operaciones exitosas.
- Errores controlados.
- Errores inesperados.
- Trazas completas de excepciones.

## 3. `entidades.py`

Contiene la clase abstracta `EntidadSistema` y la clase `Cliente`.

### `EntidadSistema`

Representa una entidad general del sistema. Es abstracta porque no se usa directamente; sirve como base para otras clases.

Incluye:

- Identificador unico.
- Fecha de creacion.
- Nombre validado.
- Metodo abstracto `resumen()`.

### `Cliente`

Representa a una persona o empresa que solicita servicios.

Aplica encapsulacion usando atributos privados:

- `_documento`
- `_correo`
- `_telefono`

Tambien usa propiedades con validaciones para impedir datos invalidos.

## 4. `servicios.py`

Contiene la clase abstracta `Servicio` y tres clases derivadas.

### `Servicio`

Define el comportamiento comun de todos los servicios:

- Nombre.
- Tarifa base.
- Disponibilidad.
- Activacion y desactivacion.
- Calculo de costo total.

El metodo `calcular_costo_total()` simula sobrecarga mediante parametros opcionales:

```python
calcular_costo_total(duracion)
calcular_costo_total(duracion, impuesto=0.19)
calcular_costo_total(duracion, impuesto=0.19, descuento=0.10)
```

### `ReservaSala`

Servicio para reservar salas.

Valida:

- Duracion maxima de 12 horas.
- Cantidad de asistentes.
- Capacidad maxima de la sala.

### `AlquilerEquipo`

Servicio para alquilar equipos.

Valida:

- Duracion maxima de 30 dias.
- Cantidad de unidades.
- Garantia no negativa.

### `AsesoriaEspecializada`

Servicio para asesorias profesionales.

Valida:

- Duracion maxima de 8 horas.
- Modalidad virtual o presencial.

## 5. `reserva.py`

Contiene la clase `Reserva`.

Integra:

- Cliente.
- Servicio.
- Duracion.
- Estado.
- Costo total.
- Fecha de creacion.

Estados posibles:

- `creada`
- `confirmada`
- `procesada`
- `cancelada`

Metodos principales:

- `confirmar()`: valida disponibilidad y cambia el estado.
- `cancelar()`: cancela si la reserva no fue procesada.
- `procesar()`: calcula el costo final usando manejo avanzado de excepciones.

El metodo `procesar()` demuestra:

- `try`
- `except`
- `else`
- `finally`
- Encadenamiento con `raise ... from error`

## 6. `sistema.py`

Contiene la clase `SistemaGestion`.

Funciona como fachada del sistema, es decir, centraliza las operaciones principales.

Maneja listas internas:

- `_clientes`
- `_servicios`
- `_reservas`

No usa base de datos.

El metodo mas importante es `ejecutar_operacion()`, porque permite que el sistema continue funcionando aunque una operacion falle.

## 7. `main.py`

Es el punto de entrada del proyecto.

Aqui se simulan operaciones reales:

- Registro de clientes validos.
- Registro de clientes invalidos.
- Creacion de servicios validos.
- Creacion incorrecta de servicios.
- Reservas exitosas.
- Reservas fallidas.
- Procesamientos exitosos.
- Procesamientos con errores controlados.

Este archivo demuestra que el sistema se mantiene activo incluso cuando ocurren errores.

## Principios de POO aplicados

- Abstraccion: `EntidadSistema` y `Servicio`.
- Herencia: `Cliente` y los servicios especializados heredan de clases base.
- Polimorfismo: cada servicio implementa su propio calculo y descripcion.
- Encapsulacion: uso de atributos privados y propiedades.
- Modularidad: cada archivo tiene una responsabilidad clara.
- Extensibilidad: se pueden agregar nuevos servicios heredando de `Servicio`.

## Manejo de excepciones aplicado

El sistema usa excepciones personalizadas para representar errores propios del negocio.

Tambien registra cada error en logs para facilitar auditoria y depuracion.