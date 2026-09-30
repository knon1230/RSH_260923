"""Calculate the standard Gibbs energy of ethanol combustion at 298.15 K.

Reaction: C2H5OH(l) + 3 O2(g) -> 2 CO2(g) + 3 H2O(l)

The tabulated standard formation enthalpies and absolute entropies below are
from NIST Chemistry WebBook (SRD 69).  See ethanol_combustion_gibbs.md for
the exact sources and calculation result.
"""

from __future__ import annotations

from dataclasses import dataclass


TEMPERATURE_K = 298.15


@dataclass(frozen=True)
class ThermochemicalData:
    formation_enthalpy_kj_per_mol: float
    entropy_j_per_mol_k: float


# Stoichiometric coefficients are positive for products and negative for
# reactants. Values correspond to the phases shown in the reaction above.
SPECIES = {
    "C2H5OH(l)": (-1, ThermochemicalData(-277.6, 159.86)),
    "O2(g)": (-3, ThermochemicalData(0.0, 205.152)),
    "CO2(g)": (2, ThermochemicalData(-393.51, 213.785)),
    "H2O(l)": (3, ThermochemicalData(-285.830, 69.95)),
}


def reaction_property(attribute: str) -> float:
    """Return a stoichiometrically weighted thermochemical property."""
    return sum(
        coefficient * getattr(data, attribute)
        for coefficient, data in SPECIES.values()
    )


def main() -> None:
    delta_h_kj_per_mol = reaction_property("formation_enthalpy_kj_per_mol")
    delta_s_j_per_mol_k = reaction_property("entropy_j_per_mol_k")
    delta_g_kj_per_mol = delta_h_kj_per_mol - TEMPERATURE_K * delta_s_j_per_mol_k / 1000

    print("C2H5OH(l) + 3 O2(g) -> 2 CO2(g) + 3 H2O(l)")
    print(f"T = {TEMPERATURE_K:.2f} K")
    print(f"Delta H° = {delta_h_kj_per_mol:.3f} kJ/mol")
    print(f"Delta S° = {delta_s_j_per_mol_k:.3f} J/(mol K)")
    print(f"Delta G° = {delta_g_kj_per_mol:.3f} kJ/mol ethanol")


if __name__ == "__main__":
    main()
