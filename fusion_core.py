class FusionReactor:
    def __init__(self):
        # Reactor state
        self.status = "OFF"

        # Plasma parameters
        self.plasma_temperature = 0.0      # million Kelvin (MK)
        self.plasma_density = 0.0           # particles/m³
        self.plasma_current = 0.0           # Mega-Amps (MA)

        # Magnetic confinement
        self.toroidal_field = 0.0            # Tesla
        self.poloidal_field = 0.0            # Tesla

        # Heating and fueling
        self.heating_power = 0.0             # MW
        self.fuel_injection = 0.0            # %

        # Reactor performance
        self.fusion_power = 0.0              # MW
        self.plasma_stability = 0.0          # %
        self.confinement = 0.0               # %

        # Thermal system
        self.wall_load = 0.0                 # MW/m²
        self.divertor_temperature = 300.0    # Kelvin

    def start_plasma(self):
        """Start the plasma initiation sequence."""

        if self.status == "OFF":
            self.status = "STARTING"
            print("Plasma initiation started.")

    def shutdown(self):
        """Safely shut down the plasma."""

        self.status = "SHUTTING DOWN"

        self.heating_power = 0.0
        self.fuel_injection = 0.0

        self.fusion_power = 0.0
        self.plasma_current = 0.0
        self.plasma_temperature = 0.0
        self.plasma_density = 0.0

        self.status = "OFF"

        print("Plasma shutdown complete.")

    def display_status(self):
        """Display the current reactor state."""

        print("\n===== FUSION REACTOR =====")
        print(f"Status:              {self.status}")
        print(f"Plasma Temperature:  {self.plasma_temperature:.2f} MK")
        print(f"Plasma Density:      {self.plasma_density:.2e}")
        print(f"Plasma Current:      {self.plasma_current:.2f} MA")
        print(f"Toroidal Field:      {self.toroidal_field:.2f} T")
        print(f"Poloidal Field:      {self.poloidal_field:.2f} T")
        print(f"Heating Power:       {self.heating_power:.2f} MW")
        print(f"Fuel Injection:      {self.fuel_injection:.2f}%")
        print(f"Fusion Power:        {self.fusion_power:.2f} MW")
        print(f"Plasma Stability:    {self.plasma_stability:.2f}%")
        print(f"Confinement:         {self.confinement:.2f}%")
        print(f"Wall Load:           {self.wall_load:.2f} MW/m²")
        print(f"Divertor Temperature:{self.divertor_temperature:.2f} K")
        print("===========================\n")