from fusion_core import FusionReactor
from plasma_physics import PlasmaPhysics
from control_system import ControlSystem


# =========================================================
# INITIALIZE REACTOR SYSTEM
# =========================================================

reactor = FusionReactor()

physics = PlasmaPhysics(reactor)

controls = ControlSystem(reactor, physics)


# =========================================================
# SIMULATOR START
# =========================================================

print("=== FUSION REACTOR SIMULATOR ===")

controls.display_stage()


# =========================================================
# STARTUP SEQUENCE
# =========================================================

controls.start_sequence()

controls.advance_stage()   # VACUUM → MAGNET CHARGE
controls.advance_stage()   # MAGNET CHARGE → PLASMA INIT
controls.advance_stage()   # PLASMA INIT → CURRENT RAMP
controls.advance_stage()   # CURRENT RAMP → HEATING
controls.advance_stage()   # HEATING → FUSION
controls.advance_stage()   # FUSION → STEADY STATE


# =========================================================
# FINAL REACTOR STATUS
# =========================================================

print("\n=== FINAL REACTOR STATUS ===")

reactor.display_status()

controls.display_stage()


# =========================================================
# ITER REFERENCE CONFIGURATION
# =========================================================

print("\n=== ITER REFERENCE CONFIGURATION ===")

print(
    f"Major Radius:        "
    f"{reactor.config.MAJOR_RADIUS} m"
)

print(
    f"Minor Radius:        "
    f"{reactor.config.MINOR_RADIUS} m"
)

print(
    f"Toroidal Field:      "
    f"{reactor.config.TOROIDAL_FIELD} T"
)

print(
    f"Max Plasma Current:  "
    f"{reactor.config.MAX_PLASMA_CURRENT} MA"
)

print(
    f"Target Fusion Power: "
    f"{reactor.config.TARGET_FUSION_POWER} MW"
)

print(
    f"Target Q Factor:     "
    f"{reactor.config.TARGET_Q}"
)