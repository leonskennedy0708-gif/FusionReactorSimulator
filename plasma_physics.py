class PlasmaPhysics:
    """
    Educational 0-D plasma model for an ITER-referenced
    fusion reactor simulator.

    This is NOT a full tokamak equilibrium or transport model.
    The equations are simplified and intended for education.
    """

    def __init__(self, reactor):
        self.reactor = reactor
        self.config = reactor.config

    # ---------------------------------------------------------
    # MAGNETIC CONFINEMENT
    # ---------------------------------------------------------

    def calculate_confinement(self):
        """
        Estimate magnetic confinement relative to the
        ITER reference toroidal field.
        """

        toroidal_field = self.reactor.toroidal_field
        reference_field = self.config.TOROIDAL_FIELD

        if reference_field <= 0:
            self.reactor.confinement = 0.0
            return

        confinement = (
            toroidal_field / reference_field
        ) * 100.0

        confinement = max(0.0, min(100.0, confinement))

        self.reactor.confinement = confinement

    # ---------------------------------------------------------
    # PLASMA TEMPERATURE
    # ---------------------------------------------------------

    def calculate_temperature(self):
        """
        Estimate plasma temperature from auxiliary heating
        and magnetic confinement.

        Educational approximation only.
        """

        heating = self.reactor.heating_power
        confinement = self.reactor.confinement

        target_temperature = self.config.TARGET_TEMPERATURE
        target_heating = self.config.NOMINAL_HEATING_POWER

        if target_heating <= 0:
            self.reactor.plasma_temperature = 0.0
            return

        heating_factor = heating / target_heating
        confinement_factor = confinement / 100.0

        temperature = (
            target_temperature
            * heating_factor
            * confinement_factor
        )

        temperature = max(
            0.0,
            min(target_temperature, temperature)
        )

        self.reactor.plasma_temperature = temperature

    # ---------------------------------------------------------
    # PLASMA DENSITY
    # ---------------------------------------------------------

    def calculate_density(self):
        """
        Estimate plasma density from the fuel injection level.

        The density is scaled between zero and the ITER
        reference density.

        Educational approximation only.
        """

        fuel = self.reactor.fuel_injection

        target_density = self.config.TARGET_DENSITY

        fuel_fraction = fuel / 100.0

        density = target_density * fuel_fraction

        density = max(
            0.0,
            min(target_density, density)
        )

        self.reactor.plasma_density = density

    # ---------------------------------------------------------
    # PLASMA CURRENT
    # ---------------------------------------------------------

    def calculate_plasma_current(self):
        """
        Estimate plasma current as a controlled quantity.

        The current approaches the ITER reference plasma
        current as the plasma initiation/current-ramp
        conditions become established.

        Educational approximation only.
        """

        target_current = self.config.MAX_PLASMA_CURRENT

        confinement_factor = self.reactor.confinement / 100.0
        fuel_factor = self.reactor.fuel_injection / 100.0

        current = (
            target_current
            * confinement_factor
            * fuel_factor
        )

        current = max(
            0.0,
            min(target_current, current)
        )

        self.reactor.plasma_current = current

    # ---------------------------------------------------------
    # PLASMA STABILITY
    # ---------------------------------------------------------

    def calculate_stability(self):
        """
        Estimate plasma stability from temperature,
        plasma current, and magnetic confinement.

        Educational approximation only.
        """

        temperature = self.reactor.plasma_temperature
        current = self.reactor.plasma_current
        confinement = self.reactor.confinement

        target_temperature = self.config.TARGET_TEMPERATURE
        target_current = self.config.MAX_PLASMA_CURRENT

        if target_temperature <= 0 or target_current <= 0:
            self.reactor.plasma_stability = 0.0
            return

        temperature_factor = (
            temperature / target_temperature
        )

        current_factor = (
            current / target_current
        )

        stability = (
            100.0
            * temperature_factor
            * current_factor
            * (confinement / 100.0)
        )

        stability = max(
            0.0,
            min(100.0, stability)
        )

        self.reactor.plasma_stability = stability

    # ---------------------------------------------------------
    # FUSION POWER
    # ---------------------------------------------------------

    def calculate_fusion_power(self):
        """
        Estimate fusion power from plasma temperature,
        density, confinement, and stability.

        The result is scaled toward the ITER reference
        fusion power.

        Educational approximation only.
        """

        temperature = self.reactor.plasma_temperature
        density = self.reactor.plasma_density
        confinement = self.reactor.confinement
        stability = self.reactor.plasma_stability

        target_temperature = self.config.TARGET_TEMPERATURE
        target_density = self.config.TARGET_DENSITY
        target_power = self.config.TARGET_FUSION_POWER

        if (
            target_temperature <= 0
            or target_density <= 0
        ):
            self.reactor.fusion_power = 0.0
            return

        temperature_factor = (
            temperature / target_temperature
        )

        density_factor = (
            density / target_density
        )

        confinement_factor = (
            confinement / 100.0
        )

        stability_factor = (
            stability / 100.0
        )

        fusion_power = (
            target_power
            * temperature_factor
            * density_factor
            * confinement_factor
            * stability_factor
        )

        fusion_power = max(0.0, fusion_power)

        self.reactor.fusion_power = fusion_power

    # ---------------------------------------------------------
    # WALL LOAD
    # ---------------------------------------------------------

    def calculate_wall_load(self):
        """
        Estimate average thermal/neutron wall loading
        from fusion power.

        Educational approximation only.
        """

        fusion_power = self.reactor.fusion_power
        plasma_volume = self.config.PLASMA_VOLUME

        if plasma_volume <= 0:
            self.reactor.wall_load = 0.0
            return

        wall_load = fusion_power / plasma_volume

        self.reactor.wall_load = max(
            0.0,
            wall_load
        )

    # ---------------------------------------------------------
    # DIVERTOR TEMPERATURE
    # ---------------------------------------------------------

    def calculate_divertor_temperature(self):
        """
        Estimate divertor temperature from thermal loading.

        Educational approximation only.
        """

        wall_load = self.reactor.wall_load

        base_temperature = 300.0

        temperature = (
            base_temperature
            + wall_load * 100.0
        )

        self.reactor.divertor_temperature = max(
            base_temperature,
            temperature
        )

    # ---------------------------------------------------------
    # COMPLETE PHYSICS UPDATE
    # ---------------------------------------------------------

    def update(self):
        """
        Run one complete plasma-physics calculation cycle.
        """

        self.calculate_confinement()
        self.calculate_density()
        self.calculate_plasma_current()
        self.calculate_temperature()
        self.calculate_stability()
        self.calculate_fusion_power()
        self.calculate_wall_load()
        self.calculate_divertor_temperature()