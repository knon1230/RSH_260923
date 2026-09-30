---
task: unsupported
engine: none
error_class: support_gap
failure_class: setup_error
outcome: support_gap
---
Symptom: The requested quantity is the standard Gibbs free energy of the stoichiometric combustion reaction C2H5OH + 3 O2 -> 2 CO2 + 3 H2O.
Attempts: Searched the live MAESTRO catalog for free energy, thermochemistry, combustion, reaction energy, Gibbs, and the Korean term for free energy. ThermoTask calculates one molecule's Gibbs free energy. ReactionProfileTask produces reaction_free_energy only from a minimum-energy path and reactant/product/transition-state Gibbs energies.
Result: No MAESTRO task composes stoichiometric Gibbs energies of multiple independent reactants and products, so standard combustion free energy is unsupported as one MAESTRO calculation.
Context: The closest supported workflow is ReactionProfileTask, intended for an elementary reaction with an MEP and transition state; it is not appropriate for the multi-species ethanol combustion reaction.
