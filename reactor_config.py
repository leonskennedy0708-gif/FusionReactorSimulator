class ITERConfig:
    """
    ITER-inspired reference configuration.

    Values are based on published ITER design/reference parameters.
    This project remains an educational simulation, not an ITER control model.
    """

    # -------------------------
    # Plasma geometry
    # -------------------------

    MAJOR_RADIUS = 6.2          # m
    MINOR_RADIUS = 2.0          # m
    PLASMA_VOLUME = 830.0       # m³

    # -------------------------
    # Magnetic system
    # -------------------------

    TOROIDAL_FIELD = 5.3        # Tesla
    MAX_PLASMA_CURRENT = 15.0   # MA

    # -------------------------
    # Plasma conditions
    # -------------------------

    TARGET_TEMPERATURE = 150.0  # million °C
    TARGET_DENSITY = 1.0e20     # particles/m³

    # -------------------------
    # Heating system
    # -------------------------

    NOMINAL_HEATING_POWER = 50.0    # MW
    MAX_HEATING_POWER = 50.0        # MW

    # -------------------------
    # Fusion performance
    # -------------------------

    TARGET_FUSION_POWER = 500.0     # MW
    TARGET_Q = 10.0

    # -------------------------
    # Pulse operation
    # -------------------------

    NOMINAL_PULSE_TIME = 400.0      # seconds
    MAX_PULSE_TIME = 600.0           # seconds

    # -------------------------
    # Neutron loading
    # -------------------------

    TARGET_NEUTRON_WALL_LOAD = 0.5   # MW/m²

    # -------------------------
    # Magnet system
    # -------------------------

    MAGNET_TEMPERATURE = 4.0         # K
    MAGNET_STORED_ENERGY = 51.0      # GJ

    # -------------------------
    # Divertor
    # -------------------------

    MAX_DIVERTOR_HEAT_LOAD = 20.0    # MW/m²