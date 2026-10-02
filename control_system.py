class ControlSystem:
    """
    Controls the operating sequence of the educational
    ITER-referenced fusion reactor simulator.
    """

    def __init__(self, reactor, physics):
        self.reactor = reactor
        self.physics = physics

        self.stage = "OFF"

    # =========================================================
    # STARTUP SEQUENCE
    # =========================================================

    def start_sequence(self):
        """Begin the reactor startup sequence."""

        if self.stage != "OFF":
            print("Reactor startup cannot begin.")
            print(f"Current stage: {self.stage}")
            return

        self.stage = "VACUUM"
        self.reactor.status = "VACUUM"

        print("Startup sequence initiated.")
        print("Stage: VACUUM")

    # =========================================================
    # ADVANCE OPERATING STAGE
    # =========================================================

    def advance_stage(self):
        """Advance the reactor through its operating sequence."""

        if self.stage == "OFF":

            print("Reactor is OFF. Start the sequence first.")
            return

        # -----------------------------------------------------
        # VACUUM
        # -----------------------------------------------------

        elif self.stage == "VACUUM":

            self.stage = "MAGNET CHARGE"
            self.reactor.status = "MAGNET CHARGE"

            self.reactor.toroidal_field = (
                self.reactor.config.TOROIDAL_FIELD
            )

            print("Toroidal magnets charged.")

        # -----------------------------------------------------
        # MAGNET CHARGE
        # -----------------------------------------------------

        elif self.stage == "MAGNET CHARGE":

            self.stage = "PLASMA INIT"
            self.reactor.status = "STARTING"

            self.reactor.fuel_injection = 10.0

            print("Plasma initiation sequence started.")

        # -----------------------------------------------------
        # PLASMA INIT
        # -----------------------------------------------------

        elif self.stage == "PLASMA INIT":

            self.stage = "CURRENT RAMP"
            self.reactor.status = "CURRENT RAMP"

            self.reactor.fuel_injection = 50.0

            self.physics.update()

            print("Plasma established.")
            print("Beginning plasma current ramp.")

        # -----------------------------------------------------
        # CURRENT RAMP
        # -----------------------------------------------------

        elif self.stage == "CURRENT RAMP":

            self.stage = "HEATING"
            self.reactor.status = "HEATING"

            self.reactor.fuel_injection = 100.0

            self.physics.update()

            print("Plasma current ramp completed.")
            print("Beginning auxiliary heating.")

        # -----------------------------------------------------
        # HEATING
        # -----------------------------------------------------

        elif self.stage == "HEATING":

            self.stage = "FUSION"
            self.reactor.status = "FUSION"

            self.reactor.heating_power = (
                self.reactor.config.NOMINAL_HEATING_POWER
            )

            self.physics.update()

            self.reactor.calculate_q_factor()

            print("Auxiliary heating active.")
            print("Fusion conditions developing.")

        # -----------------------------------------------------
        # FUSION
        # -----------------------------------------------------

        elif self.stage == "FUSION":

            self.stage = "STEADY STATE"
            self.reactor.status = "STEADY STATE"

            self.reactor.heating_power = (
                self.reactor.config.NOMINAL_HEATING_POWER
            )

            self.reactor.fuel_injection = 100.0

            self.physics.update()

            self.reactor.calculate_q_factor()

            print("Fusion conditions established.")
            print("Reactor entered steady state.")

        # -----------------------------------------------------
        # STEADY STATE
        # -----------------------------------------------------

        elif self.stage == "STEADY STATE":

            self.physics.update()
            self.reactor.calculate_q_factor()

            print("Reactor remains in steady state.")
            return

        print(f"Stage advanced to: {self.stage}")

    # =========================================================
    # SHUTDOWN
    # =========================================================

    def shutdown_sequence(self):
        """Begin normal reactor shutdown."""

        if self.stage == "OFF":

            print("Reactor is already OFF.")
            return

        self.stage = "RAMP DOWN"
        self.reactor.status = "RAMP DOWN"

        self.reactor.heating_power = 0.0
        self.reactor.fuel_injection = 0.0

        self.physics.update()

        print("Shutdown sequence initiated.")
        print("Heating and fuel injection reduced.")

    # =========================================================
    # COMPLETE SHUTDOWN
    # =========================================================

    def complete_shutdown(self):
        """Complete the reactor shutdown."""

        self.reactor.shutdown()

        self.stage = "OFF"

        print("Reactor shutdown complete.")

    # =========================================================
    # EMERGENCY SHUTDOWN
    # =========================================================

    def emergency_shutdown(self):
        """Immediately shut down the simulated reactor."""

        print("!!! EMERGENCY SHUTDOWN !!!")

        self.reactor.shutdown()

        self.stage = "OFF"

        print("Emergency shutdown complete.")

    # =========================================================
    # DISPLAY STAGE
    # =========================================================

    def display_stage(self):
        """Display the current reactor stage."""

        print(
            f"Current reactor stage: {self.stage}"
        )