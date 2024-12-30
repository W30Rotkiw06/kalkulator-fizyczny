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

@anvil.server.callable
def calculate_wave(m, n, is_lambda):
  planck_const = 6.62* pow(10, -34)
  c = 3 * pow(10, 8)
  e_m = (-13.606)/(m*m)
  e_n = (-13.606)/(n*n)
  delta_e = abs(e_m - e_n) * ( 1.6 * pow(10, -19))

  if is_lambda:
    wawe_lenght = (planck_const * c) / delta_e
    return format_number(wawe_lenght, 3)
  else:
    wave_freq = delta_e / planck_const
    return format_number(wave_freq, 3)