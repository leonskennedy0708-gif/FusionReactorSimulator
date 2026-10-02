from reactor_config import ITERConfig


class FusionReactor:
    """
    Core reactor state for the educational ITER-referenced
    fusion reactor simulator.
    """

    def __init__(self):

        # -----------------------------------------------------
        # REFERENCE CONFIGURATION
        # -----------------------------------------------------

        self.config = ITERConfig()

        # -----------------------------------------------------
        # REACTOR STATE
        # -----------------------------------------------------

        self.status = "OFF"

        # -----------------------------------------------------
        # PLASMA PARAMETERS
        # -----------------------------------------------------

        self.plasma_temperature = 0.0       # million °C
        self.plasma_density = 0.0           # particles/m³
        self.plasma_current = 0.0           # MA

        # -----------------------------------------------------
        # MAGNETIC CONFINEMENT
        # -----------------------------------------------------

        self.toroidal_field = 0.0           # Tesla
        self.poloidal_field = 0.0           # Tesla

        # -----------------------------------------------------
        # HEATING AND FUELING
        # -----------------------------------------------------

        self.heating_power = 0.0            # MW
        self.fuel_injection = 0.0           # %

        # -----------------------------------------------------
        # REACTOR PERFORMANCE
        # -----------------------------------------------------

        self.fusion_power = 0.0             # MW
        self.plasma_stability = 0.0         # %
        self.confinement = 0.0              # %

        # -----------------------------------------------------
        # THERMAL SYSTEM
        # -----------------------------------------------------

        self.wall_load = 0.0                # MW/m²
        self.divertor_temperature = 300.0   # K

        # -----------------------------------------------------
        # FUSION PERFORMANCE
        # -----------------------------------------------------

        self.q_factor = 0.0

    # =========================================================
    # PLASMA START
    # =========================================================

    def start_plasma(self):
        """
        Begin plasma initiation.
        """

        if self.status == "OFF":
            self.status = "STARTING"
            print("Plasma initiation started.")

        else:
            print(
                f"Cannot start plasma. "
                f"Current status: {self.status}"
            )

    # =========================================================
    # Q FACTOR
    # =========================================================

    def calculate_q_factor(self):
        """
        Calculate fusion gain Q.

        Q = fusion power / auxiliary heating power
        """

        if self.heating_power <= 0:
            self.q_factor = 0.0
            return

        self.q_factor = (
            self.fusion_power
            / self.heating_power
        )

    # =========================================================
    # RESET REACTOR
    # =========================================================

    def shutdown(self):
        """
        Safely reset the simulated reactor to OFF.
        """

        self.status = "SHUTTING DOWN"

        self.heating_power = 0.0
        self.fuel_injection = 0.0

        self.fusion_power = 0.0
        self.q_factor = 0.0

        self.plasma_current = 0.0
        self.plasma_temperature = 0.0
        self.plasma_density = 0.0

        self.plasma_stability = 0.0
        self.confinement = 0.0

        self.toroidal_field = 0.0
        self.poloidal_field = 0.0

        self.wall_load = 0.0
        self.divertor_temperature = 300.0

        self.status = "OFF"

        print("Plasma shutdown complete.")

    # =========================================================
    # DISPLAY STATUS
    # =========================================================

    def display_status(self):
        """
        Display the current reactor state.
        """

        print("\n===== FUSION REACTOR =====")

        print(f"Status:               {self.status}")

        print(
            f"Plasma Temperature:   "
            f"{self.plasma_temperature:.2f} million °C"
        )

        print(
            f"Plasma Density:       "
            f"{self.plasma_density:.2e} particles/m³"
        )

        print(
            f"Plasma Current:       "
            f"{self.plasma_current:.2f} MA"
        )

        print(
            f"Toroidal Field:       "
            f"{self.toroidal_field:.2f} T"
        )

        print(
            f"Poloidal Field:       "
            f"{self.poloidal_field:.2f} T"
        )

        print(
            f"Heating Power:        "
            f"{self.heating_power:.2f} MW"
        )

        print(
            f"Fuel Injection:       "
            f"{self.fuel_injection:.2f}%"
        )

        print(
            f"Fusion Power:         "
            f"{self.fusion_power:.2f} MW"
        )

        print(
            f"Q Factor:             "
            f"{self.q_factor:.2f}"
        )

        print(
            f"Plasma Stability:     "
            f"{self.plasma_stability:.2f}%"
        )

        print(
            f"Confinement:          "
            f"{self.confinement:.2f}%"
        )

        print(
            f"Wall Load:            "
            f"{self.wall_load:.2f} MW/m²"
        )

        print(
            f"Divertor Temperature: "
            f"{self.divertor_temperature:.2f} K"
        )

        print("===========================\n")