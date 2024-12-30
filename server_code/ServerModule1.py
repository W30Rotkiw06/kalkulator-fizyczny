import anvil.server
from math import log

def format_number(num, digits=3):
  if log(num, 10) >= 3 or log(num, 10) < -2:
    return format(num, ".2e")
  else: 
    significant_figures  = digits - 1 - round(log(num, 10), 0)
    return round(num, int(significant_figures))

@anvil.server.callable
def calculate_gravitational_force(m1, m2, r):
  G = 6.61 * pow(10, -11)
  gravity = (G *m1 *m2) / (r*r)
  gravity = round(gravity, 3)
  return format_number(gravity, 3)

@anvil.server.callable
def calculate_orbit_escape_velocity(m1, r, velocity_number):
  G = 6.61 * pow(10, -11)
  velocity = (velocity_number * G *m1) / r
  velocity = pow(velocity, 0.5)
  return format_number(velocity, 3)

@anvil.server.callable
def calculate_photon_energy(f, unit_multiplicator):
  planck_const = 6.62* pow(10, -34)
  energy = planck_const * f * unit_multiplicator
  return format_number(energy, 3)