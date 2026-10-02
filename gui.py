import tkinter as tk
from tkinter import messagebox


from fusion_core import FusionReactor
from plasma_physics import PlasmaPhysics
from control_system import ControlSystem


class FusionReactorGUI:

    def __init__(self, root):

        self.root = root

        # =====================================================
        # WINDOW
        # =====================================================

        self.root.title(
            "Fusion Reactor Control System"
        )

        self.root.geometry(
            "1200x800"
        )

        self.root.minsize(
            1100,
            750
        )

        self.root.configure(
            bg="#0b1117"
        )

        # =====================================================
        # REACTOR SYSTEM
        # =====================================================

        self.reactor = FusionReactor()

        self.physics = PlasmaPhysics(
            self.reactor
        )

        self.controls = ControlSystem(
            self.reactor,
            self.physics
        )

        # =====================================================
        # GUI VARIABLES
        # =====================================================

        self.status_var = tk.StringVar()
        self.stage_var = tk.StringVar()

        self.temperature_var = tk.StringVar()
        self.density_var = tk.StringVar()
        self.current_var = tk.StringVar()
        self.toroidal_var = tk.StringVar()

        self.poloidal_var = tk.StringVar()
        self.confinement_var = tk.StringVar()
        self.stability_var = tk.StringVar()
        self.heating_var = tk.StringVar()

        self.fusion_var = tk.StringVar()
        self.q_var = tk.StringVar()
        self.wall_load_var = tk.StringVar()
        self.divertor_var = tk.StringVar()

        # =====================================================
        # BUILD INTERFACE
        # =====================================================

        self.create_header()
        self.create_status_bar()
        self.create_main_dashboard()
        self.create_controls()
        self.create_event_log()

        self.update_display()

        self.log_event(
            "SYSTEM",
            "Fusion reactor simulator initialized."
        )

    # =========================================================
    # COLORS
    # =========================================================

    BG = "#0b1117"
    PANEL = "#111c26"
    PANEL_LIGHT = "#172531"

    CYAN = "#00d9ff"
    GREEN = "#00e676"
    YELLOW = "#ffd740"
    RED = "#ff5252"

    WHITE = "#ffffff"
    TEXT = "#c8d6e5"
    MUTED = "#78909c"

    # =========================================================
    # HEADER
    # =========================================================

    def create_header(self):

        header = tk.Frame(
            self.root,
            bg=self.BG
        )

        header.pack(
            fill="x",
            padx=25,
            pady=(20, 10)
        )

        title = tk.Label(
            header,
            text="FUSION REACTOR CONTROL SYSTEM",
            font=("Arial", 26, "bold"),
            fg=self.CYAN,
            bg=self.BG
        )

        title.pack()

        subtitle = tk.Label(
            header,
            text="ITER-Referenced Educational 0-D Simulation",
            font=("Arial", 11),
            fg=self.MUTED,
            bg=self.BG
        )

        subtitle.pack(
            pady=(4, 0)
        )

    # =========================================================
    # STATUS BAR
    # =========================================================

    def create_status_bar(self):

        frame = tk.Frame(
            self.root,
            bg=self.PANEL,
            bd=1,
            relief="solid"
        )

        frame.pack(
            fill="x",
            padx=25,
            pady=8
        )

        # -----------------------------------------------------
        # STATUS
        # -----------------------------------------------------

        status_container = tk.Frame(
            frame,
            bg=self.PANEL
        )

        status_container.pack(
            side="left",
            padx=25,
            pady=12
        )

        tk.Label(
            status_container,
            text="REACTOR STATUS",
            font=("Arial", 9, "bold"),
            fg=self.MUTED,
            bg=self.PANEL
        ).pack()

        self.status_indicator = tk.Label(
            status_container,
            textvariable=self.status_var,
            font=("Arial", 17, "bold"),
            fg=self.RED,
            bg=self.PANEL
        )

        self.status_indicator.pack()

        # -----------------------------------------------------
        # STAGE
        # -----------------------------------------------------

        stage_container = tk.Frame(
            frame,
            bg=self.PANEL
        )

        stage_container.pack(
            side="right",
            padx=25,
            pady=12
        )

        tk.Label(
            stage_container,
            text="OPERATING STAGE",
            font=("Arial", 9, "bold"),
            fg=self.MUTED,
            bg=self.PANEL
        ).pack()

        tk.Label(
            stage_container,
            textvariable=self.stage_var,
            font=("Arial", 17, "bold"),
            fg=self.CYAN,
            bg=self.PANEL
        ).pack()

    # =========================================================
    # MAIN DASHBOARD
    # =========================================================

    def create_main_dashboard(self):

        dashboard = tk.Frame(
            self.root,
            bg=self.BG
        )

        dashboard.pack(
            fill="both",
            expand=True,
            padx=25
        )

        # =====================================================
        # PLASMA PARAMETERS
        # =====================================================

        plasma_frame = self.create_section(
            dashboard,
            "PLASMA PARAMETERS"
        )

        plasma_frame.pack(
            fill="x",
            pady=5
        )

        self.create_metric(
            plasma_frame,
            "PLASMA TEMPERATURE",
            self.temperature_var,
            "million °C"
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=8,
            sticky="nsew"
        )

        self.create_metric(
            plasma_frame,
            "PLASMA DENSITY",
            self.density_var,
            "particles/m³"
        ).grid(
            row=0,
            column=1,
            padx=8,
            pady=8,
            sticky="nsew"
        )

        self.create_metric(
            plasma_frame,
            "PLASMA CURRENT",
            self.current_var,
            "MA"
        ).grid(
            row=0,
            column=2,
            padx=8,
            pady=8,
            sticky="nsew"
        )

        self.create_metric(
            plasma_frame,
            "TOROIDAL FIELD",
            self.toroidal_var,
            "Tesla"
        ).grid(
            row=0,
            column=3,
            padx=8,
            pady=8,
            sticky="nsew"
        )

        # =====================================================
        # PERFORMANCE
        # =====================================================

        performance_frame = self.create_section(
            dashboard,
            "FUSION PERFORMANCE"
        )

        performance_frame.pack(
            fill="x",
            pady=5
        )

        self.create_metric(
            performance_frame,
            "CONFINEMENT",
            self.confinement_var,
            "%"
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=8,
            sticky="nsew"
        )

        self.create_metric(
            performance_frame,
            "PLASMA STABILITY",
            self.stability_var,
            "%"
        ).grid(
            row=0,
            column=1,
            padx=8,
            pady=8,
            sticky="nsew"
        )

        self.create_metric(
            performance_frame,
            "AUXILIARY HEATING",
            self.heating_var,
            "MW"
        ).grid(
            row=0,
            column=2,
            padx=8,
            pady=8,
            sticky="nsew"
        )

        self.create_metric(
            performance_frame,
            "FUSION POWER",
            self.fusion_var,
            "MW"
        ).grid(
            row=0,
            column=3,
            padx=8,
            pady=8,
            sticky="nsew"
        )

        # =====================================================
        # THERMAL SYSTEM
        # =====================================================

        thermal_frame = self.create_section(
            dashboard,
            "THERMAL SYSTEM"
        )

        thermal_frame.pack(
            fill="x",
            pady=5
        )

        self.create_metric(
            thermal_frame,
            "Q FACTOR",
            self.q_var,
            ""
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=8,
            sticky="nsew"
        )

        self.create_metric(
            thermal_frame,
            "WALL LOAD PROXY",
            self.wall_load_var,
            "MW/m²"
        ).grid(
            row=0,
            column=1,
            padx=8,
            pady=8,
            sticky="nsew"
        )

        self.create_metric(
            thermal_frame,
            "DIVERTOR TEMPERATURE",
            self.divertor_var,
            "K"
        ).grid(
            row=0,
            column=2,
            padx=8,
            pady=8,
            sticky="nsew"
        )

        self.create_metric(
            thermal_frame,
            "POLOIDAL FIELD",
            self.poloidal_var,
            "Tesla"
        ).grid(
            row=0,
            column=3,
            padx=8,
            pady=8,
            sticky="nsew"
        )

        # =====================================================
        # GRID CONFIGURATION
        # =====================================================

        for frame in [
            plasma_frame,
            performance_frame,
            thermal_frame
        ]:

            for column in range(4):

                frame.grid_columnconfigure(
                    column,
                    weight=1
                )

    # =========================================================
    # SECTION CREATOR
    # =========================================================

    def create_section(
        self,
        parent,
        title
    ):

        frame = tk.LabelFrame(
            parent,
            text=f"  {title}  ",
            font=("Arial", 10, "bold"),
            fg=self.CYAN,
            bg=self.PANEL,
            bd=1,
            relief="solid"
        )

        return frame

    # =========================================================
    # METRIC CREATOR
    # =========================================================

    def create_metric(
        self,
        parent,
        name,
        variable,
        unit
    ):

        frame = tk.Frame(
            parent,
            bg=self.PANEL_LIGHT,
            height=65
        )

        frame.grid_propagate(
            False
        )

        tk.Label(
            frame,
            text=name,
            font=("Arial", 8, "bold"),
            fg=self.MUTED,
            bg=self.PANEL_LIGHT
        ).pack(
            pady=(7, 0)
        )

        value_frame = tk.Frame(
            frame,
            bg=self.PANEL_LIGHT
        )

        value_frame.pack()

        tk.Label(
            value_frame,
            textvariable=variable,
            font=("Arial", 15, "bold"),
            fg=self.WHITE,
            bg=self.PANEL_LIGHT
        ).pack(
            side="left"
        )

        if unit:

            tk.Label(
                value_frame,
                text=f" {unit}",
                font=("Arial", 8),
                fg=self.MUTED,
                bg=self.PANEL_LIGHT
            ).pack(
                side="left",
                pady=(6, 0)
            )

        return frame

    # =========================================================
    # CONTROL PANEL
    # =========================================================

    def create_controls(self):

        frame = tk.Frame(
            self.root,
            bg=self.BG
        )

        frame.pack(
            fill="x",
            padx=25,
            pady=12
        )

        # -----------------------------------------------------
        # START
        # -----------------------------------------------------

        self.start_button = tk.Button(
            frame,
            text="START REACTOR",
            font=("Arial", 10, "bold"),
            fg=self.BG,
            bg=self.GREEN,
            activebackground="#69f0ae",
            width=18,
            height=2,
            bd=0,
            command=self.start_reactor
        )

        self.start_button.pack(
            side="left",
            padx=5
        )

        # -----------------------------------------------------
        # NEXT STAGE
        # -----------------------------------------------------

        self.next_button = tk.Button(
            frame,
            text="NEXT STAGE",
            font=("Arial", 10, "bold"),
            fg=self.BG,
            bg=self.CYAN,
            activebackground="#80eaff",
            width=18,
            height=2,
            bd=0,
            command=self.next_stage
        )

        self.next_button.pack(
            side="left",
            padx=5
        )

        # -----------------------------------------------------
        # SHUTDOWN
        # -----------------------------------------------------

        self.shutdown_button = tk.Button(
            frame,
            text="SHUTDOWN",
            font=("Arial", 10, "bold"),
            fg=self.BG,
            bg=self.YELLOW,
            activebackground="#ffe57f",
            width=18,
            height=2,
            bd=0,
            command=self.shutdown_reactor
        )

        self.shutdown_button.pack(
            side="left",
            padx=5
        )

        # -----------------------------------------------------
        # EMERGENCY
        # -----------------------------------------------------

        self.emergency_button = tk.Button(
            frame,
            text="EMERGENCY STOP",
            font=("Arial", 10, "bold"),
            fg=self.WHITE,
            bg=self.RED,
            activebackground="#ff8a80",
            width=20,
            height=2,
            bd=0,
            command=self.emergency_shutdown
        )

        self.emergency_button.pack(
            side="right",
            padx=5
        )

    # =========================================================
    # EVENT LOG
    # =========================================================

    def create_event_log(self):

        frame = tk.LabelFrame(
            self.root,
            text="  SYSTEM EVENT LOG  ",
            font=("Arial", 9, "bold"),
            fg=self.CYAN,
            bg=self.PANEL,
            bd=1,
            relief="solid"
        )

        frame.pack(
            fill="x",
            padx=25,
            pady=(0, 15)
        )

        self.event_log = tk.Text(
            frame,
            height=4,
            bg="#081018",
            fg=self.TEXT,
            insertbackground=self.WHITE,
            font=("Consolas", 9),
            bd=0,
            state="disabled"
        )

        self.event_log.pack(
            fill="x",
            padx=5,
            pady=5
        )

    # =========================================================
    # EVENT LOGGER
    # =========================================================

    def log_event(
        self,
        event_type,
        message
    ):

        self.event_log.config(
            state="normal"
        )

        self.event_log.insert(
            "end",
            f"[{event_type}] {message}\n"
        )

        self.event_log.see(
            "end"
        )

        self.event_log.config(
            state="disabled"
        )

    # =========================================================
    # START REACTOR
    # =========================================================

    def start_reactor(self):

        old_stage = self.controls.stage

        self.controls.start_sequence()

        if self.controls.stage != old_stage:

            self.log_event(
                "STARTUP",
                "Startup sequence initiated."
            )

        self.update_display()

    # =========================================================
    # NEXT STAGE
    # =========================================================

    def next_stage(self):

        old_stage = self.controls.stage

        self.controls.advance_stage()

        new_stage = self.controls.stage

        if new_stage != old_stage:

            self.log_event(
                "STAGE",
                f"{old_stage} -> {new_stage}"
            )

        else:

            self.log_event(
                "INFO",
                "Reactor remains in current stage."
            )

        self.update_display()

    # =========================================================
    # NORMAL SHUTDOWN
    # =========================================================

    def shutdown_reactor(self):

        if self.controls.stage == "OFF":

            messagebox.showinfo(
                "Reactor Status",
                "The reactor is already OFF."
            )

            return

        self.controls.shutdown_sequence()

        self.log_event(
            "SHUTDOWN",
            "Normal shutdown sequence initiated."
        )

        self.update_display()

    # =========================================================
    # EMERGENCY SHUTDOWN
    # =========================================================

    def emergency_shutdown(self):

        self.controls.emergency_shutdown()

        self.log_event(
            "EMERGENCY",
            "Emergency shutdown completed."
        )

        self.update_display()

        messagebox.showwarning(
            "EMERGENCY SHUTDOWN",
            "The simulated reactor has been shut down."
        )

    # =========================================================
    # UPDATE DISPLAY
    # =========================================================

    def update_display(self):

        reactor = self.reactor

        # -----------------------------------------------------
        # STATUS
        # -----------------------------------------------------

        self.status_var.set(
            reactor.status
        )

        self.stage_var.set(
            self.controls.stage
        )

        # -----------------------------------------------------
        # STATUS COLOR
        # -----------------------------------------------------

        if reactor.status == "STEADY STATE":

            self.status_indicator.config(
                fg=self.GREEN
            )

        elif reactor.status in [
            "FUSION",
            "HEATING",
            "CURRENT RAMP",
            "STARTING"
        ]:

            self.status_indicator.config(
                fg=self.YELLOW
            )

        elif reactor.status in [
            "RAMP DOWN",
            "SHUTTING DOWN"
        ]:

            self.status_indicator.config(
                fg=self.YELLOW
            )

        elif reactor.status == "OFF":

            self.status_indicator.config(
                fg=self.RED
            )

        else:

            self.status_indicator.config(
                fg=self.CYAN
            )

        # -----------------------------------------------------
        # PLASMA
        # -----------------------------------------------------

        self.temperature_var.set(
            f"{reactor.plasma_temperature:.2f}"
        )

        self.density_var.set(
            f"{reactor.plasma_density:.2e}"
        )

        self.current_var.set(
            f"{reactor.plasma_current:.2f}"
        )

        self.toroidal_var.set(
            f"{reactor.toroidal_field:.2f}"
        )

        # -----------------------------------------------------
        # PERFORMANCE
        # -----------------------------------------------------

        self.confinement_var.set(
            f"{reactor.confinement:.2f}"
        )

        self.stability_var.set(
            f"{reactor.plasma_stability:.2f}"
        )

        self.heating_var.set(
            f"{reactor.heating_power:.2f}"
        )

        self.fusion_var.set(
            f"{reactor.fusion_power:.2f}"
        )

        # -----------------------------------------------------
        # THERMAL
        # -----------------------------------------------------

        self.q_var.set(
            f"{reactor.q_factor:.2f}"
        )

        self.wall_load_var.set(
            f"{reactor.wall_load:.2f}"
        )

        self.divertor_var.set(
            f"{reactor.divertor_temperature:.2f}"
        )

        self.poloidal_var.set(
            f"{reactor.poloidal_field:.2f}"
        )


# =============================================================
# APPLICATION ENTRY POINT
# =============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = FusionReactorGUI(
        root
    )

    root.mainloop()