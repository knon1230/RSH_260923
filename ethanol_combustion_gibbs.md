# Ethanol combustion: standard Gibbs free energy

## Result

For the standard-state reaction at 298.15 K and 1 bar,

```text
C2H5OH(l) + 3 O2(g) -> 2 CO2(g) + 3 H2O(l)
```

the calculation gives:

```text
Delta G° = -1325.796 kJ/mol ethanol
```

The negative result means that the reaction is strongly thermodynamically
favorable under these standard-state conditions. This is a standard-state
thermochemical calculation, not a kinetic prediction of flame ignition or
burning rate.

## Method

The included `ethanol_combustion_gibbs.py` evaluates

```text
Delta H° = sum(nu_i Delta_f H_i°) = -1366.910 kJ/mol
Delta S° = sum(nu_i S_i°)         = -137.896 J/(mol K)
Delta G° = Delta H° - T Delta S°  = -1325.796 kJ/mol
```

where positive stoichiometric coefficients denote products and negative
coefficients denote reactants.

## Input data

All data are from NIST Chemistry WebBook, SRD 69. Values are quoted in the
script so that the arithmetic is reproducible.

| Species | Phase | Delta_f H° (kJ/mol) | S° (J/(mol K)) |
| --- | --- | ---: | ---: |
| Ethanol | liquid | -277.6 | 159.86 |
| Oxygen | gas | 0.0 | 205.152 |
| Carbon dioxide | gas | -393.51 | 213.785 |
| Water | liquid | -285.830 | 69.95 |

Sources:

- [Ethanol condensed-phase data](https://webbook.nist.gov/cgi/cbook.cgi?ID=C64175&Mask=B)
- [Oxygen gas-phase data](https://webbook.nist.gov/cgi/cbook.cgi?ID=C7782447&Mask=17)
- [Carbon dioxide gas-phase data](https://webbook.nist.gov/cgi/cbook.cgi?ID=C124389&Mask=1&Units=SI)
- [Water condensed-phase data](https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Mask=37)

## MAESTRO scope

MAESTRO's live catalog supports molecular thermochemistry and
minimum-energy-path reaction profiles, but it has no task that combines the
stoichiometric Gibbs energies of several independently specified species.
`ReactionProfileTask` was not used because it requires a minimum-energy path
and a transition state, neither of which represents this combustion reaction.
