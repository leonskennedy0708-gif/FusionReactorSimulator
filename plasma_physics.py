import math


class PlasmaPhysics:
    def __init__(self, reactor):
        self.reactor = reactor

    def calculate_confinement(self):
        """
        Estimate plasma confinement from the magnetic fields.

        This is a simplified simulation model.
        """

        magnetic_strength = (
            self.reactor.toroidal_field * 0.7
            + self.reactor.poloidal_field * 0.3
        )

        confinement = magnetic_strength * 12

        # Keep confinement between 0 and 100%
        confinement = max(0, min(100, confinement))

        self.reactor.confinement = confinement

    def calculate_temperature(self):
        """
        Estimate plasma temperature from heating
        and confinement.
        """

        heating = self.reactor.heating_power
        confinement = self.reactor.confinement

        temperature = (
            heating * 0.8
            + confinement * 0.25
        )

        # Limit temperature for our simulation
        temperature = max(0, min(200, temperature))

        self.reactor.plasma_temperature = temperature

    def calculate_density(self):
        """
        Estimate plasma density from fuel injection.
        """

        fuel = self.reactor.fuel_injection

        # Simplified density model
        density = fuel * 1e19

        self.reactor.plasma_density = density

    def calculate_plasma_current(self):
        """
        Estimate plasma current from magnetic confinement
        and fueling.
        """

        magnetic_field = (
            self.reactor.toroidal_field
            + self.reactor.poloidal_field
        )

        current = magnetic_field * 1.5

        current *= (0.5 + self.reactor.fuel_injection / 200)

        # Limit current to our simulated operating range
        current = max(0, min(20, current))

        self.reactor.plasma_current = current

    def calculate_stability(self):
        """
        Estimate plasma stability.

        Excessive temperature, current, or insufficient
        magnetic confinement reduces stability.
        """

        temperature = self.reactor.plasma_temperature
        current = self.reactor.plasma_current
        confinement = self.reactor.confinement

        stability = 50

        # Magnetic confinement improves stability
        stability += confinement * 0.4

        # Excessive current reduces stability
        if current > 15:
            stability -= (current - 15) * 5

        # Excessive temperature reduces stability
        if temperature > 150:
            stability -= (temperature - 150) * 0.4

        stability = max(0, min(100, stability))

        self.reactor.plasma_stability = stability

    def calculate_fusion_power(self):
        """
        Estimate fusion power from temperature,
        density and confinement.

        This is intentionally simplified.
        """

        temperature = self.reactor.plasma_temperature
        density = self.reactor.plasma_density
        confinement = self.reactor.confinement

        density_factor = density / 1e19

        # Fusion becomes significant at higher temperatures.
        temperature_factor = max(0, temperature - 50) / 150

        fusion_power = (
            temperature_factor
            * density_factor
            * (confinement / 100)
            * 1000
        )

        # Stability affects useful fusion power
        fusion_power *= self.reactor.plasma_stability / 100

        fusion_power = max(0, fusion_power)

        self.reactor.fusion_power = fusion_power

    def calculate_wall_load(self):
        """
        Estimate thermal load on the reactor wall/divertor.
        """

        fusion_power = self.reactor.fusion_power

        wall_load = fusion_power / 100

        self.reactor.wall_load = max(0, wall_load)

    def update(self):
        """
        Run one complete physics calculation cycle.
        """

        self.calculate_confinement()
        self.calculate_density()
        self.calculate_plasma_current()
        self.calculate_temperature()
        self.calculate_stability()
        self.calculate_fusion_power()
        self.calculate_wall_load()